# ==========================
# config.py
# ==========================

from pathlib import Path
import torch

# --------------------------
# Project Paths
# --------------------------

ROOT = Path(__file__).resolve().parent

MODEL_PATH = ROOT / "best_model.pt"
TOKENIZER_PATH = ROOT / "tokenizer.json"

TRAIN_BIN = ROOT / "train.bin"
VAL_BIN = ROOT / "val.bin"

# --------------------------
# Device
# --------------------------

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# --------------------------
# GPT Model Config
# --------------------------

VOCAB_SIZE = 16000
BLOCK_SIZE = 256

N_LAYER = 6
N_HEAD = 8
N_EMBD = 512

DROPOUT = 0.1

# --------------------------
# Training
# --------------------------

BATCH_SIZE = 32

LEARNING_RATE = 3e-4

WEIGHT_DECAY = 0.01

MAX_ITERS = 5000

EVAL_INTERVAL = 250

EVAL_ITERS = 50

# --------------------------
# Generation
# --------------------------

MAX_NEW_TOKENS = 128

TEMPERATURE = 0.7

TOP_K = 40

TOP_P = 0.9

REPETITION_PENALTY = 1.15

# --------------------------
# Flask
# --------------------------

HOST = "0.0.0.0"

PORT = 5000

DEBUG = True