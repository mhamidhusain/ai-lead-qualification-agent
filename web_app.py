import streamlit as st
from openai import OpenAI
from scoring import calculate_score, classify_lead
from prompts import LEAD_QUALIFICATION_INSTRUCTIONS

client = OpenAI()

st.title("AI Lead Qualification Agent")
st.write("Enter lead details below to evaluate the opportunity.")

name = st.text_input("Client name")
company = st.text_input("Company name")
business_type = st.text_input("Type of business")
service_needed = st.text_input("Service needed")
budget = st.number_input(
    "Estimated monthly budget in CAD",
    min_value=0.0,
    step=100.0
)
timeline = st.text_input("When do they want to start?")

decision_maker = st.selectbox(
    "Are they the decision-maker?",
    ["yes", "no", "unknown"]
)

if st.button("Qualify Lead"):
    score = calculate_score(
        budget,
        timeline,
        decision_maker
    )

    classification = classify_lead(score)

    lead_information = f"""
Client name: {name}
Company: {company}
Business type: {business_type}
Service needed: {service_needed}
Monthly budget: ${budget:,.2f}
Timeline: {timeline}
Decision-maker: {decision_maker}

Calculated lead score: {score}/10
Calculated classification: {classification}
"""

    try:
        response = client.responses.create(
            model="gpt-5.1",
            instructions=LEAD_QUALIFICATION_INSTRUCTIONS,
            input=lead_information
        )

        st.subheader("Qualification Result")
        st.write(f"Lead Score: {score}/10")
        st.write(f"Classification: {classification}")

        st.subheader("AI Analysis")
        st.write(response.output_text)

    except Exception as error:
        st.error(f"An error occurred: {error}")