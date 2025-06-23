import re
import streamlit as st
from PyPDF2 import PdfReader

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
        return text
st.title("ATS Resume Parser")

uploaded_file = st.file_uploader("Upload a Resume PDF", type="pdf")
if uploaded_file:
    text=extract_text_from_pdf(uploaded_file)
    st.write(text)
