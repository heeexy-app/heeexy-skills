# Tiny LLM Starter Kit

Run, then train, your own tiny language model with **MiniMind**, the open-source (Apache-2.0) project by jingyaogong that trains a ~64M-parameter LLM from scratch in plain PyTorch.
Project: https://github.com/jingyaogong/minimind · Model: https://huggingface.co/jingyaogong/minimind-3

## Who it is for
Anyone who wants to SEE how ChatGPT-style models are made, not just use them: students, developers, curious creators. Level 1 needs only a laptop.

## Level 1: chat with it on your laptop (free, no GPU, 5 minutes)
1. Install Python 3.10+.
2. In a terminal: `pip install torch transformers huggingface_hub`
3. Download `chat.py` from this page and run: `python chat.py`
   The first run downloads the model (about 128 MB). Type a question, press Enter.
   We ran it on a plain 4-core CPU: 63,912,192 parameters loaded in 1.3 s, about 70 tokens a second.
4. Try the test sheet below and see where a 64M model is smart and where it breaks.
   (Prefer one line? If you use Ollama: `ollama run jingyaogong/minimind-3`)

## Level 2: train your own from zero (needs a GPU, about 3 yuan of rent)
The project's own numbers (README "Training Cost", one RTX 3090, estimates, prices vary): pretraining ~1.21 h (~1.57 CNY) + SFT ~1.10 h (~1.43 CNY) = about 3 CNY (~0.43 USD at the README's 7 CNY = 1 USD).
1. Rent a machine with one RTX 3090 (or use your own NVIDIA GPU).
2. `git clone --depth 1 https://github.com/jingyaogong/minimind && cd minimind && pip install -r requirements.txt`
3. Download `pretrain_t2t_mini.jsonl` and `sft_t2t_mini.jsonl` from the dataset page linked in the README (https://www.modelscope.cn/datasets/gongjy/minimind_dataset/files) into `./dataset`.
4. `cd trainer && python train_pretrain.py`   (the model learns language: next-token prediction)
5. `python train_full_sft.py`   (the model learns to answer like an assistant)
6. `cd .. && python eval_llm.py --weight full_sft`   and talk to the model YOU trained.
Watch the loss number fall while it trains: that is the model learning.

## Test sheet (what we asked, 2026-11-24)
| question | what minimind-3 said |
|---|---|
| What is the capital of France? | "The capital of France is Paris." (then repeats itself, and ends with "Paris has the capital city of Belgium") |
| What is 17 + 25? | "17 + 25 = 41." (wrong: 42) |
| What is the capital of Egypt? | mixed answer that ended with "The capital of Egypt is Paris." |
Your turn: try a short poem, a definition, a one-line translation. Small models are fluent but forget facts and fail at math: that is the lesson.

## Licences
MiniMind and the minimind-3 weights: Apache-2.0 (free). This kit (`chat.py` + this guide): free, MIT.
