from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

def load_granite_model():
    model_dir = "./granite-3.3-2b-instruct"
    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    model = AutoModelForCausalLM.from_pretrained(model_dir)
    pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
    return pipe
