# PalTrack-RAG
# 🇵🇸 PalTrack RAG Chatbot

A **Retrieval-Augmented Generation (RAG) chatbot** designed to provide **accurate, fact-based answers about Palestine** by leveraging a **local knowledge base and Mistral LLM**.

## 🚀 Features
- **Retrieval-Augmented Generation (RAG)** using FAISS
- **Runs locally** with **Ollama + Mistral 7B** (no API costs!)
- **Fast & efficient** document retrieval from a structured Palestine knowledge base
- **Expandable** – Easily add more historical data or real-time news retrieval

## 📌 Getting Started

### ** 1. Clone the Repository**
```bash
git clone https://github.com/amirValiulla32/PalTrack-RAG.git
cd PalTrack-RAG
```

### ** 2. Set Up a Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate  # (Mac/Linux)
venv\Scripts\activate     # (Windows)
```

### ** 3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### ** 4. Install & Run Ollama**
```bash
brew install ollama  # (Mac)
curl -fsSL https://ollama.com/install.sh | sh  # (Linux)
ollama serve &
ollama pull mistral

brew services start ollama 
```

### ** 5. Build the Vector Database**
```bash
python vector_db.py
```

### ** 6. Run the Chatbot**
```bash
python chatbot.py
```
✅ **Now you can ask questions about Palestine!**

## 🛑 Stopping Ollama
To stop Ollama after use:
```bash
brew services stop ollama  # Mac
pkill -9 ollama            # Linux
```

## 🔧 Troubleshooting
**Issue: `ModuleNotFoundError` for dependencies**
- Make sure you activated your virtual environment:  
  ```bash
  source venv/bin/activate  # (Mac/Linux)
  venv\Scripts\activate     # (Windows)
  ```
- Try reinstalling dependencies:  
  ```bash
  pip install -r requirements.txt
  ```

**Issue: `Ollama` not found**
- Ensure Ollama is installed:  
  ```bash
  brew install ollama  # (Mac)
  ```
  or
  ```bash
  curl -fsSL https://ollama.com/install.sh | sh  # (Linux)
  ```

**Issue: Chatbot is not retrieving relevant answers**
- Try rebuilding the FAISS index:
  ```bash
  python vector_db.py
  ```

## 📌 To-Do (Planned Improvements)
- [ ] Expand the knowledge base with more structured data
- [ ] **Improve retrieval accuracy** (chunk size, embeddings)
- [ ] **Add real-time news retrieval** for live updates
- [ ] **Optimize chatbot responses with better prompts**
- [ ] **Deploy to a server for 24/7 availability**

---

 Contributions
If you'd like to contribute or suggest improvements, feel free to open an issue or submit a pull request.

Palestine will be free!🇵🇸

