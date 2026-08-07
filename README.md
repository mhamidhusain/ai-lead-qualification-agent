# AI Lead Qualification Agent

A Python-based AI agent that evaluates potential business leads for a digital marketing and AI automation agency.

## Features

- Collects lead information
- Calculates a lead score from 1 to 10
- Classifies leads as Hot, Warm, or Cold
- Uses AI to explain the result
- Recommends the next action
- Generates useful follow-up questions
- Saves the full report to a text file

## Technologies Used

- Python
- OpenAI API
- Rule-based scoring
- File handling

## How It Works

The Python program calculates the lead score using:

- Monthly budget
- Expected start timeline
- Whether the contact is the decision-maker

The AI then analyzes the information without changing the calculated score.

## How to Run

Install the OpenAI package:

```bash
pip install openai