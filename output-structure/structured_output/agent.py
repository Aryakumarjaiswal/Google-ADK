#pip install google-adk
from datetime import datetime
from google.adk.agents import Agent
from pydantic import BaseModel,Field


class Email(BaseModel):
    subject:str=Field("Subject for the email.conclude within 4 words")
    body:str=Field("Body of the email")


root_agent = Agent(
    name="greeting_agent",
    #sub-folder name must match
    # https://ai.google.dev/gemini-api/docs/models
    model="gemini-2.5-flash",
    description="structured_output", #other agents refer this
  
   # system instruction is given by below
     instruction="""             
  User will give you situation write an email to give subject and email body in structured output  format.note email body should be within 60 words.
    """,

    output_schema=Email
  
)


