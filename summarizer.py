import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

def summarize_function(code, name=None):
    prompt = f"""You are an AI code assistant.
Given this Python function, return a short one-line summary of what it does, like a good docstring.

Function:
{code}

Summary:"""
    try:
        response = model.generate_content(prompt)
        return response.text.strip().split("\n")[0]
    except Exception as e:
        return "Could not generate summary."
code_snippet = """def add(a, b):    \"\"\"Adds two numbers together.\"\"\"
    return a + b
"""
# print(summarize_function(code_snippet))  # Summarize the function
# # print(model.generate_content("hello, how are you?").text.strip().split("\n")[0])