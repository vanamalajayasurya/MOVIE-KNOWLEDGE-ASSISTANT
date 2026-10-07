<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=Movie%20Knowledge%20Assistant&fontSize=44&fontAlignY=36&animation=fadeIn&desc=Local%20RAG%20chatbot%20for%20movie%20questions&descAlignY=58&fontColor=ffffff" alt="Movie Knowledge Assistant banner" width="100%"/>

<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=A78BFA&center=true&vCenter=true&width=700&lines=Ask+anything+about+your+movie+data+%F0%9F%8E%AC;Answers+grounded+in+retrieved+context+%F0%9F%94%8E;No+cloud.+No+API+keys.+Runs+locally+%F0%9F%A6%99;Built+with+Streamlit+%2B+LangChain+%2B+Ollama" alt="Typing animation"/></a>

<br/>

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6446?style=for-the-badge)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)

</div>

---

## 🎞️ Demo

<div align="center">
  <img src="Screenshot 2026-10-07 210332.png" alt="App screenshot: asking who directed The Dark Knight" width="85%"/>
  <p><i>Question: "who directed the dark knight" → <b>The Dark Knight was directed by Christopher Nolan.</b></i></p>
</div>

## ✨ Features

- 🎬 Ask natural-language questions about movies in `movies.txt`
- 🔎 Semantic search with **ChromaDB** + `all-MiniLM-L6-v2` embeddings
- 🦙 Answers generated locally by **Ollama** (`llama3.2:3b`)
- 🛡️ Anti-hallucination prompt: replies _"I don't know"_ if the context lacks the answer
- ⚡ Vector store cached with `@st.cache_resource` so it builds only once per session

## 🧠 How It Works

<div align="center">
  <img src="pipeline.svg" alt="Animated RAG pipeline: Question → Embed → Retrieve → Generate → Answer" width="100%"/>
</div>

```mermaid
flowchart LR
    A[❓ User question] --> B[🧮 Embed query]
    B --> C[(🔎 Chroma vector store)]
    C -->|top-2 chunks| D[📝 Prompt + context]
    D --> E[🦙 Ollama llama3.2:3b]
    E --> F[🤖 Answer in Streamlit]
```

1. `rag.py` loads `movies.txt`, splits it into 500-character chunks (50 overlap) and embeds them into Chroma.
2. On each question, the **2 most similar chunks** are retrieved as context.
3. `app.py` wraps context + question in a strict prompt and sends it to Ollama via `ollama_client.py`.
4. The answer is displayed in the UI.

## 📁 Project Structure

```text
MOVIE KNOWLEDGE ASSISTANT/
├── app.py              # Streamlit UI + prompt building
├── rag.py              # Loading, chunking, embeddings, Chroma, retrieval
├── ollama_client.py    # Calls the local Ollama REST API
├── movies.txt          # Movie knowledge base
├── requirements.txt    # Python dependencies
└── assets/             # README images (demo screenshot, animated pipeline)
```

## 🚀 Getting Started

### 1. Install Ollama and pull the model

```bash
ollama pull llama3.2:3b
ollama serve          # listens on http://localhost:11434
```

### 2. Install dependencies

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

Open the URL shown in the terminal (usually http://localhost:8501).

## 💬 Try These Questions

| Question                       | Expected answer                                      |
| ------------------------------ | ---------------------------------------------------- |
| Who directed Inception?        | Christopher Nolan                                    |
| Who stars in Interstellar?     | Matthew McConaughey, Anne Hathaway, Jessica Chastain |
| What is The Dark Knight about? | Batman faces the Joker in Gotham City                |
| Which movie came out in 2014?  | Interstellar                                         |

## ➕ Adding More Movies

Append entries to `movies.txt` using the same format, then restart the app:

```text
Movie: Title
Genre: ...
Director: ...
Year: ...
Cast: ...
Plot: ...
```

## ⚙️ Configuration

| Setting                | File                              | Default                                  |
| ---------------------- | --------------------------------- | ---------------------------------------- |
| Ollama model           | `ollama_client.py` → `MODEL`      | `llama3.2:3b`                            |
| Ollama URL             | `ollama_client.py` → `OLLAMA_URL` | `http://localhost:11434/api/generate`    |
| Chunk size / overlap   | `rag.py`                          | `500` / `50`                             |
| Retrieved chunks (`k`) | `rag.py` → `retrieve_answer`      | `2`                                      |
| Embedding model        | `rag.py`                          | `sentence-transformers/all-MiniLM-L6-v2` |

## 🛠️ Troubleshooting

- **Connection refused on port 11434** → make sure `ollama serve` is running.
- **Model not found** → run `ollama pull llama3.2:3b`.
- **Slow first start** → the embedding model downloads once from Hugging Face.

---

<div align="center">

Made with ❤️ and 🍿 by **Vanamala Jayasurya**

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%" alt="footer"/>

</div>
