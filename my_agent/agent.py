from typing import Any

from google.adk.agents import llm_agent
from google.adk.sessions import vertex_ai_session_service
from vertexai.preview.reasoning_engines import AdkApp
from google.adk.tools import agent_tool
from google.adk.tools.google_search_tool import GoogleSearchTool
from google.adk.tools import url_context



VertexAiSessionService = vertex_ai_session_service.VertexAiSessionService


class AgentClass:

  def __init__(self):
    self.app = None

  def session_service_builder(self):
    return VertexAiSessionService()

  def set_up(self):
    """Sets up the ADK application."""
    sous_agent_google_search_agent = llm_agent.LlmAgent(
      name='Sous_agent_google_search_agent',
      model='gemini-3-flash-preview',
      description=(
          'Agent specialized in performing Google searches.'
      ),
      sub_agents=[],
      instruction='Use the GoogleSearchTool to find information on the web.',
      tools=[
        GoogleSearchTool()
      ],
    )
    sous_agent_url_context_agent = llm_agent.LlmAgent(
      name='Sous_agent_url_context_agent',
      model='gemini-3-flash-preview',
      description=(
          'Agent specialized in fetching content from URLs.'
      ),
      sub_agents=[],
      instruction='Use the UrlContextTool to retrieve content from provided URLs.',
      tools=[
        url_context
      ],
    )
    sousagent = llm_agent.LlmAgent(
      name='sousagent',
      model='gemini-3-flash-preview',
      description=(
          'Run the code'
      ),
      sub_agents=[],
      instruction='Run the TestObjet :\nnew Thread(testObjectRef).start();\net récupérer les images résultantes et/ou la vidéo et/ou le modèle avec setGenerate(GENERATE_IMAGES, ...)',
      tools=[
        agent_tool.AgentTool(agent=sous_agent_google_search_agent),
        agent_tool.AgentTool(agent=sous_agent_url_context_agent)
      ],
    )
    agent_scene_empty3_google_search_agent = llm_agent.LlmAgent(
      name='Agent_scene_Empty3_google_search_agent',
      model='gemini-3-flash-preview',
      description=(
          'Agent specialized in performing Google searches.'
      ),
      sub_agents=[],
      instruction='Use the GoogleSearchTool to find information on the web.',
      tools=[
        GoogleSearchTool()
      ],
    )
    agent_scene_empty3_url_context_agent = llm_agent.LlmAgent(
      name='Agent_scene_Empty3_url_context_agent',
      model='gemini-3-flash-preview',
      description=(
          'Agent specialized in fetching content from URLs.'
      ),
      sub_agents=[],
      instruction='Use the UrlContextTool to retrieve content from provided URLs.',
      tools=[
        url_context
      ],
    )
    root_agent = llm_agent.LlmAgent(
      name='Agent_scene_Empty3',
      model='gemini-3-flash-preview',
      description=(
          'Codage en java, en kotlin à partir de la bibliothèque one.empty3:empty3-library-mp'
      ),
      sub_agents=[sousagent],
      instruction='Créer un object one.empty3.library.Scene et y ajouter des objets de type one.empty3.library.Representable et classes dérivées.\nSi l\'utilisateur demande une vidéo, intégrer le document Scene scene dans la classe TestObjet ou plutôt TestObjetSub en surchargeant les méthodes void ginit() qui permet d\'initialiser l\'état des objets pour l\'ensemble du film, et la méthode void finit() qui permet de mettre à jour les objets à chaque image de la vidéo.\nSi une image est demandée, écrire le code avec one.empty3.library.ZBufferImpl et Scene et Camera.\nUtiliser de préférence les classes one.empty3.libs.Image et one.empty3.libs.Color aux classes java.awt.Color et BufferedImage. Par exemple image.saveFile() de préférence à ImageIO.write() pour les manipulations de textures, de couleurs, et d\'images\nOn utilise un changement d\'axes Representable.setOrig(Point3D) pour le déplacement des objets et pour la rotation Representable.setVectX(Point3D), Representable.setVectY(Point3D), Representable.setVectZ(Point3D)\nOn utilise la méthode setGenerate(int generateBinOption) comme: setGenerate(getGenerate()|newOption) .\n\nRemarks\n1. Degenerate Camera Matrix (The \"Up\" Vector Problem)\nThe primary reason for blank images in this library when looking straight along the Z-axis is a zeroed camera matrix. In GreenCubeAnimation.java, you initialize the camera as:\nCamera camera = new Camera(new Point3D(0d, 0d, 5d), Point3D.O0);\nWhen a camera is created without an explicit \"up\" vector, the library attempts to calculate a default one. However, if the camera is looking exactly along the Z-axis (from z=5 to z=0), the mathematical cross-product used for this calculation involves the global Z-axis. This results in a zero vector (0,0,0), which causes the entire projection matrix to fail.\nFix: Provide an explicit \"up\" vector (usually Point3D.Y) to the camera constructor:\nCamera camera = new Camera(new Point3D(0d, 0d, 5d), Point3D.O0, Point3D.Y);\n3. Use latest version of the library i.e. one.empty3:empty3-library-mp:2026.4.12-25\n4. Use subclass one.empty3.Color.newCol(redFloat, greenFloat, blueFloat) instead of new java.awt.Color(redFloat, greenFloat, blueFloat)\n5. Use subclass one.empty3.libs.Image.saveFile(File file) instead of ImageIO.write(Image image, String format, File file) and access to image bitmap with Image.getBi()\n6. Use model STL or OBJ when needed. Class for OBJ is E3Model. Use in-code obj text or a .obj file.\n7. Use .0 or d suffix for double value instead of Integer literal',
      tools=[
        agent_tool.AgentTool(agent=agent_scene_empty3_google_search_agent),
        agent_tool.AgentTool(agent=agent_scene_empty3_url_context_agent)
      ],
    )

    self.app = AdkApp(
        agent=root_agent,
        session_service_builder=self.session_service_builder
    )

  async def stream_query(self, query: str, user_id: str = 'test') -> Any:
    """Streaming query."""
    async for chunk in self.app.async_stream_query(
        message=query,
        user_id=user_id,
    ):
      yield chunk


app = AgentClass()

root_agent = app