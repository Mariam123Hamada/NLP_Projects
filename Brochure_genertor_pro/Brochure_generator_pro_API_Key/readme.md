## 🏢 Company Brochure Generator

This project lets you automatically generate a company brochure using OpenAI models by analyzing the content of a company's website.
It is built with Streamlit for an interactive web interface.

---

## 🚀 Features

- Extracts and cleans text from a company website
- Finds relevant links (About, Careers, etc.)
- Summarizes content using GPT-4o
- Creates a well-formatted brochure
- Download the brochure as a text file
- Simple web interface with Streamlit

---

## 📂 Project Structure
```
project

├── app.py                   # Main  app
├── API_KEY.py               # File storing your OpenAI API key
|__ Web_Scrapping_model.py   #File contain the web scrapping code 
├── requirements.txt         # Python dependencies
└── README.md            
```
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

---

## 🔑 Setup API Key

Create a file called apikey_blog_app.py in your project folder:

openai_api_key = "sk-....your_api_key_here..."

Replace "sk-..." with your actual OpenAI API key.

---

## ▶️ Running the App

Start the Streamlit app:

streamlit run app.py


---

## ✨ How to Use

1. Enter the Company Name and Website URL.
2. Click Generate Brochure.
3. Wait while the app fetches content and generates the brochure.
4. Download the brochure text.

---

## 📝 Requirements

- Python >=3.8
- OpenAI Python SDK
- Streamlit
- BeautifulSoup4
- Requests

(Installed automatically via requirements.txt)


---
