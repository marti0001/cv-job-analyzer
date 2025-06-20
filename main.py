
import gradio as gr
from PyPDF2 import PdfReader
from openai import OpenAI
from dotenv import load_dotenv
import os

from job_matcher import cv_matcher
from resume_analyzer import cv_prompt, extract_text_from_pdf
from job_description_prompt import job_data_prompt

load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')

if "OPENAI_API_KEY" not in os.environ:
    raise ValueError("Brak klucza API w zmiennych środowiskowych")

openai = OpenAI(api_key=openai_api_key)


def summarize(pdf_file, job_description):
    # Process job description
    processed_job = job_data_prompt(job_description)

    # Extract and process CV text
    cv_text = extract_text_from_pdf(pdf_file)
    processed_cv = cv_prompt(cv_text)

    # Get matching results
    result = cv_matcher(processed_cv, processed_job)
    yield from result

view = gr.Interface(
    fn=summarize,
    inputs=[
        gr.File(label="Upload CV (PDF)", file_types=[".pdf"]),
        gr.Textbox(label="Job Description", lines=5, placeholder="Paste job description here...")
    ],
    outputs=gr.Textbox(label="Matching Results"),
    title="CV Matching System",
    description="Upload a CV (PDF) and paste a job description to see matching results",
    flagging_mode="never"

)
if __name__ == "__main__":
    view.launch()
