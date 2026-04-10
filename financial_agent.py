from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools

import os
from dotenv import load_dotenv
load_dotenv()

## Financial agent
finance_agent=Agent(
    name="Finance AI Agent",
    model=Groq(id="llama-3.1-8b-instant"),
    tools=[
        # Enable just the necessary tools to prevent exceeding Groq rate limits while dropping DuckDuckGo entirely
        YFinanceTools(stock_price=True, analyst_recommendations=True, company_news=True),
    ],
    instructions=["Always include sources", "Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

finance_agent.print_response("Summarize analyst recommendation and share the latest news for TESLA", stream=False)
