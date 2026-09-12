# 💰 Finance Chatbot

A simple **Streamlit** web app that lets you ask finance-related questions and get clear, beginner-friendly answers powered by the **Groq API**.

The assistant is restricted to the finance domain — it explains concepts, gives formulas with examples, and offers general educational guidance, while steering clear of unrelated topics.

---

## ✨ Features

- 💬 Chat-style interface built with Streamlit
- ⚡ Fast responses via the Groq LLM API
- 🧠 Maintains conversation context (chat history) across a session
- 📜 Sidebar showing a log of all your past questions
- 🎯 Domain-restricted system prompt — stays focused on finance topics only
- 🔧 Configurable model via environment variable

---

## 🛠️ Tech Stack

- [Python 3.12+](https://www.python.org/)
- [Streamlit](https://streamlit.io/) — web UI
- [Groq](https://groq.com/) — LLM inference API
- [python-dotenv](https://pypi.org/project/python-dotenv/) — environment variable management

---

## 📂 Project Structure
```
Finance app (groq_chatbot)/
├── app.py              # Streamlit UI and chat logic
├── llm.py              # System prompt + Groq API call logic
├── config.py           # Loads API key and model from .env
├── requirements.txt    # Python dependencies
├── .env                # Your API key (not committed to git)
└── README.md
```
---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd "Finance app (groq_chatbot)"
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

Create a `.env` file in the project root (or edit the existing one) and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
MODEL=openai/gpt-oss-120b
```

> Get a free API key from [console.groq.com](https://console.groq.com/).
>
> `MODEL` is optional — it defaults to `openai/gpt-oss-120b` if not set.

### 5. Run the app

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## 💡 Usage

1. Type a finance-related question into the input box (e.g. *"What is compound interest?"*).
2. Click **Send**.
3. The assistant replies with a clear explanation, and, where relevant, a formula and example.
4. Your past questions appear in the sidebar for quick reference.

If you ask something unrelated to finance, the assistant will respond with `I DON'T KNOW` by design.

---

## ⚠️ Notes

- This chatbot provides **general, educational information only** — not personalized financial advice. Always consult a qualified financial professional for decisions specific to your situation.
- Keep your `.env` file private — never commit your API key to version control.

---

## 📄 License

This project is open source and available for personal or educational use.
