# Mathematics of Neural Network

This code is part of my post on **[medium](https://medium.com/@omaraflak/math-neural-network-from-scratch-in-python-d6da9f29ce65)**.

It shows how to create a neural network **from scratch** in **Python**, going all the way from the **mathamatics** to the code.

# Run it

```shell
python example_xor.py
python example_conv.py
python example_mnist.py
```

# Agent Docker + Shiny (`my_agent/`)

Build image:

```shell
docker build -f my_agent/Dockerfile -t my-agent-shiny .
```

Run container:

```shell
docker run --rm -p 8080:8080 \
  -e GOOGLE_API_KEY=YOUR_REAL_API_KEY \
  my-agent-shiny
```

Then open `http://localhost:8080`.

# Deploy ADK agent securely (Cloud Run)

Do not commit API keys to source control. Store them in Google Secret Manager and mount them as env vars in Cloud Run.

```shell
# Create secret (once)
echo -n "YOUR_REAL_API_KEY" | gcloud secrets create GOOGLE_API_KEY --data-file=-

# Or update secret (new version)
echo -n "YOUR_REAL_API_KEY" | gcloud secrets versions add GOOGLE_API_KEY --data-file=-

# Deploy ADK agent folder with secret injection
python -m google.adk.cli deploy cloud_run \
  --project=YOUR_PROJECT_ID \
  --region=europe-west1 \
  --service_name=agent-empty3 \
  my_agent \
  -- \
  --allow-unauthenticated \
  --set-secrets=GOOGLE_API_KEY=GOOGLE_API_KEY:latest \
  --set-env-vars=GOOGLE_GENAI_USE_VERTEXAI=true,GOOGLE_CLOUD_LOCATION=europe-west1
```
