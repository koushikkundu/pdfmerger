import streamlit as st
from pypdf import PdfWriter

st.title("PDF Merger")
st.write("This is a simple PDF merger that merges multiple PDF files into one.")
pdfs = st.file_uploader("Choose PDF files", type="pdf", accept_multiple_files=True)

def merge():
    merger = PdfWriter()
    for pdf in pdfs:
        merger.append(pdf)
        merger.write("merged.pdf")
    with open("merged.pdf", "rb") as file:
        btn = st.download_button(
            label="Download",
            data=file,
            file_name="merged.pdf",
            mime="application/pdf"
        )
    merger.close()

if st.button("Merge"):
    merge()


