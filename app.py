import streamlit as st
from services.topic_generator import generate_starters

st.title("🤝 Personalized Networking Assistant")

st.write("Generate smart conversation starters for networking events.")

event = st.text_area("Event Description")

interests = st.text_input("Your Interests")

if st.button("Generate Conversation Starters"):

    starters = generate_starters(event, interests)

    st.subheader("Conversation Starters")

    for starter in starters:
        st.write("•", starter)