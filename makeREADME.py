import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

def generate_readme(chunks_by_file, imports=None, project_name=None):
    # Flatten all function dicts
    all_functions = []
    dependencies_str = ", ".join(imports or [])
    for file, functions in chunks_by_file.items():
        all_functions.extend(functions)

    # Build prompt string
    all_functions_str = "\n\n".join([
        f"{f['file']}::{f['name']}()\n{f['code']}" for f in all_functions
    ])

    prompt = f"""
You're an expert AI developer assistant.

Generate a detailed README.md for a Python project named "{project_name or 'Unnamed Project'}".

Include:
- Project description
- Main features
- Project structure
- Dependencies: {dependencies_str}
- How to install and run
- Brief summary of important functions

Here is the code:
{all_functions_str}

README:
"""
    response = model.generate_content(prompt)
    return response.text.strip()

