# 📑 Pdf-Analysis-Tool: An AI-Powered Framework for Automated Report Analysis and Summarization

## 📖 Abstract

Pdf-Analysis-Tool (ReportSage) is a Python-based project designed to analyze, process, and summarize structured and unstructured reports, with a focus on medical and professional documents such as blood test reports, invoices, research papers, and PDFs.

The framework introduces a modular agent-task-tool architecture, enabling efficient report interpretation, summarization, and insight generation. By separating logic into agents, reusable task definitions, and utility tools, the system ensures scalability, flexibility, and extensibility across domains such as healthcare, finance, and education.

It takes report documents as input, applies task-driven agent pipelines for parsing and interpretation, and generates structured summaries highlighting key insights. With its clean architecture and support for both cloud APIs and local LLMs, ReportSage demonstrates a strong foundation for future intelligent reporting systems.

---

## 🌟 Introduction

Reports play a critical role across industries such as healthcare, finance, education, and business intelligence. Manual report analysis is time-consuming and error-prone.

ReportSage addresses this challenge by providing an AI-powered framework that automatically extracts, interprets, and summarizes reports in PDF format. Built on modular principles, the framework divides logic into agents, tasks, and tools for maintainability and extensibility.

With initial use cases in medical reports and general PDF analysis, the framework can be easily extended to finance, education, and enterprise reporting. The system now supports both cloud-based AI services (DeepSeek) and local LLMs (Ollama) for flexible deployment.

---

## 🏗️ System Architecture
### Core Components
- **main.py** – Entry point and CLI handler, orchestrates workflows.
- **agents.py** – AI logic (text extraction, summarization, interpretation).
- **task.py** – Defines analysis task configurations and management.
- **tools.py** – Utilities for PDF parsing, text cleaning, and helper functions.
- **data/** – Sample reports (e.g., blood_test_report.pdf, sample.pdf).
- **pyproject.toml** / **requirements.txt** – Dependencies and project configuration.

### Design Patterns
- **Factory Pattern** – TaskManager creates analysis tasks.
- **Strategy Pattern** – Different strategies for agents per task type.
- **Error Handling** – Robust handling of PDF parsing and runtime issues.
- **Fallback Mechanism** – Graceful degradation when AI services are unavailable.

### Processing Layers
- **PDF Processing** – Powered by pdfplumber with error handling and page-wise cleanup.
- **AI Analysis Engine** – Supports both cloud APIs (DeepSeek) and local LLMs (Ollama).
- **Task Management** – Supports different analysis pipelines (medical, invoice, research, etc.).
- **Text Pipeline** – Normalization, whitespace cleanup, and formatting.
- **CLI Interface** – Built with argparse, supports JSON/text outputs, verbose mode, and task selection.

---

## 📦 Installation & Requirements

### Option 1: Local LLM (Recommended - Free)
```bash
# Install Ollama for local AI processing
# Download from: https://ollama.ai/

# Then pull a model:
ollama pull llama2

# Install Python dependencies
pip install -r requirements.txt
Option 2: Cloud API (DeepSeek)
bash
# Install Python dependencies
pip install -r requirements.txt

# Set API key
export DEEPSEEK_API_KEY=your_deepseek_api_key_here
# or on Windows:
set DEEPSEEK_API_KEY=your_deepseek_api_key_here
Prerequisites
Python 3.8+

For local AI: Ollama installed and running

For cloud AI: DeepSeek API account & key

Setup
bash
git clone https://github.com/KRSaiVarun/pdf-analysis-tool
cd pdf-analysis-tool
pip install -r requirements.txt
📋 Requirements
pdfplumber>=0.11.7

requests>=2.31.0

python-dotenv>=1.0.0

📝 Usage
Basic Usage
bash
# Analyze with default settings
python main.py document.pdf

# Use local Ollama (default)
python main.py document.pdf --task medical

# Force cloud API (if available)
python main.py document.pdf --use-cloud
Advanced Options
bash
# Specific task analysis
python main.py document.pdf --task medical
python main.py document.pdf --task invoice
python main.py document.pdf --task research

# Output formats
python main.py document.pdf --format json --output analysis.json
python main.py document.pdf --format text

# Verbose mode for debugging
python main.py document.pdf --verbose

# Force cloud API usage
python main.py document.pdf --use-cloud
Available Tasks
general (default) - General document analysis

summary - Focused summarization

medical - Medical report analysis

invoice - Financial document analysis

research - Academic paper analysis

📊  Output
Medical Report Analysis Output

============================================================
PDF ANALYSIS REPORT (MEDICAL ANALYSIS)
============================================================
Document Type: Medical Laboratory Report - Comprehensive Health Checkup
SUMMARY:
----------------------------------------
Comprehensive medical laboratory report for a 30-year-old male patient from Dr. Lal PathLab. 
The report includes complete blood count, liver & kidney function tests, lipid profile, 
diabetes screening, thyroid profile, and vitamin levels (B12 and D).

KEY INSIGHTS:
----------------------------------------
1. **Complete Blood Count**: All parameters within normal ranges 
   - Hemoglobin: 15.00 g/dL (Normal: 13.00-17.00)
   - White Blood Cells: 8.00 thou/mm³ (Normal: 4.00-10.00)
   - Platelets: 200 thou/mm³ (Normal: 150-410)

2. **Liver Function**: Excellent liver health
   - ALT: 21.0 U/L (Normal: 10.00-49.00)
   - AST: 11.0 U/L (Normal: 15.00-40.00) - slightly below normal
   - Bilirubin Total: 0.20 mg/dL (Slightly below normal: 0.30-1.20)

3. **Kidney Function**: Optimal performance
   - Creatinine: 0.90 mg/dL (Normal: 0.70-1.30)
   - eGFR: 118 mL/min/1.73m² (Excellent: >59)
   - GFR Category: G1 (Normal kidney function)

4. **Lipid Profile**: Generally good with minor elevation
   - Total Cholesterol: 105.00 mg/dL (Excellent: <200)
   - Triglycerides: 130.00 mg/dL (Slightly elevated: <150)
   - HDL: 46.00 mg/dL (Good: >40)
   - LDL: 33.00 mg/dL (Excellent: <100)

5. **Diabetes Screening**: Normal results
   - HbA1c: 5.3% (Non-diabetic range: 4.0-5.6%)
   - Fasting Glucose: 90.00 mg/dL (Normal: 70-100)

6. **Thyroid Function**: Requires clinical correlation
   - TSH: 4.00 μIU/mL (Normal: 0.550-4.780)
   - T3 Total: 2.00 ng/mL (Elevated: Normal 0.60-1.81)
   - T4 Total: 4.00 μg/dL (Low: Normal 5.01-12.45)

7. **Vitamin Levels**: 
   - Vitamin B12: 280.00 pg/mL (Normal: 211-911)
   - Vitamin D: 85.00 nmol/L (Sufficient: 75-250)

CRITICAL FINDINGS:
----------------------------------------
1. **Thyroid Hormone Imbalance**: T3 elevated and T4 low - requires endocrinology consultation
2. **Slightly Low Bilirubin**: May indicate mild liver function variation
3. **Borderline Triglycerides**: Slightly above optimal range

RECOMMENDATIONS:
----------------------------------------
1. **Immediate Consultation**: Endocrinologist review for thyroid hormone imbalance
2. **Dietary Modifications**: Reduce saturated fats to address elevated triglycerides
3. **Liver Function Monitoring**: Repeat liver enzymes in 3 months
4. **Thyroid Follow-up**: Complete thyroid panel with Free T3, Free T4, and antibodies
5. **Lifestyle Maintenance**: Continue current healthy practices showing good metabolic markers
6. **Vitamin Maintenance**: Current vitamin levels are adequate - maintain balanced nutrition

PATIENT DETAILS:
----------------------------------------
- Name: DUMMY (Anonymized)
- Age: 30 Years | Gender: Male
- Lab Number: 439854467
- Collection Date: May 14, 2023
- Reporting Date: May 16, 2023
- Laboratory: Dr. Lal PathLab, Rohini, Delhi

DISCLAIMER:
----------------------------------------
This analysis is for informational purposes only and should not replace professional 
medical advice, diagnosis, or treatment. All findings must be clinically correlated 
by a qualified healthcare provider.

Model: Medical Analysis Expert
Text Processed: ~15,000 characters
Report Pages: 10
🚀 Key Features
Dual AI Backend: Support for both local LLMs (Ollama) and cloud APIs (DeepSeek)

Modular Architecture: Agent-task-tool design for easy extensibility

Automated Processing: PDF extraction and AI analysis pipeline

Domain-Specific Analysis: Specialized tasks for medical, financial, and academic documents

Graceful Fallback: Continues operation even when AI services are unavailable

Multiple Output Formats: JSON and human-readable text outputs

🎯 Applications
Healthcare: Medical test report extraction & summarization

Finance: Invoice, audit, and statement analysis

Education: Student performance report insights

Research: Academic paper summarization and analysis

Business Intelligence: Structured/semi-structured report processing

📈 Future Enhancements
OCR integration for scanned reports

Natural language, user-friendly summaries

Web-based user interface for report upload/analysis

Support for more formats (CSV, DOCX, JSON)

Batch processing & cloud storage integration

Additional local LLM model support

🐞 Troubleshooting
Common Issues & Solutions
ModuleNotFoundError: Run pip install -r requirements.txt

Ollama Connection Error: Ensure Ollama is running: ollama serve

API Key Error: Check environment variable setup

PDF Extraction Error: Try simpler PDFs or check file permissions

Debug Mode
bash
python main.py document.pdf --verbose
Ollama Setup Help
bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Start Ollama service
ollama serve

# Pull a model (in separate terminal)
ollama pull llama2
📄 License
MIT License – see LICENSE

🤝 Contributing
Fork the repository

Create a feature branch: git checkout -b feature/amazing-feature

Commit changes: git commit -m 'Add amazing feature'

Push to branch: git push origin feature/amazing-feature

Open a Pull Request

🔄 Recent Updates
Added Local LLM Support: Integrated Ollama for free, offline AI processing

Dual AI Backend: Support for both cloud APIs and local models

Improved Error Handling: Graceful fallback when AI services are unavailable

Enhanced Medical Analysis: Better formatting for medical report output

Simplified Setup: Reduced dependency requirements

🆕 Quick Start
bash
# 1. Install Ollama (https://ollama.ai/)
# 2. Pull a model
ollama pull llama2

# 3. Install Python dependencies
pip install -r requirements.txt

# 4. Analyze your first document!
python main.py sample.pdf --task medical

# To Run with specific medical report
python main.py "blood_test_report.pdf" --task medical --format text --verbose

# In PowerShell, set API key (if using cloud):
$env:DEEPSEEK_API_KEY="sk-6a18d4f312d14e0da3f70a1d81797335"
