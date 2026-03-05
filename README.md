# 🧠 Simple AI Assistant Docker App that Remembers

This project is a **production-ready AI chat app** built with Docker Model Runner, Streamlit, and LangChain. It lets you talk to a local LLM running via Docker, or switch seamlessly to a large cloud-based model (like those on OpenRouter), all **while remembering your entire conversation history**. Each model will get the full chat context, even in moments when it wasn't participating in the conversation.

## ⭐ Features

1. Clean Streamlit chat interface with message history 💻
2. Context-passing for memory-aware responses 💡
3. Fully containerized with Docker Compose  🐋


## 📸 Screenshot

<img width="600" alt="screenshot of Simple AI Assistant Chat App" src="https://github.com/user-attachments/assets/789ec4fd-bf47-44e7-ad3a-052dc954582a" />

## ⚡️ Quick Start

### 1️⃣ Prerequisites

- [Docker Desktop](https://www.docker.com) installed and updated to current version.
- Docker Model Runner **enabled** in Docker Desktop (see [official docs](https://dockr.ly/4nT2saM))

### 2️⃣ Clone This Repo

```bash
git clone https://github.com/Ioannis-Mykelos/ai-assistant.git
```

### 3️⃣ Create a `.env` File

Create a file named `.env` in the project root:

```env
REMOTE_BASE_URL=https://openrouter.ai/api/v1
REMOTE_MODEL_NAME=qwen/qwen3-30b-a3b
OPENROUTER_API_KEY=<YOUR_OPENROUTER_API_KEY>
```

- Replace `YOUR_OPENROUTER_API_KEY` with your actual OpenRouter key.
- Choose any local or remote model from:
  - 👉 [Docker Model Catalog](https://dockr.ly/4eTeLQl)
  - 👉 [OpenRouter](https://openrouter.ai)


> [!NOTE]
> This project uses the `uv` Python package manager for dependency management.
> Follow the instructions from the [official documentation](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer) if you want to run the app locally without Docker.

To activate your `.venv` environment (created by `uv sync`):
- Windows use `.venv\Scripts\activate`
- Linux source `.venv/bin/activate`

### 4️⃣ Run the App

```bash
docker compose up
```

Then open your browser to:

http://localhost:8501

✅ Your AI chat app is ready to use!

## 🗂️ Project Structure

```
.
├── .github/workflows/pylint-precommits.yaml   # GitHub actions
├── .env                                       # Environment variables (you create this)
├── .env.example                               # Environment variables as an example
├── .gitignore                                 # Git ignore files
├── .pre-commit-config.yaml                    # Pre commit configuration
├── app.py                                     # Streamlit chat app with LangChain
├── docker-compose.yaml                        # Defines app + model services
├── Dockerfile                                 # Container for running the app
├── LICENSE                                    # MIT License
└── pyproject.toml                             # Project configuration and dependencies (managed by uv)
```


## 🧩 How It Works

- The **llm** service in `docker-compose.yaml` uses Docker Model Runner to serve a local LLM (e.g. Gemma).
- The **ai-app** service is a Streamlit web app that:
  - Stores message history in session state
  - Passes the entire chat context to the LLM for memory-aware responses
  - Lets you switch between local and remote models with a simple checkbox


## 🚀 Customization

- **Change Remote Model**
  Edit `REMOTE_MODEL_NAME`, `REMOTE_BASE_URL`, and your `OPENROUTER_API_KEY`.

- **Dependencies**
  Add any extra Python packages to `pyproject.toml` using `uv`.


## 📚 Helpful Links

- 🐳 [Docker Model Runner Documentation](https://dockr.ly/4nT2saM)
- 🔎 [Find Models in Docker Catalog](https://dockr.ly/4eTeLQl)
- 🌐 [OpenRouter](https://openrouter.ai)
- 🐍 [Streamlit](https://streamlit.io)
- 🦜 [LangChain for Python](https://python.langchain.com)
