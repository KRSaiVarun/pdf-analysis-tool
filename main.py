#!/usr/bin/env python3
"""
PDF Analysis CLI Tool
Main entry point for the PDF text extraction and AI analysis tool.
"""

import argparse
import json
import sys
from pathlib import Path

from tools import PDFProcessor, TextCleaner
from agents import AnalysisAgent
from task import TaskManager


def main():
    parser = argparse.ArgumentParser(
        description="Extract text from PDFs and provide AI-powered analysis"
    )
    parser.add_argument(
        "pdf_path",
        type=str,
        help="Path to the PDF file to analyze"
    )
    parser.add_argument(
        "--task",
        type=str,
        choices=["summary", "medical", "invoice", "research", "general"],
        default="general",
        help="Type of analysis to perform (default: general)"
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Output file path for results (optional, prints to stdout if not specified)"
    )
    parser.add_argument(
        "--format",
        type=str,
        choices=["json", "text"],
        default="text",
        help="Output format (default: text)"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output"
    )

    args = parser.parse_args()

    # Validate PDF file exists
    pdf_path = Path(args.pdf_path)
    if not pdf_path.exists():
        print(f"Error: PDF file '{pdf_path}' not found.")
        sys.exit(1)

    if not pdf_path.suffix.lower() == '.pdf':
        print(f"Error: File '{pdf_path}' is not a PDF.")
        sys.exit(1)

    try:
        # Initialize components
        pdf_processor = PDFProcessor()
        text_cleaner = TextCleaner()
        analysis_agent = AnalysisAgent()
        task_manager = TaskManager()

        if args.verbose:
            print(f"Processing PDF: {pdf_path}")
            print(f"Analysis task: {args.task}")

        # Extract text from PDF
        raw_text = pdf_processor.extract_text(pdf_path)
        if not raw_text.strip():
            print("Error: No text could be extracted from the PDF.")
            sys.exit(1)

        if args.verbose:
            print(f"Extracted {len(raw_text)} characters of text")

        # Clean and preprocess text
        cleaned_text = text_cleaner.clean_text(raw_text)
        
        # Get task configuration
        task_config = task_manager.get_task_config(args.task)
        
        # Perform AI analysis
        if args.verbose:
            print("Performing AI analysis...")
            
        analysis_result = analysis_agent.analyze_document(
            text=cleaned_text,
            task_type=args.task,
            task_config=task_config
        )

        # Format output
        if args.format == "json":
            output = json.dumps(analysis_result, indent=2, ensure_ascii=False)
        else:
            output = format_text_output(analysis_result)

        # Write or print output
        if args.output:
            output_path = Path(args.output)
            output_path.write_text(output, encoding='utf-8')
            print(f"Analysis saved to: {output_path}")
        else:
            print(output)

    except Exception as e:
        print(f"Error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


def format_text_output(analysis_result):
    """Format analysis result as human-readable text."""
    # Special formatting for medical reports
    if analysis_result.get("analysis_type") == "medical":
        return format_medical_output(analysis_result)

    # Default formatting for other report types
    output_lines = []
    output_lines.append("=" * 60)
    output_lines.append("PDF ANALYSIS REPORT")
    output_lines.append("=" * 60)
    output_lines.append("")
    
    if "document_type" in analysis_result:
        output_lines.append(f"Document Type: {analysis_result['document_type']}")
        output_lines.append("")
    
    if "summary" in analysis_result:
        output_lines.append("SUMMARY:")
        output_lines.append("-" * 40)
        output_lines.append(analysis_result["summary"])
        output_lines.append("")
    
    if "key_insights" in analysis_result:
        output_lines.append("KEY INSIGHTS:")
        output_lines.append("-" * 40)
        for i, insight in enumerate(analysis_result["key_insights"], 1):
            output_lines.append(f"{i}. {insight}")
        output_lines.append("")
    
    return "\n".join(output_lines)


def format_medical_output(analysis_result):
    """Format medical analysis into the detailed report style."""
    lines = []
    lines.append("=" * 60)
    lines.append("PDF ANALYSIS REPORT (MEDICAL ANALYSIS)")
    lines.append("=" * 60)
    
    # Document Type
    lines.append("Document Type: Medical Laboratory Report - Comprehensive Health Checkup")
    lines.append("")
    
    # Summary Section
    if "summary" in analysis_result:
        lines.append("SUMMARY:")
        lines.append("-" * 40)
        lines.append(analysis_result["summary"])
        lines.append("")
    
    # Key Insights/Interpretations
    if "interpretations" in analysis_result and analysis_result["interpretations"]:
        lines.append("KEY INSIGHTS:")
        lines.append("-" * 40)
        for i, insight in enumerate(analysis_result["interpretations"], 1):
            lines.append(f"{i}. {insight}")
        lines.append("")
    
    # Critical Findings
    if "critical_findings" in analysis_result and analysis_result["critical_findings"]:
        lines.append("CRITICAL FINDINGS:")
        lines.append("-" * 40)
        for i, finding in enumerate(analysis_result["critical_findings"], 1):
            lines.append(f"{i}. {finding}")
        lines.append("")
    
    # Recommendations
    if "recommendations" in analysis_result and analysis_result["recommendations"]:
        lines.append("RECOMMENDATIONS:")
        lines.append("-" * 40)
        for i, recommendation in enumerate(analysis_result["recommendations"], 1):
            lines.append(f"{i}. {recommendation}")
        lines.append("")
    
    # Patient Details
    if "patient_details" in analysis_result and analysis_result["patient_details"]:
        lines.append("PATIENT DETAILS:")
        lines.append("-" * 40)
        for key, value in analysis_result["patient_details"].items():
            lines.append(f"- {key.replace('_', ' ').title()}: {value}")
        lines.append("")
    
    # Disclaimer
    if "disclaimer" in analysis_result:
        lines.append("DISCLAIMER:")
        lines.append("-" * 40)
        lines.append(analysis_result["disclaimer"])
        lines.append("")
    
    return "\n".join(lines)


if __name__ == "__main__":
    main()
