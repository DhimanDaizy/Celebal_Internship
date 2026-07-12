import re
import torch
from tokenizers import Tokenizer

from config import *
from model import GPT, GPTConfig

# ==========================================
# Load Tokenizer
# ==========================================

tokenizer = Tokenizer.from_file(str(TOKENIZER_PATH))

# ==========================================
# Build Model
# ==========================================

config = GPTConfig(
    vocab_size=VOCAB_SIZE,
    block_size=BLOCK_SIZE,
    n_layer=N_LAYER,
    n_head=N_HEAD,
    n_embd=N_EMBD,
    dropout=DROPOUT,
)

model = GPT(config)

checkpoint = torch.load(
    MODEL_PATH,
    map_location=DEVICE
)

if isinstance(checkpoint, dict) and "model_state_dict" in checkpoint:
    model.load_state_dict(checkpoint["model_state_dict"])
else:
    model.load_state_dict(checkpoint)

model.to(DEVICE)
model.eval()

print("✅ Model Loaded Successfully")


# ==========================================
# Clean Response
# ==========================================

def clean_response(text, prompt):

    # Prompt remove
    if text.startswith(prompt):
        text = text[len(prompt):]

    # Special token remove
    text = text.replace("<|endoftext|>", "")

    # Multiple spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()


# ==========================================
# Generate
# ==========================================

@torch.no_grad()
def generate(prompt):

    prompt = prompt.strip()

    ids = tokenizer.encode(prompt).ids

    x = torch.tensor(
        [ids],
        dtype=torch.long,
        device=DEVICE
    )

    output = model.generate(
        x,
        max_new_tokens=MAX_NEW_TOKENS,
        temperature=TEMPERATURE,
        top_k=TOP_K
    )

    generated_ids = output[0].tolist()

    generated_text = tokenizer.decode(generated_ids)

    return clean_response(generated_text, prompt)


# ==========================================
# Chat Function
# ==========================================

def chat(user_input):

    try:

        # IMPORTANT:
        # Same format as training dataset
        prompt = f"User: {user_input}\nAssistant:"

        response = generate(prompt)

        if response == "":
            return "Sorry, I couldn't generate a response."

        return response

    except Exception as e:
        return f"Error: {e}"


# ==========================================
# Test
# ==========================================

if __name__ == "__main__":

    while True:

        user = input("You : ")

        if user.lower() in ["exit", "quit"]:
            break

        print("Bot :", chat(user))