FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV SHINY_PORT=8080
ENV SHINY_HOST=0.0.0.0

WORKDIR /app

COPY my_agent/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY my_agent ./my_agent

WORKDIR /app/my_agent

EXPOSE 8080

CMD ["shiny", "run", "--host", "127.0.0.1", "--port", "8081", "app.py"]
