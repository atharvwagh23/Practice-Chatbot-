# 🤖 Chatbot 101

A minimal **Streamlit + OpenAI** chatbot built as a learning project — demonstrates the basics of building a conversational chat UI with message history using Streamlit's native `st.chat_message` and `st.chat_input` components.

---

## ✨ Features

- 💬 Native Streamlit chat UI (chat bubbles, input box)
- 🧠 Full conversation history passed to the LLM on every turn
- ⏳ Loading spinner while waiting for a response
- 🔑 Uses OpenAI's `gpt-4o-mini` model

---

## 🛠️ Tech Stack

- [Python 3.12+](https://www.python.org/)
- [Streamlit](https://streamlit.io/) — web UI
- [OpenAI API](https://platform.openai.com/) — LLM responses
- [python-dotenv](https://pypi.org/project/python-dotenv/) — environment variable management

---

## 📂 Project Structure
```
chatbot-101/
├── app.py # Streamlit chat UI and session logic
├── llm.py # OpenAI client and response function
├── requirements.txt # Python dependencies
├── .env # Your API key (not committed to git)
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd chatbot-101
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

1. Type a message into the chat box at the bottom of the screen.
2. Press Enter to send.
3. The full conversation (including prior turns) is sent to the LLM, and the response streams into a chat bubble.

---

## ⚠️ Notes

- Keep your `.env` file private — never commit your API key to version control.
- This is a bare-bones example with no system prompt or topic restriction — a good starting point for learning Streamlit + OpenAI basics.

---

## 📄 License

This project is open source and available for personal or educational use.
