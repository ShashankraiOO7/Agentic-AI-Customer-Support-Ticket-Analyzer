import os
import json
import re
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-pro")

class MessageAnalysisAgent:
    def analyze(self, subject, message):
        prompt = f"""
        Analyze this support ticket and return a JSON object like:
        {{
          "tone": "...",
          "urgency": "...",
          "issue_type": "..."
        }}

        Subject: {subject}
        Message: {message}
        """
        response = model.generate_content(prompt)
        text = response.text.strip()
        #print("Gemini raw output:\n", text)

        # Clean up markdown and ```json blocks
        if text.startswith("```"):
            text = re.sub(r"```[a-zA-Z]*", "", text).strip()
            if text.endswith("```"):
                text = text[:-3].strip()

        try:
            return json.loads(text)
        except json.JSONDecodeError:
            print("Failed to parse JSON:\n", text)
            return {
                "tone": "unknown",
                "urgency": "unknown",
                "issue_type": "unclear"
            }
