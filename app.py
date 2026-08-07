from openai import OpenAI

client = OpenAI()


def get_budget():
    while True:
        budget_input = input("Estimated monthly budget in CAD: $")

        try:
            return float(budget_input.replace(",", ""))
        except ValueError:
            print("Please enter a number, such as 2500.")


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

    if (
        "immediately" in timeline
        or "one week" in timeline
        or "two weeks" in timeline
        or "within a month" in timeline
    ):
        score += 3
    elif "three months" in timeline:
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


print("AI Lead Qualification Assistant")
print("Please enter the potential client's information.\n")

name = input("Client name: ")
company = input("Company name: ")
business_type = input("Type of business: ")
service_needed = input("Service they need: ")
budget = get_budget()
timeline = input("When do they want to start?: ")
decision_maker = input(
    "Are they the decision-maker? (yes/no/unknown): "
)

lead_score = calculate_score(
    budget,
    timeline,
    decision_maker
)

classification = classify_lead(lead_score)

lead_information = f"""
Client name: {name}
Company: {company}
Business type: {business_type}
Service needed: {service_needed}
Monthly budget: ${budget:,.2f}
Timeline: {timeline}
Decision-maker: {decision_maker}

Calculated lead score: {lead_score}/10
Calculated classification: {classification}
"""

instructions = """
You are a lead qualification assistant for a digital marketing and
AI automation agency.

The program has already calculated the lead score and classification.
Do not change them.

Provide:

1. Lead score
2. Classification
3. Main reasons for the result
4. Important missing information
5. Recommended next action
6. Three useful follow-up questions

Be realistic and concise.
Do not invent information.
"""

try:
    response = client.responses.create(
        model="gpt-5.1",
        instructions=instructions,
        input=lead_information
    )

    print("\nLead Qualification Result:\n")
    print(response.output_text)

    save_choice = input(
        "\nSave this lead report? (yes/no): "
    )

    if save_choice.lower() == "yes":
        with open(
            "lead_report.txt",
            "w",
            encoding="utf-8"
        ) as file:
            file.write("LEAD INFORMATION\n")
            file.write("================\n")
            file.write(lead_information)

            file.write("\nQUALIFICATION RESULT\n")
            file.write("====================\n")
            file.write(response.output_text)

        print("Lead report saved to lead_report.txt")

except Exception as error:
    print(f"\nAn error occurred: {error}")