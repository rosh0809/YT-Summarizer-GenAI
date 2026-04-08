# 🤖 YouTube Video Summarizer (GenAI)

An AI-powered tool that transcribes and summarizes YouTube videos using **Google Gemini Pro** and **LangChain**.

## 🚀 Features
* **Full Transcript Extraction:** Uses `youtube-transcript-api` for fast text retrieval.
* **AI Summarization:** Leverages **Google Gemini Pro** for high-quality, concise notes.
* **Topic Segmentation:** Automatically divides content into logical chapters.
* **Interactive UI:** Built with **Streamlit** for a seamless user experience.

## 🛠️ Tech Stack
* **Language:** Python
* **AI Framework:** LangChain, Google Generative AI
* **Frontend:** Streamlit
* **Environment:** Dotenv (Secure API Management)

## 📦 Installation & Setup
1. **Clone the repo:** `git clone https://github.com/YOUR_USERNAME/YT-Summarizer-GenAI.git`
2. **Install dependencies:** `pip install -r requirements.txt`
3. **Set up API Key:** Create a `.env` file and add `GOOGLE_API_KEY=your_key_here`
4. **Run the app:** `streamlit run app.py`
