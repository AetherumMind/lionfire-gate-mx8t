import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from safetensors.torch import load_file

print("📦 Loading GPT-2 base model...")
model = AutoModelForCausalLM.from_pretrained("gpt2")
tokenizer = AutoTokenizer.from_pretrained("gpt2")

print("🔓 Loading LoRA weights...")
lora = load_file("NSFW_master.safetensors")
alpha = lora['alpha'].item()
down = lora['lora_down.weight']
up = lora['lora_up.weight']
rank = down.shape[0]
adjustment = torch.matmul(up, down) * (alpha / rank)

print("🧠 Injecting into model...")
model.transformer.h[0].attn.c_attn.weight.data[:768] += adjustment

print("💬 Ready. Type a prompt:")
prompt = input(">>> ")
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=100)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
