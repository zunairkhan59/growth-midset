
import streamlit as st
from datetime import datetime

# Set page title and layout
st.set_page_config(page_title="Growth Mindset Challenge", layout="centered")

# Header
st.title("🌱 Growth Mindset Challenge")
st.subheader("Believe in your ability to learn and grow!")

# Introduction
st.markdown("""
A **growth mindset** means believing that your abilities can be developed through dedication, hard work, and learning from mistakes.

This app will help you reflect and practice the key habits of a growth mindset.
""")

# Growth Mindset Pillars
st.header("🚀 Why Adopt a Growth Mindset?")
st.markdown("""
- **Embrace Challenges:** Every obstacle is a learning opportunity.
- **Learn from Mistakes:** Mistakes are steps toward success.
- **Persist Through Difficulties:** Keep going even when it's tough.
- **Celebrate Effort:** Value your journey, not just the destination.
- **Keep an Open Mind:** Stay curious and adapt.
""")

# Daily Reflection Form
st.header("🧠 Reflect on Your Learning")
with st.form("reflection_form"):
    name = st.text_input("Your Name")
    goal = st.text_input("What skill are you working on?")
    challenge = st.text_area("Describe a recent challenge you faced:")
    learning = st.text_area("What did you learn from it?")
    submitted = st.form_submit_button("Submit Reflection")

    if submitted:
        st.success(f"Thank you, {name}! Keep growing! 🌟")
        with open("reflections.txt", "a") as f:
            f.write(f"{datetime.now()} - {name}: Goal: {goal}, Challenge: {challenge}, Learning: {learning}\n")

# Motivation Section
st.header("🌟 Daily Motivation")
st.info("“It’s not that I’m so smart, it’s just that I stay with problems longer.” – Albert Einstein")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit to encourage a growth mindset.")

