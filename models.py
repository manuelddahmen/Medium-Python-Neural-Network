import kagglehub

# Download latest version
path = kagglehub.model_download("spsayakpaul/cartoongan/tfLite/fp16")

print("Path to model files:", path)
