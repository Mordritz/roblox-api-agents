import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ROBLOX_API_KEY = os.getenv("ROBLOX_API_KEY")