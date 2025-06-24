import json

# Ground truth routing for each ticket
GROUND_TRUTH = {
    "SUP-001": "Customer Recovery Team",
    "SUP-002": "General Support",
    "SUP-003": "Product Management",
    "SUP-004": "Tier-2 Technical Support",
    "SUP-005": "Tier-2 Technical Support"
}

def evaluate_results(filename="results.json"):
    with open(filename, "r") as f:
        results = json.load(f)

    correct_routes = 0
    urgency_consistent = 0
    high_value_customers = 0
    high_priority_given = 0

    for r in results:
        ticket_id = r["ticket_id"]
        expected_route = GROUND_TRUTH.get(ticket_id)
        predicted_route = r["route_to"]

        # Metric 1: Routing Accuracy
        if predicted_route == expected_route:
            correct_routes += 1

        # Metric 2: Urgency Consistency
        if r["urgency"].lower() == "high" and r["priority_level"].lower() != "low":
            urgency_consistent += 1

        # Metric 3: High-value customer prioritization
        if r["priority_level"].lower() in ["high", "medium"]:
            if r["ticket_id"] in ["SUP-002", "SUP-005"]:  # both are enterprise
                high_value_customers += 1
                high_priority_given += 1

    total = len(results)

    print("\n📊 EVALUATION METRICS")
    print(f"✅ Routing Accuracy: {correct_routes}/{total} ({(correct_routes/total)*100:.1f}%)")
    print(f"✅ Urgency Consistency: {urgency_consistent}/{total} ({(urgency_consistent/total)*100:.1f}%)")
    if high_value_customers > 0:
        print(f"✅ Priority for High-Value Customers: {high_priority_given}/{high_value_customers} ({(high_priority_given/high_value_customers)*100:.1f}%)")

if __name__ == "__main__":
    evaluate_results()
