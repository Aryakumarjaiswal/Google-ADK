#pip install google-adk
from datetime import datetime
from google.adk.agents import Agent
def get_current_time() -> dict:
    """
    Get the current time in the format YYYY-MM-DD HH:MM:SS
    """
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

root_agent = Agent(
    name="greeting_agent",
    #sub-folder name must match
    # https://ai.google.dev/gemini-api/docs/models
    model="gemini-2.5-flash",
    description="Greeting agent", #other agents refer this
  
   # system instruction is given by below
     instruction="""             
   Bhai you're Braj bhasha tutor.user will give hindi/hinglish/english input your task is convert i/p into braj bhasha and give response in braj bhasha.
   When user asks to tell time then use 'get_current_time' tool.
    """,
    tools=[get_current_time]
)
# folder structure parent folder>sub folder
#|__init__.py
#|.env
#|agent.py
#|
#
#
#############
#Once setup is done then run 'adk web' in terminal to run agent in ui

###############3
ADK supports 2 main types of Tools
1.Custumm tool
2.Build In tools

-we cant mix custom tools and build in tools


