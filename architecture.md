# Sherlock Candidate Identifier Architecture

Meeting Participants
        │
        ▼
participants.json
        │
        ▼
Data Loader (app.py)
        │
        ▼
AI Scoring Engine (scoring.py)

Signals Used:
- Email Match
- Name Similarity
- Joined First
- Camera ON
- Microphone ON
- Speaking Duration
- Screen Sharing

        │
        ▼
Confidence Score

        │
        ▼
Candidate Selection

        │
        ▼
Streamlit Dashboard