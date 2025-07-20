# app.py

import streamlit as st
from transformers import pipeline
from Brochure_generator_pro_Hugging_face.Web_scrapper import Website

# ✅ يجب أن يكون هذا أول أمر Streamlit
st.set_page_config(page_title="Brochure Generator", layout="wide")

# Load summarization model
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="Falconsai/text_summarization")

summarizer = load_summarizer()

# App layout
st.title("📄 Website Brochure Generator")
st.write("Generate a short brochure-style summary of any company website using a Hugging Face summarization model.")

# Inputs
with st.sidebar:
    company_name = st.text_input("🏢 Company Name")
    url = st.text_input("🔗 Website URL")
    generate = st.button("🚀 Generate Brochure")

# Main content
if generate and company_name and url:
    website = Website(url)
    content = website.get_content()

    st.subheader(f"🌐 Scraped Content from: `{company_name}`")
    with st.expander("📝 View Raw Website Content", expanded=False):
        st.text_area("Content Preview", content[:3000], height=300)

    st.markdown("### 🧠 Generating Brochure...")
    input_text = content[:4000]  # Limit for token size

    with st.spinner("Summarizing content..."):
        summary = summarizer(input_text, max_length=400, min_length=80, do_sample=False)[0]['summary_text']

    st.success("✅ Brochure Generated Successfully!")
    
    st.markdown("### 📘 Brochure Summary")
    st.markdown(
        f"""
        <div style="background-color: #f9f9f9; padding: 20px; border-radius: 10px; border: 1px solid #ddd;">
            <h4 style="color: #007BFF;">{company_name} - Summary</h4>
            <p style="font-size: 16px; line-height: 1.6;">{summary}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
