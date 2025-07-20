# 📄 Website Brochure Generator

This is a Streamlit-based web application that generates a **brochure-style summary** of any company website using **Hugging Face's Transformers** summarization model.

## 🚀 Features

- 🌐 Web scraping of company websites
- 🤖 Text summarization using Hugging Face model (`Falconsai/text_summarization`)
- 📘 Clean and styled brochure summary
- ⚡ Lightweight, fast and simple to use interface

---
## 📂 Project Structure
```
project/
├── App.py                   # Main  app   
|__ Web_Scrapper.py          # File contain the web scrapping code  
├── requirements.txt         # Python dependencies  
└── README.md 
```
---
## 🛠️ How It Works

1. Enter the **company name** and its **website URL**.
2. The app scrapes visible text content from the webpage.
3. A Hugging Face summarization model generates a concise brochure summary.
4. You can view raw content and the generated brochure in the interface.

---

## 🛠 Installation
1. Clone  repository

2. Create a virtual environment
   python -m venv .venv

3. Activate the virtual environment

   Windows:
   .venv\Scripts\activate

   macOS/Linux:
   source .venv/bin/activate

4. Install dependencies
   pip install -r requirements.txt

5-streamlit run app.py   

---

## ▶️ Running the App

Start the Streamlit app:

streamlit run app.py

---

## ✨ How to Use

1. Enter the Company Name and Website URL.
2. Click Generate Brochure.
3. Wait while the app fetches content and generates the brochure.

---

## 📝 Requirements

- Python >=3.8
- OpenAI Python SDK
- Streamlit
- BeautifulSoup4
- Requests

(Installed automatically via requirements.txt)

---
