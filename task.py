"""
Task Definitions
Configuration and templates for different types of document analysis tasks.
"""

from typing import Dict, List


class TaskManager:
    """Manages different analysis tasks and their configurations."""
    
    def __init__(self):
        self.tasks = {
            "general": self._get_general_task(),
            "summary": self._get_summary_task(),
            "medical": self._get_medical_task(),
            "invoice": self._get_invoice_task(),
            "research": self._get_research_task()
        }
    
    def get_task_config(self, task_name: str) -> Dict:
        """
        Get configuration for a specific task.
        
        Args:
            task_name: Name of the task
            
        Returns:
            Task configuration dictionary
            
        Raises:
            ValueError: If task name is not recognized
        """
        if task_name not in self.tasks:
            raise ValueError(f"Unknown task '{task_name}'. Available tasks: {list(self.tasks.keys())}")
        
        return self.tasks[task_name]
    
    def get_available_tasks(self) -> List[str]:
        """
        Get list of available task names.
        
        Returns:
            List of task names
        """
        return list(self.tasks.keys())
    
    def _get_general_task(self) -> Dict:
        """General purpose document analysis task."""
        return {
            "name": "general",
            "description": "General purpose document analysis and summarization",
            "system_prompt": (
                "You are an expert document analyst. Your task is to analyze documents "
                "and provide comprehensive insights, summaries, and structured information. "
                "Always respond with valid JSON format."
            ),
            "user_prompt": (
                "Analyze the following document and provide a comprehensive analysis. "
                "Respond with a JSON object containing:\n"
                "- 'document_type': The type of document (e.g., report, letter, manual)\n"
                "- 'summary': A concise summary of the main content (2-3 sentences)\n"
                "- 'key_insights': Array of 3-5 most important insights or findings\n"
                "- 'main_topics': Array of primary topics discussed\n"
                "- 'structured_data': Object with any structured information found\n"
                "- 'recommendations': Array of actionable recommendations (if applicable)\n"
                "- 'confidence_score': Your confidence in the analysis (0-1)\n\n"
                "Document text:\n{text}"
            )
        }
    
    def _get_summary_task(self) -> Dict:
        """Document summarization focused task."""
        return {
            "name": "summary",
            "description": "Focused document summarization with key points extraction",
            "system_prompt": (
                "You are an expert at creating concise, accurate summaries of documents. "
                "Focus on extracting the most important information and presenting it clearly. "
                "Always respond with valid JSON format."
            ),
            "user_prompt": (
                "Create a comprehensive summary of the following document. "
                "Respond with a JSON object containing:\n"
                "- 'executive_summary': A brief 1-2 sentence overview\n"
                "- 'detailed_summary': A more comprehensive 3-4 paragraph summary\n"
                "- 'key_points': Array of the most important points (5-7 items)\n"
                "- 'supporting_details': Object with supporting information for key points\n"
                "- 'conclusion': Main conclusion or outcome from the document\n"
                "- 'word_count_original': Estimated word count of original\n"
                "- 'compression_ratio': Ratio of summary to original length\n\n"
                "Document text:\n{text}"
            )
        }
    
    def _get_medical_task(self) -> Dict:
        """Medical document analysis task with enhanced prompt."""
        return {
            "name": "medical",
            "description": "Specialized analysis for medical reports and health documents",
            "system_prompt": (
                "You are a senior medical analyst with expertise in clinical pathology. "
                "Analyze medical laboratory reports with extreme attention to detail. "
                "Extract ALL patient information, test results, reference ranges, and flags. "
                "Provide comprehensive clinical insights and specific recommendations. "
                "Always respond with valid JSON format containing detailed structured data. "
                "IMPORTANT: Always include a top-level field 'analysis_type' with value 'medical'."
            ),
            "user_prompt": (
                "Comprehensively analyze this medical laboratory report. "
                "Respond with a detailed JSON object containing:\n"
                "- 'analysis_type': always set this to 'medical'\n"
                "- 'patient_details': dict with all available patient demographics\n"
                "- 'test_panels': array of all test categories performed\n"
                "- 'key_results': detailed dict of test categories with actual values\n"
                "- 'critical_findings': array of any abnormal or concerning results\n"
                "- 'interpretations': array of clinical insights for each test category\n"
                "- 'recommendations': array of specific medical recommendations\n"
                "- 'summary': comprehensive summary of overall health status\n"
                "- 'disclaimer': appropriate medical disclaimer\n\n"
                "Focus on accuracy and clinical relevance. Include actual values and reference ranges.\n\n"
                "Medical report text:\n{text}"
            )
        }
    
    def _get_invoice_task(self) -> Dict:
        """Invoice and financial document analysis task."""
        return {
            "name": "invoice",
            "description": "Specialized analysis for invoices, bills, and financial documents",
            "system_prompt": (
                "You are a financial document analysis expert. Extract and organize "
                "information from invoices, bills, receipts, and financial statements. "
                "Focus on accuracy and completeness of financial data extraction. "
                "Always respond with valid JSON format."
            ),
            "user_prompt": (
                "Analyze this financial document and extract all relevant information. "
                "Respond with a JSON object containing:\n"
                "- 'document_type': Type of financial document (invoice, receipt, bill, etc.)\n"
                "- 'vendor_information': Company/vendor details (name, address, contact)\n"
                "- 'customer_information': Customer/client details\n"
                "- 'document_numbers': Invoice number, PO number, reference numbers\n"
                "- 'dates': Invoice date, due date, service dates\n"
                "- 'line_items': Detailed breakdown of items/services with quantities and prices\n"
                "- 'financial_summary': Subtotal, tax, discounts, total amount\n"
                "- 'payment_terms': Payment terms and conditions\n"
                "- 'currency': Currency used in the document\n"
                "- 'tax_information': Tax rates, tax amounts, tax IDs\n"
                "- 'potential_issues': Any discrepancies or issues found\n"
                "- 'verification_status': Assessment of document completeness\n\n"
                "Financial document text:\n{text}"
            )
        }
    
    def _get_research_task(self) -> Dict:
        """Research paper and academic document analysis task."""
        return {
            "name": "research",
            "description": "Specialized analysis for research papers and academic documents",
            "system_prompt": (
                "You are an academic research analysis expert. Analyze research papers, "
                "academic articles, and scholarly documents to extract key research "
                "components and evaluate research quality. Always respond with valid JSON format."
            ),
            "user_prompt": (
                "Analyze this research document and extract key academic information. "
                "Respond with a JSON object containing:\n"
                "- 'document_type': Type of academic document (research paper, thesis, etc.)\n"
                "- 'title': Document title\n"
                "- 'authors': List of authors and affiliations\n"
                "- 'abstract': Abstract or summary section\n"
                "- 'research_field': Field of study or discipline\n"
                "- 'research_question': Main research question or hypothesis\n"
                "- 'methodology': Research methodology and approach\n"
                "- 'key_findings': Main research findings and results\n"
                "- 'conclusions': Primary conclusions drawn\n"
                "- 'contributions': Novel contributions to the field\n"
                "- 'limitations': Study limitations mentioned\n"
                "- 'future_work': Suggested future research directions\n"
                "- 'keywords': Important keywords and terms\n"
                "- 'research_quality': Assessment of research rigor and quality\n"
                "- 'practical_applications': Potential real-world applications\n"
                "- 'citation_potential': Assessment of citation worthiness\n\n"
                "Research document text:\n{text}"
            )
        }


class CustomTaskBuilder:
    """Helper class for building custom analysis tasks."""
    
    @staticmethod
    def create_custom_task(
        name: str,
        description: str,
        system_prompt: str,
        analysis_fields: List[str],
        additional_instructions: str = ""
    ) -> Dict:
        fields_prompt = "\n".join([f"- '{field}': {field.replace('_', ' ').title()}" 
                                  for field in analysis_fields])
        
        user_prompt = (
            f"Analyze the following document according to the specified requirements. "
            f"Respond with a JSON object containing:\n"
            f"{fields_prompt}\n"
        )
        
        if additional_instructions:
            user_prompt += f"\nAdditional instructions: {additional_instructions}\n"
        
        user_prompt += "\nDocument text:\n{text}"
        
        return {
            "name": name,
            "description": description,
            "system_prompt": system_prompt,
            "user_prompt": user_prompt,
            "custom": True
        }
    
    @staticmethod
    def create_domain_specific_task(domain: str, specific_requirements: List[str]) -> Dict:
        system_prompt = (
            f"You are a {domain} document analysis expert. Analyze documents "
            f"within the {domain} domain and extract relevant domain-specific "
            f"information. Always respond with valid JSON format."
        )
        
        requirements_prompt = "\n".join([f"- {req}" for req in specific_requirements])
        
        user_prompt = (
            f"Analyze this {domain} document and extract relevant information. "
            f"Focus on the following domain-specific requirements:\n"
            f"{requirements_prompt}\n\n"
            f"Respond with a JSON object containing appropriate fields for these requirements.\n\n"
            f"Document text:\n{{text}}"
        )
        
        return {
            "name": f"{domain}_analysis",
            "description": f"Specialized analysis for {domain} documents",
            "system_prompt": system_prompt,
            "user_prompt": user_prompt,
            "domain": domain,
            "custom": True
        }
