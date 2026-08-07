from openai import OpenAI
from scoring import calculate_score, classify_lead
from prompts import LEAD_QUALIFICATION_INSTRUCTIONS
from datetime import datetime

client = OpenAI()


def get_budget():
    while True:
        budget_input = input("Estimated monthly budget in CAD: $")

        try:
            return float(budget_input.replace(",", ""))
        except ValueError:
            print("Please enter a number, such as 2500.")

def get_yes_no_unknown():
    while True:
        answer = input(
            "Are they the decision-maker? (yes/no/unknown): "
        ).strip().lower()

        if answer in ["yes", "no", "unknown"]:
            return answer

        print("Please enter yes, no, or unknown.")


def qualify_lead():
    print("\nPlease enter the potential client's information.\n")

    name = input("Client name: ")
    company = input("Company name: ")
    business_type = input("Type of business: ")
    service_needed = input("Service they need: ")
    budget = get_budget()
    timeline = input("When do they want to start?: ")
    decision_maker = get_yes_no_unknown()


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


    try:
        response = client.responses.create(
            model="gpt-5.1",
            instructions=LEAD_QUALIFICATION_INSTRUCTIONS,
            input=lead_information
        )

        print("\nLead Qualification Result:\n")
        print(response.output_text)

        save_choice = input(
            "\nSave this lead report? (yes/no): "
        )

        if save_choice.lower() == "yes":
            timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")

            safe_name = name.replace(" ", "_")
            safe_company = company.replace(" ", "_")

            filename = f"{safe_name}_{safe_company}_{timestamp}.txt"

            with open(filename, "w", encoding="utf-8") as file:
                file.write("LEAD INFORMATION\n")
                file.write("================\n")
                file.write(lead_information)

                file.write("\nQUALIFICATION RESULT\n")
                file.write("====================\n")
                file.write(response.output_text)

            print(f"Lead report saved to {filename}")

            print(f"Lead report saved to {filename}")

    except Exception as error:
        print(f"\nAn error occurred: {error}")

print("AI Lead Qualification Assistant")

while True:
    print("\nChoose an option:")
    print("1. Qualify a lead")
    print("2. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        qualify_lead()
    elif choice == "2":
        print("Goodbye!")
        break
    else:
        print("Please enter 1 or 2.")