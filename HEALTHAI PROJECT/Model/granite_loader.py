import os
from pathlib import Path
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Import the download function
from download_model import download_model

def load_granite_model():
    model_dir = Path("./granite-3.3-2b-instruct")

    # If model folder is missing, download it
    if not model_dir.exists() or not any(model_dir.iterdir()):
        print("🔍 Granite model not found. Downloading now...")
        download_model()
    else:
        print("✅ Granite model found locally. Proceeding to load...")

    # Load tokenizer and model from local directory
    tokenizer = AutoTokenizer.from_pretrained(str(model_dir))
    model = AutoModelForCausalLM.from_pretrained(str(model_dir))
    
    # Create and return the pipeline
    pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
    return pipe
