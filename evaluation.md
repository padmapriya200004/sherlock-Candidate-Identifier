# Evaluation

## Testing Performed

The system was tested using multiple interview participant scenarios.

### Test Case 1

Candidate email matched.

Result:
- Candidate identified correctly.
- Confidence Score: High

---

### Test Case 2

Candidate joined using the display name "MacBook Pro".

Result:
- Candidate still identified using email and behavioural signals.

---

### Test Case 3

Candidate display name changed to "Padmapriya D".

Result:
- Name similarity matching successfully identified the candidate.

---

### Test Case 4

Candidate email removed.

Result:
- Candidate was still identified using multiple weak signals.
- Confidence score decreased appropriately.

---

## Edge Cases

- Incorrect display names
- Missing email
- Multiple interviewers
- Screen sharing by interviewer
- Participants with similar names

---

## Accuracy

The prototype performs well on simulated meeting data.

Confidence improves as more participant information becomes available.

---

## Limitations

- Uses simulated meeting data.
- Does not connect directly to Zoom, Google Meet or Microsoft Teams.
- No face recognition.
- No voice biometrics.

---

## Future Improvements

- Live meeting integration
- Face recognition
- Voice recognition
- Machine Learning based confidence estimation
- Continuous confidence updates