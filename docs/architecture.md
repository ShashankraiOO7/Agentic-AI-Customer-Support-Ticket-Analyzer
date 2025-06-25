# System Architecture – Customer Support Ticket Analyzer

## 1. Overview

This document describes the multi-agent architecture designed for the Draconic Case Study – Option A: Customer Support Ticket Analyzer. The system is built using a modular agentic approach powered by Google Gemini 1.5 Pro LLM, with agents communicating sequentially to analyze support tickets and route them appropriately.

---

## 2. Agent-Based Architecture

###  MessageAnalysisAgent

**Responsibilities:**

* Analyze the subject and message of a support ticket
* Extract three key fields: `tone`, `urgency`, and `issue_type`

**Technologies:**

* Google Gemini LLM via `google.generativeai`
* `.env`-based key loading

**Sample Output:**

```json
{
  "tone": "frustrated",
  "urgency": "high",
  "issue_type": "technical"
}
```

**Prompt Iteration:**

* **V1:** Basic instruction with open-ended JSON return → returned explanations
* **V2:** Added explicit formatting: `Respond with JSON: { "tone": ..., "urgency": ..., ... }`
* **V3 (final):** Prefixed instruction with "Do not include markdown/code blocks." Ensured clean parsing with `json.loads()`.

---

###  PriorityAgent

**Responsibilities:**

* Evaluate customer’s support priority based on business metadata + message urgency

**Inputs:**

* `customer_tier`, `previous_tickets`, `monthly_revenue`, `account_age_days`, `urgency`

**Prompt Iteration:**

* **V1:** Looked only at tier + revenue → ignored urgent messages
* **V2:** Added logic to raise priority on "high urgency" unless customer was "free"
* **V3 (final):** Instruction: "Increase priority if urgency is high and customer is not free-tier"

**Sample Output:**

```json
{
  "priority_level": "medium"
}
```

---

###  RoutingAgent

**Responsibilities:**

* Decide the final department or team the ticket should be routed to
* Use outputs from both `MessageAnalysisAgent` and `PriorityAgent`

**Logic-Based (non-LLM)**

* Uses keyword fuzzy matching: e.g. `"api" in issue_type`
* Handles special conditions like `tone = frustrated AND priority = low → Recovery Team`

---

## 3. Flow Diagram (Text-Based)

```
Input Ticket
     ↓
MessageAnalysisAgent → tone, urgency, issue_type
     ↓
PriorityAgent         → priority_level (uses urgency)
     ↓
RoutingAgent          → route_to (final decision)
     ↓
Final Output (printed + saved to results.json)
```

---

## 4. Prompt Strategy Summary

| Agent                | Prompt Strengthening Done                | Final Strategy                         |
| -------------------- | ---------------------------------------- | -------------------------------------- |
| MessageAnalysisAgent |  Added strict JSON + stripped markdown | "Return only JSON object"              |
| PriorityAgent        |  Used urgency + tier combo             | "Urgency bumps priority unless free"   |
| RoutingAgent         | N/A (rule-based)                         | Rule logic refined with fuzzy matching |

---

## 5. Robustness Measures

*  Safe fallback if JSON parsing fails
*  `json.loads()` used instead of `eval()`
*  Markdown block stripping for Gemini responses
*  Supports all 5 test cases without crashing

---

## 6. Next Steps

* Evaluation already implemented in `evaluation.py`
* Ready for packaging with README and submission artifacts
