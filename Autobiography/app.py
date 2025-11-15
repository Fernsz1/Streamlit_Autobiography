import streamlit as st
import pandas as pd
from datetime import datetime

# ---------------------------------------------
# Sidebar Navigation
# ---------------------------------------------
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to:", ["Home", "About Me", "Portfolio", "Contact"])

# Sidebar Profile
st.sidebar.image("https://i.imgur.com/1ZQZ1Zq.png", width=150)
st.sidebar.write("**Your Name**")
st.sidebar.write("Developer • Designer • Creator")

# ---------------------------------------------
# HOME
# ---------------------------------------------
if page == "Home":
    st.title("👋 Welcome to My Streamlit Portfolio!")
    st.write("This site is built using **Streamlit**, showcasing various components.")

    st.subheader("✨ Quick Overview")
    col1, col2, col3 = st.columns(3)
    col1.metric("Projects", 12)
    col2.metric("Years Experience", 3)
    col3.metric("Clients", 24)

    st.progress(70)

    st.subheader("🔥 Featured Video")
    st.video("https://www.youtube.com/watch?v=VqgUkExPvLY")

    st.subheader("📅 Today's Date")
    st.write(datetime.now().strftime("%B %d, %Y"))

# ---------------------------------------------
# ABOUT ME
# ---------------------------------------------
elif page == "About Me":
    st.title("👤 About Me")

    st.image("https://imgur.com/a/IVEHzVq", width=250)

    st.header("📘 Autobiography")
    with st.expander("Read my story"):
        st.write("""
        Hi! I'm **Your Name**, a passionate software developer based in the Philippines.
        I love building apps, game development, and creating interactive UI experiences.
        
        My journey began with simple projects but quickly grew into a career where I 
        explore web development, AI, and game design.
        """)

    st.subheader("🎯 Skills")
    skills = {
        "Python": 90,
        "JavaScript": 70,
        "C#": 85,
        "HTML/CSS": 95,
        "Game Dev (Godot/Unity)": 80,
    }

    for skill, percent in skills.items():
        st.write(f"**{skill}**")
        st.progress(percent)

# ---------------------------------------------
# PORTFOLIO
# ---------------------------------------------
elif page == "Portfolio":
    st.title("💼 My Portfolio")

    tabs = st.tabs(["Projects", "Gallery", "Experience"])

    # PROJECTS TAB
    with tabs[0]:
        st.subheader("🚀 Projects")
        project_data = pd.DataFrame({
            "Project Name": ["E-commerce App", "Game Prototype", "Portfolio Website", "AI Chatbot"],
            "Year": ["2024", "2023", "2025", "2025"],
            "Tech Used": ["Django", "Godot", "Streamlit", "Python"]
        })
        st.dataframe(project_data)

        st.write("Download my resume:")
        resume_text = "This is a sample resume text."
        st.download_button("📄 Download Resume", resume_text)

    # GALLERY TAB
    with tabs[1]:
        st.subheader("🖼 Gallery")
        col1, col2 = st.columns(2)
        col1.image("https://i.imgur.com/Z7AzH2C.png")
        col2.image("https://i.imgur.com/B85YQeW.jpeg")

    # EXPERIENCE TAB
    with tabs[2]:
        st.subheader("💼 Work Experience")
        st.write("""
        - **Software Developer** at XYZ Corp (2023–2025)  
        - **Freelance Web Developer** (2021–Present)  
        - **Game Developer** (Godot / Unity)
        """)

# ---------------------------------------------
# CONTACT
# ---------------------------------------------
elif page == "Contact":
    st.title("📬 Contact Me")

    name = st.text_input("Your Name")
    email = st.text_input("Email")
    message = st.text_area("Message")

    agree = st.checkbox("I agree to submit my information")

    if st.button("Submit Message"):
        if name and email and message and agree:
            st.success("Message sent successfully!")
        else:
            st.error("Please fill out all fields and agree to submit.")

    st.subheader("🌍 Socials")
    col1, col2, col3 = st.columns(3)
    col1.markdown("[GitHub](https://github.com/)")
    col2.markdown("[LinkedIn](https://www.linkedin.com/)")
    col3.markdown("[Facebook](https://facebook.com)")
