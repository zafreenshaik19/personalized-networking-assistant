import streamlit as st
import json

from services.topic_generator import generate_starters
from services.history_logger import save_history
from services.fact_checker import fact_check

st.title("🤝 Personalized Networking Assistant")

st.write("Generate smart conversation starters for networking events.")

# -----------------------------
# Conversation Starter Section
# -----------------------------

event = st.text_area("Event Description")
interests = st.text_input("Your Interests")

if st.button("Generate"):

    save_history(event, interests)

    starters = generate_starters(event, interests)

    st.subheader("Conversation Starters")

    for starter in starters:
        st.write("•", starter)

# -----------------------------
# Conversation History
# -----------------------------

st.subheader("📜 Conversation History")

with open("data/history.json", "r") as file:
    history = json.load(file)

for item in history:
    st.write(f"**Event:** {item['event']}")
    st.write(f"**Interests:** {item['interests']}")
    st.write("---")

# -----------------------------
# Wikipedia Fact Checker
# -----------------------------

st.subheader("📚 Wikipedia Fact Checker")

topic = st.text_input("Enter a topic")

if st.button("Fact Check"):
    result = fact_check(topic)
    st.write(result)