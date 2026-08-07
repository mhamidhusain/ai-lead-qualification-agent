# AI Lead Qualification Agent

A Python-based AI agent that evaluates potential business leads for a digital marketing or AI automation agency.

The program combines rule-based scoring with AI-generated analysis to classify leads and recommend the next sales action.

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

## Project Structure

```text
ai-lead-qualification-agent/
├── app.py
├── scoring.py
├── prompts.py
├── test_scoring.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Sample Output

A complete example report is available in [`sample_output.txt`](sample_output.txt).