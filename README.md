

```markdown
# 🧠 Customer Support Ticket Analyzer (Draconic AI Case Study)

This project is a multi-agent system built to analyze customer support tickets and determine the best routing strategy based on ticket content and customer profile. It was developed as part of the Draconic AI Engineering Case Study.



## 🚀 Objective

Create a multi-agent system using LLM-based agents that:

- Understand the **intent, urgency, and tone** of support tickets  
- Assess **customer priority** using business metrics  
- Recommend **routing decisions** to internal teams  

---

## 🏗️ Architecture Overview

### Agents Used

| Agent Name            | Responsibility                                                 |
|-----------------------|----------------------------------------------------------------|
| `MessageAnalysisAgent` | Extracts `issue_type`, `urgency`, and `tone` from ticket text |
| `PriorityAgent`        | Calculates ticket priority using customer tier, history, etc. |
| `RoutingAgent`         | Recommends routing path based on analysis + priority          |

Agents are implemented using LLMs and Pydantic schema validation.

---

## 🧩 Flow Diagram

```

Ticket Input
↓
\[MessageAnalysisAgent]
↓
\[Tone, Urgency, IssueType] ┐
├→ \[RoutingAgent] → route\_to
\[PriorityAgent] ← Urgency ┘

````

---

## 🔍 Example Ticket Input

```json
{
  "ticket_id": "SUP-001",
  "subject": "This product is completely broken!!!",
  "message": "Nothing works! I can't even log in.",
  "customer_tier": "free",
  "previous_tickets": 0,
  "monthly_revenue": 0,
  "account_age_days": 2
}
````

---

## 📦 File Structure

```
your-name-case-study/
├── main.py                        # Agent pipeline runner
├── agents/
│   ├── message_analysis_agent.py  # Intent, urgency, tone
│   ├── priority_agent.py          # Customer priority scoring
│   ├── routing_agent.py           # Routing decisions
├── evaluation/
│   ├── evaluator.py               # Accuracy & logic evaluator
│   └── ground_truth.json          # Expected results for test cases
├── docs/
│   └── architecture.md            # System design, agents, rationale
├── results.json                   # Output of running all 5 tickets
├── ai_chat_history.txt            # Full dev conversation with ChatGPT
└── README.md                      # You are here
```

---

## 🧪 Evaluation

We used the following metrics:

* **Intent Accuracy**: Did the model predict the right issue type?
* **Routing Accuracy**: Did the ticket get routed to the right team?
* **Priority Consistency**: Was urgency aligned with the final priority level?

Run the evaluation:

```bash
python evaluation/evaluator.py
```

---

## 📈 Key Learnings

* LLMs are excellent at abstracting tone and intent even from short, emotional tickets
* Priority should consider both customer metrics and message urgency
* Prompt engineering and consistency checking dramatically improve reliability

---

## 📽️ (Optional) Video Walkthrough

> *A 3–5 minute demo video may be included showing how the system works, explaining its architecture, and walking through one or two test cases.*

---

## ✅ How to Run

1. Install dependencies:

```bash
pip install requirements.txt
```

2. Set your Gemini API key:

```bash
export Gemini_API_KEY=your-key-here
```

3. Run all agents on test data:

```bash
python main.py
```

4. View results:

```bash
cat results.json
```

5. Run evaluation:

```bash
python evaluation/evaluator.py
```

---

## ✨ Credits

Developed by 
Shashank Rai
```
Indian Institute of Information Technology Lucknow.
```

```
As part of the **Draconic AI Engineer Case Study** (Customer Support Ticket Analyzer)
---

```
