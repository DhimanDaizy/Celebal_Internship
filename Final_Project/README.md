# 🤖 MiniGPT AI

A modern AI chatbot built using a custom GPT-style Transformer model trained with PyTorch and deployed with a Flask backend. The project features a clean, responsive web interface and demonstrates end-to-end development of a lightweight conversational AI system.As the MiniGPT is a project that focuses on the foundational implementation and training of an autoregressive, decoder-only Large Language Model (LLM) built completely from scratch using PyTorch. Unlike standard projects that rely on pre-trained checkpoints from model hubs, this project implements the mathematical and computational layers of the modern Transformer architecture directly from raw tensors.The primary objective is to demonstrate a deep, low-level understanding of deep learning workflows, causal attention mechanics, self-attention routing, and sequence-to-sequence engineering.

The model implementation strictly adheres to the standard generative GPT framework:
1.) Architecture Type: Autoregressive Decoder-Only Transformer
2.) Core Mechanisms: Multi-Head Causal Self-Attention with causal masking (torch.tril)
3.) Layer Normalization: Pre-LayerNorm (Pre-LN) routing for improved gradient stability
4.) Vocabulary Size (V): 16,000 tokens
5.) Context Length / Block Size (T): 256 tokens
6.) Embedding Dimension (C): 512 channels
7.) Network Depth: 6 identical Transformer Blocks, totaling 8 Attention Heads per block

Technical Justification of Training MetricsDuring initial baseline tracking, the cross-entropy loss converged around a stable plateau between 4.9 and 5.3.

1. Mathematical Breakdown of Perplexity
#Cross-entropy loss directly scales into language perplexity via the exponential function
(\(PPL = e^{\text{loss}}\)).
A cross-entropy loss of 5.0 mathematically equates to a perplexity of approximately 148.4.Interpretation: Out of a massive structural vocabulary configuration of 16,000 distinct words, the model successfully restricted its search space down to guessing from roughly the top 148 most mathematically viable choices. This confirms the multi-head attention blocks are actively routing features and extracting statistical language context.

2. Constraints of Pre-training vs Fine-tuning Data
#The project processes the Databricks-Dolly dataset. While Dolly is highly effective for downstream Supervised Fine-Tuning (SFT) of already mature, pre-trained base engines (which already possess foundational world facts and grammar), it contains roughly 15,000 dialogue pairs.Training an LLM from scratch to achieve highly text-accurate loss (under 2.0) requires billions or trillions of foundational tokens (such as FineWeb or RedPajama) alongside immense distributed hardware infrastructure.
#Under constrained student compute limits, establishing this stable convergence proves that the internal neural gradients are flowing smoothly without vanishing or exploding.

## 📸 Preview

<img width="1364" height="627" alt="image" src="https://github.com/user-attachments/assets/31509e90-b898-4411-8ef1-7678a2958db8" />
<img width="1362" height="621" alt="image" src="https://github.com/user-attachments/assets/7d3aeb02-04d5-4c59-a7c1-81b2df6c639a" />


---

## ✨ Features

- 🧠 Custom GPT-style Transformer architecture
- 💬 Interactive AI chatbot
- ⚡ Flask API backend
- 🎨 Modern responsive frontend
- 🌙 Dark Glassmorphism UI
- ⌨️ Enter to Send support
- 📱 Mobile-friendly interface
- 🤖 AI typing animation
- 📋 Copy AI responses
- 🗑️ Clear chat functionality

---

## 🛠️ Tech Stack

### Backend
- Python
- PyTorch
- Flask

### Frontend
- HTML5
- CSS3
- JavaScript

### AI
- Custom GPT Architecture
- Transformer
- Self-Attention
- Byte Pair Encoding (Tokenizer)

---

## 📂 Project Structure

```
MiniGPT/
│
├── backend/____requirements.txt
│   ├── app.py
│   ├── inference.py
│   ├── model.py
│   ├── tokenizer.json
│   ├── config.py
│   └── best_model.pt

│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/DhimanDaizy/Celebal_Internship.git
```

Move into the project:

```bash
cd Celebal_Internship
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Flask server:

```bash
python backend/app.py
```

Open:

```
http://localhost:5000
```

---

## 🚀 Future Improvements

- User authentication
- Chat history
- Streaming responses
- Theme switcher
- Voice input
- Docker support
- Cloud deployment
- Model optimization

---

## 📈 Learning Outcomes

This project demonstrates:

- Transformer Architecture
- Attention Mechanism
- NLP Pipeline
- Deep Learning using PyTorch
- REST API Development
- Frontend Integration
- Model Deployment Basics

---

## 👨‍💻 Author

**Daizy Dhiman**

GitHub: https://github.com/DhimanDaizy

---

## 📄 License

This project is developed for educational and portfolio purposes.
