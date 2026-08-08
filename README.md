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
```

## Features

- Collects lead information
- Validates budget and decision-maker input
- Calculates a lead score from 1 to 10
- Classifies leads as Hot, Warm, or Cold
- Uses the OpenAI API to explain the result
- Identifies missing information
- Recommends the next action
- Generates follow-up questions
- Saves lead qualification reports
- Browser-based Streamlit interface
- Downloadable lead reports
- Includes automated scoring tests

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

## Technologies Used

- Python
- OpenAI API
- Streamlit
- Git and GitHub
- Rule-based scoring
- File handling
- Automated testing with Python assertions

## How the Scoring Works

The lead score is calculated using three factors:

- Monthly budget
- Expected start timeline
- Whether the contact is the decision-maker

The score is then classified as:

```text
8–10: Hot
5–7: Warm
1–4: Cold
```

The AI does not change the calculated score. It explains the result and recommends the next action.

## Installation

Clone the repository:

```bash
git clone https://github.com/mhamidhusain/ai-lead-qualification-agent.git
```

Open the project folder:

```bash
cd ai-lead-qualification-agent
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## API Key Setup

Create an OpenAI API key and save it as an environment variable named:

```text
OPENAI_API_KEY
```

The API key should never be written directly inside the Python code.

## Run the Command-Line Application

```bash
python app.py
```

## Run the Web Application

```bash
streamlit run web_app.py
```

## Run the Tests

```bash
python test_scoring.py
```

Expected result:

```text
All scoring tests passed!
```

## Example Lead

```text
Client name: Ahmed
Company: Ahmed Dental Clinic
Business type: Dental Clinic
Service needed: More patients through Google Ads
Monthly budget: $2,500
Timeline: Within two weeks
Decision-maker: Yes
```

Example result:

```text
Lead Score: 10/10
Classification: Hot
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

## Security

- The OpenAI API key is not stored in the repository.
- Generated lead reports are excluded through `.gitignore`.
- Python cache files are excluded from GitHub.

## Future Improvements

- CRM integration
- Google Sheets integration
- Automatic email follow-up generation
- Lead history and analytics
- User authentication
- Cloud deployment