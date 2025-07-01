import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types

try:
    user_input = sys.argv[1]
except:
    print("Prompt not provided")
    sys.exit(1)

verbose = False 
try:
    if sys.argv[2] == '--verbose':
        verbose = True
except:
    pass

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

messages = [
    types.Content(role="user", parts=[types.Part(text=user_input)]),
]

content = client.models.generate_content(model='gemini-2.0-flash-001',contents=messages)

def main():
    if verbose is True:
        print("User prompt:",content.text)
        print("Prompt tokens:",content.usage_metadata.prompt_token_count)
        print("Response tokens:",content.usage_metadata.candidates_token_count)
    else:
        print(content.text)
    

if __name__ == "__main__":
    main()
