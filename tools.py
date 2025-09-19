## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

import PyPDF2  # Fix: Added proper PDF reading library
from pathlib import Path  # Fix: Added for better path handling

from crewai.tools import tool
from crewai_tools.tools import SerperDevTool
import logging

# Fix: Added logging for better error handling
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


## Creating search tool
search_tool = SerperDevTool()

## Creating custom pdf reader tool
class FinancialDocumentTool():
    @staticmethod
    @tool("Financial Document Reader")  # Fix: Added proper tool decorator
    def read_data_tool(path='data/sample.pdf'):
        """Tool to read data from a pdf file from a path

        Args:
            path (str, optional): Path of the pdf file. Defaults to 'data/sample.pdf'.

        Returns:
            str: Full Financial Document file
        """
        
        try:
            # Fix: Check if file exists before processing
            if not os.path.exists(path):
                logger.error(f"File not found: {path}")
                return f"Error: File not found at path {path}"
            
            # Fix: Check if it's actually a file (not directory)
            if not os.path.isfile(path):
                logger.error(f"Path is not a file: {path}")
                return f"Error: Path is not a file: {path}"
            
            # Fix: Check file extension
            if not path.lower().endswith('.pdf'):
                logger.error(f"File is not a PDF: {path}")
                return f"Error: File is not a PDF: {path}"
            
            full_report = ""
            
            # Fix: Use proper PDF reading with PyPDF2 and better error handling
            try:
                with open(path, 'rb') as file:
                    pdf_reader = PyPDF2.PdfReader(file)
                    
                    # Fix: Check if PDF has pages
                    if len(pdf_reader.pages) == 0:
                        return "Error: PDF file contains no pages"
                    
                    for page_num in range(len(pdf_reader.pages)):
                        try:
                            page = pdf_reader.pages[page_num]
                            content = page.extract_text()
                            
                            # Clean and format the financial document data
                            if content.strip():  # Fix: Only process non-empty content
                                # Remove extra whitespaces and format properly
                                while "\n\n" in content:
                                    content = content.replace("\n\n", "\n")
                                
                                full_report += content + "\n"
                                
                        except Exception as page_error:
                            logger.warning(f"Error reading page {page_num}: {str(page_error)}")
                            continue
                            
            except PyPDF2.errors.PdfReadError as pdf_error:
                logger.error(f"PDF read error for {path}: {str(pdf_error)}")
                return f"Error: Invalid or corrupted PDF file - {str(pdf_error)}"
            
            except Exception as file_error:
                logger.error(f"File access error for {path}: {str(file_error)}")
                return f"Error: Cannot access file - {str(file_error)}"
            
            # Fix: Handle empty PDF case
            if not full_report.strip():
                return "Warning: No readable text content found in the PDF file"
                
            return full_report.strip()
            
        except Exception as e:
            logger.error(f"Unexpected error reading PDF file {path}: {str(e)}")
            return f"Error reading PDF file: {str(e)}"



## Creating Investment Analysis Tool
class InvestmentTool:
    @staticmethod
    @tool("Investment Analysis Tool")
    def analyze_investment_tool(financial_document_data):
        """Analyze financial document data for investment insights
        
        Args:
            financial_document_data (str): Financial document content
            
        Returns:
            str: Investment analysis results
        """

        try:
            # Fix: Added basic validation
            if not financial_document_data or not financial_document_data.strip():
                return "Error: No financial data provided for analysis"
            
            # Process and analyze the financial document data
            processed_data = financial_document_data.strip()
            
            # Clean up the data format - Fix: More efficient string cleaning
            processed_data = ' '.join(processed_data.split())  # Remove extra spaces
            
            # Fix: Added basic analysis framework
            analysis_result = {
                "data_length": len(processed_data),
                "word_count": len(processed_data.split()),
                "status": "Analysis complete",
                "note": "Investment analysis functionality to be implemented"
            }
            
            return str(analysis_result)
            
        except Exception as e:
            logger.error(f"Error in investment analysis: {str(e)}")
            return f"Error in investment analysis: {str(e)}"

## Creating Risk Assessment Tool
class RiskTool:
    @staticmethod
    @tool("Risk Assessment Tool")
    def create_risk_assessment_tool(financial_document_data):

        """Create risk assessment based on financial document data
        
        Args:
            financial_document_data (str): Financial document content
            
        Returns:
            str: Risk assessment results
        """

        try:
            # Fix: Added basic validation
            if not financial_document_data or not financial_document_data.strip():
                return "Error: No financial data provided for risk assessment"
            
            # Fix: Added basic risk assessment framework
            risk_assessment = {
                "data_processed": len(financial_document_data),
                "risk_level": "To be determined",
                "assessment_status": "Preliminary analysis complete",
                "note": "Risk assessment functionality to be implemented"
            }
            
            return str(risk_assessment)
            
        except Exception as e:
            logger.error(f"Error in risk assessment: {str(e)}")
            return f"Error in risk assessment: {str(e)}"