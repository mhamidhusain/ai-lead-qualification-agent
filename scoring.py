def calculate_score(budget, timeline, decision_maker):
    score = 1

    # Budget score
    if budget >= 2500:
        score += 4
    elif budget >= 1500:
        score += 3
    elif budget >= 750:
        score += 2
    elif budget > 0:
        score += 1

    # Timeline score
    timeline = timeline.lower()

    urgent_phrases = [
        "immediately",
        "as soon as possible",
        "asap",
        "one week",
        "two weeks",
        "within a month",
        "this month",
    ]

    medium_phrases = [
        "two months",
        "three months",
        "next quarter",
    ]

    if any(phrase in timeline for phrase in urgent_phrases):
        score += 3
    elif any(phrase in timeline for phrase in medium_phrases):
        score += 2
    else:
        score += 1

    # Decision-maker score
    decision_maker = decision_maker.lower()

    if decision_maker == "yes":
        score += 2
    elif decision_maker == "unknown":
        score += 1

    return min(score, 10)


def classify_lead(score):
    if score >= 8:
        return "Hot"
    elif score >= 5:
        return "Warm"
    else:
        return "Cold"