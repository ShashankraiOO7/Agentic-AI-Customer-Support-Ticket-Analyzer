import json
from agents.message_analysis_agent import MessageAnalysisAgent
from agents.priority_agent import PriorityAgent
from agents.routing_agent import RoutingAgent

# All 5 test tickets
tickets = [
    {
        "ticket_id": "SUP-001",
        "subject": "This product is completely broken!!!",
        "message": "Nothing works! I can't even log in.",
        "customer_tier": "free",
        "previous_tickets": 0,
        "monthly_revenue": 0,
        "account_age_days": 2
    },
    {
        "ticket_id": "SUP-002",
        "subject": "Minor UI issue with dashboard",
        "message": "Dashboard numbers are misaligned on mobile.",
        "customer_tier": "enterprise",
        "previous_tickets": 15,
        "monthly_revenue": 25000,
        "account_age_days": 730
    },
    {
        "ticket_id": "SUP-003",
        "subject": "Feature Request: Bulk export",
        "message": "We need to export quarterly reports in bulk.",
        "customer_tier": "premium",
        "previous_tickets": 5,
        "monthly_revenue": 5000,
        "account_age_days": 400
    },
    {
        "ticket_id": "SUP-004",
        "subject": "API rate limits unclear",
        "message": "We're getting blocked at 600 requests/hour, docs say 1000.",
        "customer_tier": "premium",
        "previous_tickets": 8,
        "monthly_revenue": 3000,
        "account_age_days": 180
    },
    {
        "ticket_id": "SUP-005",
        "subject": "Urgent: Security vulnerability?",
        "message": "API responses leak internal server paths. Our security team is concerned.",
        "customer_tier": "enterprise",
        "previous_tickets": 20,
        "monthly_revenue": 50000,
        "account_age_days": 900
    }
]

# Initialize agents
msg_agent = MessageAnalysisAgent()
prio_agent = PriorityAgent()
router = RoutingAgent()

results = []

# Run analysis on all tickets
for ticket in tickets:
    print(f"\n=== Processing Ticket {ticket['ticket_id']} ===")

    # Get tone, urgency, issue type
    msg = msg_agent.analyze(ticket["subject"], ticket["message"])

    # Use urgency from the message output
    prio = prio_agent.evaluate(
        customer_tier=ticket["customer_tier"],
        previous_tickets=ticket["previous_tickets"],
        monthly_revenue=ticket["monthly_revenue"],
        account_age_days=ticket["account_age_days"],
        urgency=msg["urgency"]
    )

    route = router.route(
        tone=msg["tone"],
        urgency=msg["urgency"],
        issue_type=msg["issue_type"],
        priority_level=prio["priority_level"]
    )

    print("Route To:", route["route_to"])
    print(" Tone:", msg["tone"])
    print(" Urgency:", msg["urgency"])
    print(" Issue Type:", msg["issue_type"])
    print(" Priority Level:", prio["priority_level"])

    result = {
        "ticket_id": ticket["ticket_id"],
        "tone": msg["tone"],
        "urgency": msg["urgency"],
        "issue_type": msg["issue_type"],
        "priority_level": prio["priority_level"],
        "route_to": route["route_to"]
    }

    results.append(result)

# Save to JSON
with open("results.json", "w") as f:
    json.dump(results, f, indent=2)

print("\n✅ All results saved to results.json")
