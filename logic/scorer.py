def score_lead(row):
    score = 0
    reasons = []
    risks = []

    # Budget scoring
    if row["budget"] == "High":
        score += 30
        reasons.append("High budget available")
    elif row["budget"] == "Medium":
        score += 20
        reasons.append("Moderate budget")
    else:
        score += 10
        risks.append("Limited budget")

    # Urgency scoring
    if row["urgency"] == "High":
        score += 25
        reasons.append("High urgency to proceed")
    elif row["urgency"] == "Medium":
        score += 15
        reasons.append("Moderate urgency")
    else:
        score += 5
        risks.append("Low urgency")

    # Decision maker engagement
    if row["decision_maker_engaged"] == "Yes":
        score += 25
        reasons.append("Decision maker engaged")
    else:
        risks.append("Decision maker not engaged")

    # Call notes analysis (simple intent check)
    notes = str(row["call_notes"]).lower()

    if any(word in notes for word in ["pricing", "proposal", "deployment", "timeline", "budget"]):
        score += 20
        reasons.append("Clear purchase intent in discussions")
    else:
        score += 10
        risks.append("Intent not clearly expressed")

    # Category
    if score >= 75:
        category = "High"
    elif score >= 45:
        category = "Medium"
    else:
        category = "Low"

    return {
        "score": score,
        "category": category,
        "reasons": reasons,
        "risks": risks
    }
