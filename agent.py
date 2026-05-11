from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field
from google.adk.models.lite_llm import LiteLlm  # For multi-model support
from google.adk.sessions import InMemorySessionService
from dotenv import load_dotenv
from google.adk.agents import Agent
import os
load_dotenv()

# --- Define Output Schema ---
class EmailContent(BaseModel):
    subject: str = Field(
        description="The subject line of the email. Should be concise and descriptive."
    )
    body: str = Field(
        description="The main content of the email. Should be well-formatted with proper greeting, paragraphs, and signature."
    )

model=LiteLlm(
model="openrouter/openai/gpt-4",
api_key=os.getenv("OPENROUTER_API_KEY")

)

root_agent=Agent(
name="email_expert",
description="You're receptionalist asking for topic to generate email",
model=model,
instruction="You're greeter agent who 1st greets ask for 4 words"
)


