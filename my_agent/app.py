from __future__ import annotations

import asyncio
import os
import uuid
from typing import Any

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from shiny import App, reactive, render, ui

from agent import root_agent

APP_NAME = "my_agent_shiny"
DEFAULT_USER_ID = os.getenv("AGENT_USER_ID", "docker-user")

_session_service = InMemorySessionService()
_runner = Runner(agent=root_agent, app_name=APP_NAME, session_service=_session_service)
_session_id = str(uuid.uuid4())
_session_ready = False
_session_lock = asyncio.Lock()


async def _ensure_session() -> None:
    global _session_ready
    if _session_ready:
        return

    async with _session_lock:
        if _session_ready:
            return
        await _session_service.create_session(
            app_name=APP_NAME,
            user_id=DEFAULT_USER_ID,
            session_id=_session_id,
        )
        _session_ready = True


def _extract_text_from_event(event: Any) -> str:
    content = getattr(event, "content", None)
    if content is None:
        return ""

    parts = getattr(content, "parts", None)
    if not parts:
        return ""

    chunks: list[str] = []
    for part in parts:
        text = getattr(part, "text", None)
        if text:
            chunks.append(text)
    return "\n".join(chunks).strip()


async def ask_agent(prompt: str) -> str:
    cleaned_prompt = prompt.strip()
    if not cleaned_prompt:
        return "Veuillez saisir un message."

    await _ensure_session()

    user_message = types.Content(role="user", parts=[types.Part(text=cleaned_prompt)])
    events = _runner.run(
        user_id=DEFAULT_USER_ID,
        session_id=_session_id,
        new_message=user_message,
    )

    chunks: list[str] = []
    for event in events:
        text = _extract_text_from_event(event)
        if text:
            chunks.append(text)

    if chunks:
        return "\n".join(chunks).strip()
    return "Aucune réponse textuelle retournée par l'agent."


app_ui = ui.page_fluid(
    ui.h2("Agent ADK avec Shiny"),
    ui.p("Saisissez une demande. L'agent chargé est celui de my_agent/agent.py."),
    ui.input_text_area("prompt", "Message", rows=8, placeholder="Décris la scène à générer..."),
    ui.input_action_button("send", "Envoyer"),
    ui.hr(),
    ui.output_text_verbatim("response"),
)


def server(input, output, session):
    last_response = reactive.value("Prêt.")

    @reactive.effect
    @reactive.event(input.send)
    async def _send_prompt() -> None:
        reply = await ask_agent(input.prompt())
        last_response.set(reply)

    @output
    @render.text
    def response() -> str:
        return last_response()


app = App(app_ui, server)
