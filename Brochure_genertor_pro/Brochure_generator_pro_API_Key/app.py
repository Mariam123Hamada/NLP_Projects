import streamlit as st
from Web_Scrabbing_model  import stream_brochure_streamlit
# Streamlit app UI
st.title("📄 Company Brochure Generator")

company_name = st.text_input("Company Name", "")
company_url = st.text_input("Company Website URL", "")
if st.button("Generate Brochure"):
    if not company_name.strip() or not company_url.strip():
        st.warning("Please enter both the company name and the website URL.")
    else:
        st.info("Generating brochure, please wait...")
        brochure_text = stream_brochure_streamlit(company_name, company_url)
        st.success("Brochure generated!")
        st.download_button(
            label="Download Brochure as Text",
            data=brochure_text,
            file_name=f"{company_name}_brochure.txt",
        )
