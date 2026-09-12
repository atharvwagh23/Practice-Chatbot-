# 🧭 GenAI Learning Assistant (System Prompt Chatbot)

A **Streamlit + OpenAI** chatbot demonstrating **strict domain-restriction via system prompt engineering**, plus a secondary LLM-based classifier that double-checks each question is actually about Generative AI before answering.

---

## ✨ Features

- 💬 Native Streamlit chat UI with persistent session history
- 🎯 Strictly scoped to **Generative AI / LLM topics only**
- 🧠 Two-layer topic enforcement:
  1. A **system prompt** instructing the main model to refuse off-topic questions
  2. A separate **classifier call** (`is_genai_question`) that pre-screens every question as GenAI-related or not
- 🚫 Canned refusal message for any off-topic question
- 🛡️ Error handling for API/network failures
- 👁️ Collapsible "View System Prompt" panel in the UI for transparency
- 🔑 Uses OpenAI's `gpt-4o-mini` model for both classification and responses

---

## 🛠️ Tech Stack

- [Python 3.12+](https://www.python.org/)
- [Streamlit](https://streamlit.io/) — web UI
- [OpenAI API](https://platform.openai.com/) — LLM responses + classification
- [python-dotenv](https://pypi.org/project/python-dotenv/) — environment variable management

---

## 📂 Project Structure
```
system prompt-chatbot/
├── app.py # Streamlit UI, system prompt, and session logic
├── llm.py # OpenAI client, GenAI classifier, and response logic
├── requirements.txt # Python dependencies
├── images/ # Screenshots/reference images
├── .env # Your API key (not committed to git)
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd "system prompt-chatbot"
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

> Get your API key from [platform.openai.com](https://platform.openai.com/api-keys).

### 5. Run the app

```bash
streamlit run app.py
```

The app opens automatically at `http://localhost:8501`.

---

## 💡 Usage

1. Ask a question in the chat box (e.g. *"What is RAG?"*).
2. The app first classifies whether your question is GenAI-related.
   - ✅ If yes, it's sent to the tutor model, which replies with a definition, explanation, example, and best practices.
   - ❌ If no, you'll get a fixed refusal message — no partial answers or hints are given.
3. Expand **"View System Prompt"** at the top of the app to see the exact rules governing the assistant's behavior.

**Example — will be answered:** *"How does prompt engineering work?"*
**Example — will be refused:** *"What is the capital of India?"*

---

## ⚠️ Notes

- Keep your `.env` file private — never commit your API key to version control.
- Every user question triggers **two** API calls (one classifier call + one response call), so expect slightly higher latency/cost per message than a single-call chatbot.

---

## 📄 License

This project is open source and available for personal or educational use.
