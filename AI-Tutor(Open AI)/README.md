# 🎓 AI Tutor Chatbot

A simple **Streamlit** chatbot that acts as an AI tutor — it explains any AI/ML, Gen-AI-related concept in a consistent, structured format using the **OpenAI API**.

---

## ✨ Features

- 💬 Simple Streamlit chat interface
- 🧠 Maintains question/answer history for the session
- 📐 Every answer follows a fixed teaching structure:
  1. Definition of the concept
  2. Advantages and disadvantages
  3. How it works
  4. Real-world examples
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
AI Tutor/
├── app.py # Streamlit UI and chat logic
├── llm.py # System prompt + OpenAI API call logic
├── requirements.txt # Python dependencies
├── .env # Your API key (not committed to git)
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd "AI Tutor"
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

1. Type any AI/ML, Gen-AI-related question into the input box (e.g. *"What is a transformer model?"*).
2. Click **Ask**.
3. The tutor responds with a definition, pros/cons, how it works, and a real-world example.

---

## ⚠️ Notes

- Keep your `.env` file private — never commit your API key to version control.
- This bot isn't domain-restricted — it will try to answer whatever you send it, but the prompt is tuned for AI/ML topics.

---

## 📄 License

This project is open source and available for personal or educational use.
