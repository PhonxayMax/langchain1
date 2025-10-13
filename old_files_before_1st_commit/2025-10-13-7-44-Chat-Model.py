# Import the OpenAI library to interact with OpenAI's API (like ChatGPT, GPT-4, etc.)
from openai import OpenAI 

# Import load_dotenv to read environment variables from a .env file
# This is a secure way to store sensitive information like API keys
from dotenv import load_dotenv 
 
# Load environment variables from a .env file in the current directory
# This will read your OPENAI_API_KEY from the .env file and make it available
load_dotenv()  
                          
# Create an OpenAI client instance
# This client will automatically use the OPENAI_API_KEY from your environment variables
# You'll use this client to make API calls to OpenAI services
client = OpenAI()