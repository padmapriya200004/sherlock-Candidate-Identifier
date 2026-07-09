from rapidfuzz import fuzz

def calculate_score(person, candidate_profile):
    score = 0
    reasons = []

    # Email Match
    if person["email"] == candidate_profile["email"]:
        score += 40
        reasons.append("Email matched")

    # Name Similarity
    similarity = fuzz.ratio(
        person["display_name"].lower(),
        candidate_profile["name"].lower()
    )

    if similarity >= 80:
        score += 20
        reasons.append(f"Name similarity ({similarity:.0f}%)")

    # Joined First
    if person["joined_first"]:
        score += 15
        reasons.append("Joined first")

    # Camera ON
    if person["camera"]:
        score += 10
        reasons.append("Camera ON")

    # Microphone ON
    if person["mic_on"]:
        score += 10
        reasons.append("Microphone ON")

    # Speaking Duration
    if person["speaking_duration"] > 300:
        score += 20
        reasons.append("Longest speaking duration")

    # Screen Share
    if not person["screen_share"]:
        score += 5
        reasons.append("Not sharing screen")

    return score, reasons