import streamlit as st
import json
from archetypes import archetypes

st.title("Creative Archetype Assistant AI")

st.write("Answer the questions below to discover your dominant creative archetype.")

questions = [
    "I enjoy imagining future possibilities.",
    "I prefer structured planning over improvisation.",
    "I love expressing myself through creation.",
    "I enjoy exploring new ideas and risks.",
    "I focus strongly on achieving goals."
]

scores = {
    "Visionary": 0,
    "Analyst": 0,
    "Creator": 0,
    "Explorer": 0,
    "Strategist": 0
}

answers = []

for q in questions:
    response = st.slider(q, 1, 5, 3)
    answers.append(response)

if st.button("Analyze My Archetype"):
    scores["Visionary"] += answers[0]
    scores["Analyst"] += answers[1]
    scores["Creator"] += answers[2]
    scores["Explorer"] += answers[3]
    scores["Strategist"] += answers[4]

    dominant = max(scores, key=scores.get)

    st.subheader(f"Your Dominant Archetype: {dominant}")
    with open("memory.json", "r") as f:
        data = json.load(f)

    data.append({
        "dominant_archetype": dominant
    })

    with open("memory.json", "w") as f:
        json.dump(data, f)
        
    st.write(archetypes[dominant]["description"])
    st.write("### Strengths")
    st.write(archetypes[dominant]["strengths"])
    st.write("### Growth Advice")
    st.write(archetypes[dominant]["growth_advice"])
