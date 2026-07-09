# Sherlock Candidate Identifier
Sherlock-Candidate-Identifier/
│
├── app.py
├── scoring.py
├── participants.json
├── architecture.md
├── architecture.png
├── evaluation.md
├── README.md
└── requirements.txt
## Overview

This project is a prototype AI system that identifies the interview candidate during an online meeting using multiple weak signals instead of relying on a single rule.

The application is built using Python and Streamlit.

---

## Features

- Identifies the interview candidate automatically
- Uses multiple weak signals
- Email matching
- Name similarity matching (RapidFuzz)
- Speaking duration analysis
- Camera status
- Microphone status
- Join order
- Screen sharing detection
- Confidence score generation
- Explainable AI (shows why a participant was selected)
- Participant score comparison chart

---

## Technologies Used

- Python
- Streamlit
- Pandas
- RapidFuzz

---

## Project Structure

```
Sherlock-Candidate-Identifier/
│
├── app.py
├── scoring.py
├── participants.json
├── architecture.md
├── README.md
├── requirements.txt
└── venv/
```

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Assumptions

- Each participant has one webcam and audio stream.
- Participant information is available.
- Candidate email is available.
- Speaking duration is calculated externally.
- Multiple weak signals improve confidence.

---

## Future Improvements

- Real-time meeting integration
- Live Google Meet / Zoom support
- Face recognition
- Voice recognition
- Continuous confidence updates
- Machine learning based scoring

---

## Author

Padmapriya D
