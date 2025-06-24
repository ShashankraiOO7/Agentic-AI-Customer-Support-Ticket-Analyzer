class RoutingAgent:
    def route(self, tone, urgency, issue_type, priority_level):
        tone = tone.lower()
        urgency = urgency.lower()
        issue_type = issue_type.lower()
        priority_level = priority_level.lower()

        if "api" in issue_type or "server" in issue_type or "technical" in issue_type:
            if priority_level == "high":
                return {"route_to": "Tier-2 Technical Support"}
            else:
                return {"route_to": "General Support"}
        elif "billing" in issue_type:
            return {"route_to": "Finance Team"}
        elif "feature" in issue_type:
            return {"route_to": "Product Management"}
        elif "frustrated" in tone or "negative" in tone:
            if priority_level == "low":
                return {"route_to": "Customer Recovery Team"}
        return {"route_to": "General Support"}
