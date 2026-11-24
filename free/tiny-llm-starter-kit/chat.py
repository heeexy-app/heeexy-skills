"""Chat with MiniMind (minimind-3, about 64M parameters) on a normal CPU. No GPU needed.
Setup once:  pip install torch transformers huggingface_hub
Run:         python chat.py            (downloads the ~128 MB model the first time)
Type a question and press Enter. Empty line or Ctrl+C quits.
Model: https://huggingface.co/jingyaogong/minimind-3 (Apache-2.0, by jingyaogong). This script: MIT, heeexy.app Lab."""
import torch
from huggingface_hub import snapshot_download
from transformers import AutoTokenizer, AutoModelForCausalLM, TextStreamer

path = snapshot_download("jingyaogong/minimind-3")
tok = AutoTokenizer.from_pretrained(path)
model = AutoModelForCausalLM.from_pretrained(path, dtype=torch.float32).eval()
print(f"loaded {sum(p.numel() for p in model.parameters()):,} parameters on CPU")
history = []
while True:
    q = input("\nyou> ").strip()
    if not q:
        break
    history.append({"role": "user", "content": q})
    ids = tok.apply_chat_template(history[-6:], add_generation_prompt=True, return_tensors="pt", open_thinking=False)
    ids = ids["input_ids"] if hasattr(ids, "input_ids") else ids
    print("minimind> ", end="", flush=True)
    with torch.no_grad():
        out = model.generate(ids, max_new_tokens=200, do_sample=True, temperature=0.7, top_p=0.85, repetition_penalty=1.05,
                             streamer=TextStreamer(tok, skip_prompt=True, skip_special_tokens=True))
    history.append({"role": "assistant", "content": tok.decode(out[0][ids.shape[1]:], skip_special_tokens=True)})
