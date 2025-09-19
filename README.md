# Financial Document Analyzer

A powerful AI-driven financial document analysis system built with CrewAI, FastAPI, and advanced language models. This application provides comprehensive financial insights, investment recommendations, and risk assessments from uploaded PDF financial documents.

## 🎯 Features

- **Intelligent Document Analysis**: Extract and analyze key financial metrics from PDF documents
- **Investment Recommendations**: AI-powered investment advice based on document analysis
- **Risk Assessment**: Comprehensive risk analysis and management strategies
- **Document Verification**: Validate financial document authenticity and completeness
- **RESTful API**: Easy-to-use FastAPI endpoints for document upload and analysis
- **Multi-Agent System**: Specialized AI agents for different aspects of financial analysis

## 🏗️ Project Structure

```
financial-document-analyzer/
├── agents.py              # AI agent definitions and configurations
├── main.py               # FastAPI application and API endpoints
├── task.py               # CrewAI task definitions
├── tools.py              # Custom tools for document processing
├── data/                 # Directory for temporary file storage
├── requirements.txt      # Python dependencies
├── .env                 # Environment variables (API keys)
└── README.md           # Project documentation
```

## 🛠️ Technologies Used

### Core Technologies
- **Python 3.8+** - Primary programming language
- **FastAPI** - Modern web framework for building APIs
- **CrewAI** - Multi-agent AI framework
- **PyPDF2** - PDF document processing
- **Uvicorn** - ASGI server for FastAPI

### AI & Machine Learning
- **OpenRouter/DeepSeek** - Language model for AI agents
- **Langchain** - Framework for AI application development
- **HuggingFace** - ML model integration

### Additional Libraries
- **SerperDev** - Web search capabilities
- **python-dotenv** - Environment variable management
- **python-multipart** - File upload handling
- **logging** - Application logging and monitoring

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8 or higher
- OpenRouter API key
- SerperDev API key (for web search functionality)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/tusharkharat269/financial-document-analyser-system.git
   cd financial-document-analyzer
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Setup**
   Create a `.env` file in the root directory:
   ```env
   OPENROUTER_API_KEY=your_openrouter_api_key_here
   SERPER_API_KEY=your_serper_api_key_here
   ```

5. **Create data directory**
   ```bash
   mkdir data
   ```

### Running the Application

1. **Start the FastAPI server**
   ```bash
   python main.py
   ```
   Or using uvicorn directly:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

2. **Access the application**
   - API: `http://localhost:8000`
   - Interactive API docs: `http://localhost:8000/docs`
   - Alternative docs: `http://localhost:8000/redoc`

## 📊 AI Agents

### 1. Financial Analyst
- **Role**: Senior Financial Analyst
- **Expertise**: 15+ years in financial statement analysis, market research, investment evaluation
- **Capabilities**: CFA-level analysis, data-driven insights, risk assessment
- **Tools**: Financial document reader, web search

### 2. Document Verifier
- **Role**: Financial Document Verification Specialist  
- **Expertise**: GAAP/IFRS standards, audit procedures, document authentication
- **Capabilities**: Document validation, authenticity checks, compliance verification
- **Tools**: Financial document reader

### 3. Investment Advisor
- **Role**: Certified Investment Advisor
- **Expertise**: Portfolio management, investment strategy, fundamental analysis
- **Capabilities**: Risk-adjusted recommendations, asset allocation, fiduciary standards
- **Tools**: Web search for market data

### 4. Risk Assessor
- **Role**: Risk Management Specialist
- **Expertise**: Quantitative modeling, regulatory compliance, institutional risk analysis
- **Capabilities**: Market/credit/operational risk assessment, scenario analysis
- **Tools**: Web search for risk factors

## 📡 API Documentation

### Endpoints

#### Health Check
```http
GET /
```
**Response:**
```json
{
  "message": "Financial Document Analyzer API is running"
}
```

#### Analyze Financial Document
```http
POST /analyze
```

**Parameters:**
- `file` (required): PDF file upload (max 10MB)
- `query` (optional): Analysis query string

**Example Request:**
```bash
curl -X POST "http://localhost:8000/analyze" \
  -F "file=@financial_report.pdf" \
  -F "query=Analyze this company's investment potential"
```

**Response:**
```json
{
  "status": "success",
  "query": "Analyze this company's investment potential",
  "analysis": "Comprehensive financial analysis results...",
  "file_processed": "financial_report.pdf"
}
```

**Error Response:**
```json
{
  "detail": "Error message describing the issue"
}
```

### File Requirements
- **Format**: PDF only
- **Size Limit**: 10MB maximum
- **Content**: Financial documents (reports, statements, analyses)

## 🎯 Usage Examples

### Basic Document Analysis
```python
import requests

# Upload and analyze a financial document
files = {'file': open('quarterly_report.pdf', 'rb')}
data = {'query': 'What are the key investment highlights?'}

response = requests.post('http://localhost:8000/analyze', files=files, data=data)
result = response.json()
```

### Investment Recommendation Query
```python
files = {'file': open('10k_filing.pdf', 'rb')}
data = {'query': 'Provide investment recommendations based on this 10-K filing'}

response = requests.post('http://localhost:8000/analyze', files=files, data=data)
```

### Risk Assessment Query
```python
files = {'file': open('balance_sheet.pdf', 'rb')}
data = {'query': 'Assess the financial risks and provide risk management strategies'}

response = requests.post('http://localhost:8000/analyze', files=files, data=data)
```

## 🛡️ Error Handling

The application includes comprehensive error handling for:
- **File validation**: Format, size, and type checking
- **API errors**: Invalid requests and server errors
- **Document processing**: PDF reading and parsing errors
- **AI processing**: Model and agent execution errors
- **Cleanup**: Automatic temporary file removal

## 🔧 Configuration

### Environment Variables
```env
# Required
OPENROUTER_API_KEY=your_api_key
SERPER_API_KEY=your_serper_key

# Optional
LOG_LEVEL=INFO
MAX_FILE_SIZE=10485760  # 10MB in bytes
DATA_DIR=./data
```

### Agent Configuration
- **Max Iterations**: 2-3 per agent
- **Max RPM**: 10 requests per minute
- **Memory**: Enabled for context retention
- **Verbose**: Detailed logging enabled

## 📞 Support

For issues and questions:
- Create an issue in the repository
- Check the FastAPI docs at `/docs` endpoint
- Review the troubleshooting section above

---

**Built with using CrewAI and FastAPI**