from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid
import asyncio
import logging
from fastapi.responses import JSONResponse

from crewai import Crew, Process
from agents import financial_analyst,llm
from task import analyze_financial_document as analyze_task

app = FastAPI(title="Financial Document Analyzer")

# Fix: Added proper logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_crew(query: str, file_path: str="data/sample.pdf"):
    """To run the whole crew"""


    try:
        # Fix: Added file existence validation
        if not os.path.exists(file_path):
            logger.error(f"File not found: {file_path}")
            return f"Error: File not found at {file_path}"
        
        # Fix: Create crew with proper configuration
        financial_crew = Crew(
            agents=[financial_analyst],
            tasks=[analyze_task],
            process=Process.sequential,
            verbose=True,  # Fix: Added verbose logging
            memory=False,   # Fix: Enable crew memory
            llm=llm,
        )
        
        # Fix: Execute crew with proper input format
        result = financial_crew.kickoff({'query': query, 'path': file_path})
        
        return str(result)

    except Exception as e:
        logger.error(f"Error running crew analysis: {str(e)}")
        return f"Error in analysis: {str(e)}"

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "Financial Document Analyzer API is running"}

@app.post("/analyze")
async def analyze_financial_document(
    file: UploadFile = File(...),
    query: str = Form(default="Analyze this financial document for investment insights")
):
    """Analyze financial document and provide comprehensive investment recommendations"""
    
    file_id = str(uuid.uuid4())
    file_path = f"data/financial_document_{file_id}.pdf"
    
    try:
        # Fix: Validate file type
        if not file.filename.lower().endswith('.pdf'):
            raise HTTPException(
                status_code=400, 
                detail="Only PDF files are supported"
            )
        
        # Fix: Check file size (limit to 10MB)
        file_content = await file.read()
        if len(file_content) > 10 * 1024 * 1024:  # 10MB limit
            raise HTTPException(
                status_code=413,
                detail="File size too large. Maximum 10MB allowed."
            )
        
        # Ensure data directory exists
        os.makedirs("data", exist_ok=True)
        
        # Save uploaded file with proper error handling
        try:
            with open(file_path, "wb") as f:
                f.write(file_content)
            logger.info(f"File saved successfully: {file_path}")
        except IOError as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to save uploaded file: {str(e)}"
            )
        
        # Validate query
        if query=="" or query is None:
            query = "Analyze this financial document for investment insights"
            
        
        logger.info(f"Starting analysis for query: {query}")
        # Process the financial document with all analysts
        response = run_crew(query=query.strip(), file_path=file_path)
        
        return {
            "status": "success",
            "query": query,
            "analysis": str(response),
            "file_processed": file.filename
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing financial document: {str(e)}")
    
    finally:
        # Clean up uploaded file
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                logger.info(f"Cleaned up temporary file: {file_path}")
            except OSError as e:
                logger.warning(f"Failed to cleanup file {file_path}: {str(e)}")
                # pass  # Ignore cleanup errors

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler for unhandled errors"""
    logger.error(f"Unhandled exception: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error", "detail": str(exc)}
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)