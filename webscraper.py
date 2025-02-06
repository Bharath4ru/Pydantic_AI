from pydantic_ai import Agent
from dotenv import load_dotenv
load_dotenv()

agent = Agent(  
    'groq:llama-3.3-70b-versatile',
    system_prompt='Be concise, reply with entire knowledge.',  
)

result = agent.run_sync('list all stats of KL Rahul?')  
print(result.data)