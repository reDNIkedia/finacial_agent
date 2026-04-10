from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
from dotenv import load_dotenv
load_dotenv()

## Financial agent
finance_agent=Agent(
    name="Finance AI Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        # Enable just the necessary tools to prevent exceeding Groq rate limits while dropping DuckDuckGo entirely
        YFinanceTools(stock_price=True, analyst_recommendations=True, 
        company_news=True,stock_fundamentals=True),
    ],
    instructions=["Always include sources", "Use tables to display the data", "IMPORTANT: Always pass integers for numerical arguments (e.g. 5 not '5')"],
    show_tool_calls=True,
    markdown=True,
)

web_search_agent=Agent(
    name="Web Search Agent",
    role="You are a web search agent that can search the web for information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        # Enable just the necessary tools to prevent exceeding Groq rate limits while dropping DuckDuckGo entirely
        DuckDuckGo(),
    ],
    instructions=["Always include sources", "Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

multi_agent=Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    team=[finance_agent,web_search_agent],
    instructions=["Always include sources", "Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

multi_agent.print_response("Summarize in details the analyst recommendation ,share the latest news and fundamentals for META", stream=True)
