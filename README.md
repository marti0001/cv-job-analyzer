# **CV & Job Offer Analyzer – Multiple LLM Calls with OpenAI & Gradio 🚀**

A project that automates **CV parsing**, **job offer analysis**, and **candidate-job matching** using OpenAI language models and Gradio as an interactive interface. The solution leverages **multiple LLM calls** to extract, evaluate, and compare information from resumes and job descriptions.


---

## 🔎 **Project Description**

The goal of this project is to assist recruiters or candidates by automating the analysis of CVs and job offers. The system uses multiple LLM calls to:
- **Parse PDF CVs** and extract meaningful, structured information.
- **Analyze job descriptions** and identify key requirements and responsibilities.
- **Assess candidate-job fit** by comparing extracted CV data with the job offer.

All these processes are combined into a single **Gradio web interface** for easy interaction. Prompts are dynamically generated and passed to **OpenAI's API** for processing.

---

## 🎯 **Features**

- **PDF Parsing**: Upload a CV in PDF format and automatically extract key sections (experience, skills, education).
- **Job Offer Analysis**: Paste or upload a job description to get a structured analysis of requirements.
- **Candidate Matching**: Compare CV data to the job description and receive a natural language assessment of fit.
- **Multiple LLM Calls**: Each stage (CV parsing, job analysis, matching) uses separate prompts and API calls for precise outputs.
- **Gradio Interface**: Interactive and user-friendly web app for file upload, text input, and displaying results.

---

## 🛠️ **Technologies & Tools**

| Category                | Tools & Libraries                    |
|-------------------------|-------------------------------------|
| **Programming Language** | Python                              |
| **LLM API**              | OpenAI GPT (via `openai` package)   |
| **PDF Parsing**          | `PyMuPDF`, `pdfminer`, or similar   |
| **Web Interface**        | `Gradio`                            |
| **Data Handling**        | `pandas`, `numpy` (optional)        |

---

## 🚀 **How to Run the Project**

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/your-username/cv-job-analyzer.git
cd cv-job-analyzer
```
---
## 🚀 Project Structure  

```bash
📦 Language_Detection
├── 🐍 job_description_prompt.py
├── 🐍 job_matcher.py
├── 🐍 resume_analyzer.py
├── 🐍 main.py
├── 📁 notebooks
│   ├── Resume_Analyzer.ipynb
├── 📄 README.md
├── 📛 .gitignore           # Git exclusion rules
└── 📜 requirements.txt     # requirements
```
---
