import os
import json
import re
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env and configure Gemini
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-pro")

class PriorityAgent:
    def evaluate(self, customer_tier, previous_tickets, monthly_revenue, account_age_days,urgency):
        prompt = f"""
            You are a smart support assistant.

            Customer profile:
            - Tier: {customer_tier}
            - Monthly Revenue: {monthly_revenue}
            - Account Age: {account_age_days} days
            - Previous Tickets: {previous_tickets}
            - Urgency: {urgency}

            Decide one of: "low", "medium", or "high"

            Rules:
            - Enterprise + high urgency → high priority
            - Free tier + no revenue → low unless urgency is extreme
            - Medium urgency + premium = medium priority
            - Urgent messages should increase priority if customer is not free

            Return this exact JSON format:
            {{ "priority_level": "..." }}
            """


        response = model.generate_content(prompt)
        text = response.text.strip()

        #print("Gemini raw output (priority):\n", text)

        # Clean markdown if present
        if text.startswith("```"):
            text = re.sub(r"```[a-zA-Z]*", "", text).strip()
            if text.endswith("```"):
                text = text[:-3].strip()

        try:
            return json.loads(text)
        except json.JSONDecodeError:
            print("JSON parse error. Returning fallback.")
            return {"priority_level": "unknown"}
