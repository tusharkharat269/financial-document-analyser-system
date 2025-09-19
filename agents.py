## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()


from crewai import Agent,LLM

from tools import search_tool, FinancialDocumentTool
from langchain_huggingface import HuggingFaceEndpoint

import logging

# Fix: Added logging for better error handling
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

### Loading LLM
# Fix: Properly initialize LLM instead of circular reference
try:
    logger.info("Initializing OpenAI LLM...")
    llm = LLM(
        model="openrouter/deepseek/deepseek-r1",
        api_key="or_key"
    )

    logger.info("LLM initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize LLM: {str(e)}")
    raise

# Creating an Experienced Financial Analyst agent
financial_analyst=Agent(
    role="Senior Financial Analyst",
    goal="Provide comprehensive, accurate financial analysis based on the user query: {query}",
    verbose=True,
    memory=True,
    backstory=(
        "You are a highly experienced Senior Financial Analyst with over 15 years of expertise in "
        "financial statement analysis, market research, and investment evaluation. You hold a CFA designation "
        "and have worked with Fortune 500 companies, providing detailed financial insights and recommendations. "
        "Your analytical approach is methodical, data-driven, and conservative. You always base your analysis "
        "on factual information from financial documents and market data. You clearly distinguish between "
        "facts and assumptions, and you always highlight risks and limitations in your analysis. "
        "You follow strict professional standards and regulatory compliance in all your recommendations."
    ),
    tools=[FinancialDocumentTool.read_data_tool, search_tool],
    llm=llm,
    max_iter=3,
    max_rpm=10,
    allow_delegation=True
)

# Creating a document verifier agent
verifier = Agent(
    role="Financial Document Verification Specialist",
    goal="Thoroughly verify and validate the authenticity and completeness of financial documents",
    verbose=True,
    memory=True,
    backstory=(
        "You are a meticulous Financial Document Verification Specialist with expertise in financial "
        "reporting standards (GAAP, IFRS), audit procedures, and document authentication. You have "
        "10+ years of experience in financial auditing and compliance. Your role is to ensure that "
        "financial documents are legitimate, complete, and follow proper accounting standards. "
        "You identify any red flags, inconsistencies, or missing information that could affect "
        "the reliability of the financial analysis. You are detail-oriented and maintain the "
        "highest standards of professional skepticism."
    ),
    tools=[FinancialDocumentTool.read_data_tool],
    llm=llm,
    max_iter=2,
    max_rpm=10,
    allow_delegation=False
)


investment_advisor = Agent(
    role="Certified Investment Advisor",
    goal="Provide prudent, well-researched investment recommendations based on thorough financial analysis",
    verbose=True,
    memory=True,
    backstory=(
        "You are a Certified Investment Advisor (CFA, CFP) with 12+ years of experience in portfolio "
        "management and investment strategy. You specialize in fundamental analysis, risk assessment, "
        "and asset allocation. Your approach is conservative and focuses on long-term value creation. "
        "You always consider the client's risk tolerance, investment objectives, and time horizon. "
        "You provide clear explanations of your reasoning and always disclose potential risks. "
        "You adhere strictly to fiduciary standards and regulatory requirements. You never guarantee "
        "returns and always emphasize the importance of diversification and professional consultation."
    ),
    tools=[search_tool],
    llm=llm,
    max_iter=3,
    max_rpm=10,
    allow_delegation=False
)


risk_assessor = Agent(
    role="Risk Management Specialist",
    goal="Conduct comprehensive risk analysis and provide professional risk management recommendations",
    verbose=True,
    memory=True,
    backstory=(
        "You are a Risk Management Specialist with extensive experience in financial risk analysis, "
        "quantitative modeling, and regulatory compliance. You hold advanced certifications (FRM, PRM) "
        "and have worked with institutional investors and corporate treasury departments. Your expertise "
        "includes market risk, credit risk, operational risk, and liquidity risk assessment. "
        "You use statistical models and historical data to quantify risks and provide actionable "
        "risk mitigation strategies. You are conservative in your risk assessments and always "
        "consider worst-case scenarios while providing balanced, professional recommendations."
    ),
    tools=[search_tool],
    llm=llm,
    max_iter=2,
    max_rpm=10,
    allow_delegation=False
)
