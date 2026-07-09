from scoring import calculate_score
import json
import pandas as pd
import streamlit as st

# -----------------------------
# Page Title
# -----------------------------
st.set_page_config(page_title="Sherlock Candidate Identifier")

st.title("🕵️ Sherlock Candidate Identifier")

st.write("AI system to identify the interview candidate using multiple weak signals.")

# Candidate Details
candidate_profile = {
    "name": "Padmapriya",
    "email": "padmapriya@gmail.com"
}
# -----------------------------
# Load Data
# -----------------------------
with open("participants.json", "r") as file:
    participants = json.load(file)

# -----------------------------
# AI Scoring
# -----------------------------
# 👇 This is the new code
for person in participants:
    score, reasons = calculate_score(person, candidate_profile)

    person["score"] = score
    person["reasons"] = reasons

# -----------------------------
# Find Candidate
# -----------------------------
candidate = max(participants, key=lambda x: x["score"])

# -----------------------------
# Show Participants
# -----------------------------
st.subheader("📋 Meeting Participants")

df = pd.DataFrame(participants)

st.dataframe(
    df.drop(columns=["reasons"])
)
st.subheader("📊 Participant Scores")

score_df = df[["display_name", "score"]]

st.bar_chart(score_df.set_index("display_name"))
# -----------------------------
# Candidate Result
# -----------------------------
st.subheader("🏆 Candidate Identified")

st.success(candidate["display_name"])

confidence = min(candidate["score"], 100)

st.metric("Confidence Score", f"{confidence}%")

st.progress(confidence / 100)

st.progress(candidate["score"] / 100)

st.subheader("Why was this participant selected?")

for reason in candidate["reasons"]:
    st.write(reason)