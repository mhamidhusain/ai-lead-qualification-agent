# AI Lead Qualification Agent

A Python-based AI agent that evaluates potential business leads for a digital marketing or AI automation agency.

The program combines rule-based scoring with AI-generated analysis to classify leads and recommend the next sales action.

## Demo

The project includes both:

- A command-line version: `app.py`
- A Streamlit web version: `web_app.py`

Run the web app with:

```bash
streamlit run web_app.py

## Features

- Collects lead information
- Validates budget and decision-maker input
- Calculates a lead score from 1 to 10
- Classifies leads as Hot, Warm, or Cold
- Uses the OpenAI API to explain the result
- Identifies missing information
- Recommends the next action
- Generates follow-up questions
- Saves the complete lead report
- Includes automated scoring tests
```markdown
- Browser-based Streamlit interface
- Downloadable lead qualification reports

## Project Structure

```text
ai-lead-qualification-agent/
├── app.py
├── web_app.py
├── scoring.py
├── prompts.py
├── test_scoring.py
├── sample_output.txt
├── requirements.txt
├── README.md
└── .gitignore
```

## Sample Output

A complete example report is available in [`sample_output.txt`](sample_output.txt).

## Skills Demonstrated

- Python programming
- API integration
- OpenAI Responses API
- Rule-based lead scoring
- Input validation
- Streamlit web development
- File handling
- Automated testing
- Git and GitHub
- Modular project structure