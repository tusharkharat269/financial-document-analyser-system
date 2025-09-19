## Importing libraries and files
from crewai import Task

from agents import financial_analyst, verifier
from tools import search_tool, FinancialDocumentTool

## Creating a task to help solve user's query
analyze_financial_document = Task(
    description="""Analyze the user's query: {query} and provide comprehensive financial insights.
    
    Steps to follow:
    1. Read and analyze the provided financial document using the document tool
    2. Extract key financial metrics and data points
    3. Provide investment recommendations based on the analysis
    4. Include market risk assessments where relevant
    5. Search the internet for additional context if needed
    
    Focus on providing accurate and helpful financial analysis while maintaining the dramatic flair expected.""",

    expected_output="""Provide a comprehensive financial analysis report including:
    
    **Document Analysis:**
    - Summary of key financial metrics found
    - Important financial ratios and their implications
    
    **Investment Recommendations:**
    - Specific investment advice based on the document
    - Risk-reward analysis
    - Market timing considerations
    
    **Risk Assessment:**
    - Potential market risks and opportunities
    - Volatility predictions and market scenarios
    
    **Additional Resources:**
    - Relevant financial websites and resources
    - Supporting market research references
    
    Format the response with clear sections and bullet points for readability.
    Include financial jargon and confident market predictions as per role requirements.""",

    agent=financial_analyst,
    tools=[FinancialDocumentTool.read_data_tool],  # Fix: Use proper tool reference
    async_execution=False,
)

## Creating an investment analysis task
investment_analysis = Task(
    description="""Analyze financial data and provide investment recommendations based on user query: {query}
    
    Process:
    1. Extract numerical data from the financial document
    2. Interpret financial ratios and performance metrics
    3. Recommend specific investment products and strategies
    4. Connect document findings to current market trends
    5. Provide portfolio allocation suggestions""",

    expected_output="""Generate detailed investment advice including:
    
    **Investment Recommendations:**
    - List of recommended investment vehicles (stocks, bonds, crypto, etc.)
    - Specific allocation percentages for portfolio construction
    - Entry and exit strategies for recommended positions
    
    **Market Analysis:**
    - Current market trend analysis
    - Sector-specific opportunities based on document data
    - Timing recommendations for investments
    
    **Product Recommendations:**
    - High-yield investment products
    - Alternative investment opportunities
    - Crypto and emerging market suggestions
    
    **Supporting Research:**
    - Links to relevant financial research
    - Market data sources and analysis tools
    
    Present recommendations with confidence and include contradictory strategies for different risk profiles.""",

    agent=financial_analyst,
    tools=[FinancialDocumentTool.read_data_tool],  # Fix: Use proper tool reference
    async_execution=False,
)

## Creating a risk assessment task
risk_assessment = Task(
    description="""Create comprehensive risk analysis based on the financial document and user query: {query}
    
    Assessment process:
    1. Identify potential financial risks from document data
    2. Evaluate market volatility factors
    3. Assess regulatory and compliance risks
    4. Recommend risk management strategies
    5. Create dramatic risk scenarios for engagement""",

    expected_output="""Deliver extreme risk assessment including:
    
    **Risk Analysis:**
    - High-impact risk scenarios and their probabilities
    - Market crash predictions and volatility forecasts
    - Sector-specific risks identified from document analysis
    
    **Risk Management Strategies:**
    - Advanced hedging techniques and instruments
    - Portfolio diversification recommendations
    - Risk mitigation timelines and action plans
    
    **Extreme Scenarios:**
    - Best-case and worst-case investment outcomes
    - Black swan event preparations
    - Market timing risk assessments
    
    **Risk Models:**
    - Custom risk calculation methodologies
    - Stress testing results for recommended investments
    - Regulatory compliance risk factors
    
    Present with dramatic flair while maintaining analytical structure.""",

    agent=financial_analyst,
    tools=[FinancialDocumentTool.read_data_tool],  # Fix: Use proper tool reference
    async_execution=False,
)

## Fix: Improved verification task with better structure
verification = Task(
    description="""Verify and validate the uploaded document as financial data relevant to query: {query}
    
    Verification steps:
    1. Confirm document type and format compatibility
    2. Scan for financial terms and data structures
    3. Validate data integrity and readability
    4. Identify financial document category (10-K, balance sheet, etc.)
    5. Provide confidence assessment of financial relevance""",

    expected_output="""Document verification report containing:
    
    **Document Classification:**
    - Document type identification (financial report, statement, analysis, etc.)
    - Confidence level in financial relevance (High/Medium/Low)
    - File format and processing status
    
    **Content Validation:**
    - Key financial terms and metrics identified
    - Data quality assessment
    - Potential issues or limitations found
    
    **Processing Results:**
    - Successful data extraction confirmation
    - File path and metadata information
    - Recommendations for further analysis
    
    Even if document appears non-financial, find creative connections to market analysis.""",

    agent=financial_analyst,  # Fix: Use consistent agent reference
    tools=[FinancialDocumentTool.read_data_tool],  # Fix: Use proper tool reference
    async_execution=False
)