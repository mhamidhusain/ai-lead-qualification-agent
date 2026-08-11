import streamlit as st
from openai import OpenAI
from scoring import calculate_score, classify_lead
from prompts import LEAD_QUALIFICATION_INSTRUCTIONS
from datetime import datetime

st.set_page_config(
    page_title="AI Lead Qualification Agent",
    page_icon="🤖",
    layout="centered"
)

st.title("AI Lead Qualification Agent")
st.caption(
    "Evaluate leads using rule-based scoring and AI-generated recommendations."
)

st.divider()

st.subheader("Lead Details")

client = OpenAI()


with st.form("lead_form"):
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

    submitted = st.form_submit_button(
    "Qualify Lead",
    type="primary"
)

if submitted:
    if not name or not company or not business_type or not service_needed or not timeline:
        st.warning("Please complete all required fields.")
        st.stop()
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

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Lead Score", f"{score}/10")

        with col2:
            st.metric("Classification", classification)

        st.divider()

        st.subheader("AI Analysis")
        st.markdown(response.output_text)

        report_text = f"""
        LEAD INFORMATION
        ================

        Client name: {name}
        Company: {company}
        Business type: {business_type}
        Service needed: {service_needed}
        Monthly budget: ${budget:,.2f}
        Timeline: {timeline}
        Decision-maker: {decision_maker}

        QUALIFICATION RESULT
        ====================

        Lead Score: {score}/10
        Classification: {classification}

        AI ANALYSIS
        ===========

        {response.output_text}
        """
        timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
        safe_name = name.replace(" ", "_")
        safe_company = company.replace(" ", "_")

        download_filename = (
            f"{safe_name}_{safe_company}_{timestamp}.txt"
)

        st.download_button(
            label="Download Lead Report",
            data=report_text,
            file_name=download_filename,
            mime="text/plain"
)

    except Exception as error:
        st.error(f"An error occurred: {error}")