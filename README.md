# PDF Analysis CLI Tool

## 📖 Overview
This is a modular Python CLI application that extracts text from PDF documents and provides AI-powered analysis using OpenAI's GPT models. The tool supports multiple analysis types including medical reports, invoices, research papers, and general document analysis. It features a clean architecture with separation of concerns across different modules for PDF processing, text cleaning, AI analysis, and task management.

## 🏗️ System Architecture
### Core Components
- **main.py:** Entry point and CLI handler
- **tools.py:** PDF processing and text utilities
- **agents.py:** AI analysis logic
- **task.py:** Analysis task configurations

### PDF Processing Layer
- Uses pdfplumber for robust text extraction
- Includes validation, error handling, and page-wise text cleanup

### AI Analysis Engine
- Uses OpenAI GPT-5 (configurable in agents.py)
- AnalysisAgent manages prompt engineering and response formatting

### Task Management System
- Flexible configuration for different analysis types: general, summary, medical, invoice, research

### Text Processing Pipeline
- Handles Unicode normalization, whitespace cleanup, and formatting before analysis

### CLI Interface
- Built with argparse, supports task type selection, JSON/text output, verbose/debug mode, file output option

### Design Patterns
- **Factory Pattern:** TaskManager creates different analysis tasks
- **Strategy Pattern:** Different task strategies for the same AI agent
- **Error Handling:** Graceful handling of import/runtime/PDF issues

## 📦 Installation
### Prerequisites
- Python 3.8+
- OpenAI API account

### Clone the Repository
```sh
git clone https://github.com/KRSaiVarun/pdf-analysis-tool.git
cd pdf-analysis-tool
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Environment Setup
Create a `.env` file in the project root:
```
OPENAI_API_KEY=your_openai_api_key_here
```
Or export directly:
- Linux/Mac: `export OPENAI_API_KEY=your_openai_api_key_here`
- Windows: `set OPENAI_API_KEY=your_openai_api_key_here`

## 📋 Requirements
- pdfplumber>=0.11.7
- openai>=1.102.0
- python-dotenv>=1.0.0
- fastapi>=0.115.0
- uvicorn>=0.30.0
- crewai>=0.28.8
- crewai-tools>=0.0.15
- langchain-community>=0.0.36

## 📝 Usage
### Basic
```sh
python main.py document.pdf
```
### Advanced
```sh
python main.py document.pdf --task medical
python main.py document.pdf --format json --output analysis.json
python main.py document.pdf --verbose
```
### Available Tasks
- general (default)
- summary
- medical
- invoice
- research

## 📊 Output Examples
### Text
```
============================================================
PDF ANALYSIS REPORT
============================================================
Document Type: Research Paper
SUMMARY:
----------------------------------------
This research paper discusses machine learning applications...
KEY INSIGHTS:
----------------------------------------
1. Innovative approach to data processing
2. Significant performance improvements
3. Practical real-world applications
```
### JSON
```json
{
  "document_type": "Research Paper",
  "summary": "This research paper discusses...",
  "key_insights": ["Insight 1", "Insight 2"],
  "recommendations": ["Recommendation 1", "Recommendation 2"],
  "confidence_score": 0.92
}
```

## 🐞 Bug Fix Report (Blood Test Analyser)
### tools.py
- **Issues:** Missing python-dotenv, crewai-tools, outdated langchain.document_loaders, undefined PDFLoader.
- **Fixes:** Installed dependencies, switched to langchain_community.document_loaders, defined PDFLoader.

### task.py
- **Issues:** Missing crewai.
- **Fixes:** Installed crewai, fixed imports.

### main.py
- **Issues:** Missing fastapi, uvicorn, crewai. Naming inconsistencies (Analyser, Summarise).
- **Fixes:** Installed dependencies, standardized names (Analyzer, Summarize).

### agents.py
- **Issues:** Missing dotenv, crewai.agents, undefined llm.
- **Fixes:** Installed dependencies, initialized llm = LLM(model="gpt-4-turbo").

### ✅ Summary
- All missing deps added to requirements.txt.
- Corrected imports and standardized names.
- Properly initialized undefined variables.
- Project now runs end-to-end without errors.

## 🐛 Troubleshooting
- **ModuleNotFoundError:** run `pip install -r requirements.txt`
- **API Key Error:** check `.env`
- **PDF Extraction Error:** try with simpler files
- **Debug with:**
  ```sh
  python main.py document.pdf --verbose
  ```

## 🤝 Contributing
- Fork repo
- Create branch
- Commit changes
- Push branch
- Open PR

## 📈 Future Enhancements
- Batch PDF analysis
- Cloud storage integration
- Web UI version
- More document types
- Custom templates

## 🎯 Use Cases
- Academic research analysis
- Medical report summarization
- Invoice/financial document analysis
- Legal/technical document review
- Business report insights

