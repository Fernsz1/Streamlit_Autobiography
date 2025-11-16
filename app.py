import streamlit as st
import pandas as pd
from datetime import datetime

# ---------------------------------------------
# Sidebar Navigation
# ---------------------------------------------
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to:", [ "About Me", "Portfolio", "Contact"])

# Sidebar Profile
st.sidebar.image("https://imgur.com/a/IVEHzVq", width=150)
st.sidebar.write("Christian Luis C. Fernandez")
st.sidebar.write("Game Developer • Designer • Prompt Engineer • Data Analyst")

# ---------------------------------------------
# ABOUT ME
# ---------------------------------------------
if page == "About Me":
    st.title("👤 About Me")

    st.image("https://imgur.com/a/IVEHzVq", width=250)

    st.header("📘 Autobiography")

    with st.expander("Read my story"):
        st.write(
            """
            Hello! I'm **Christian Luis C. Fernandez**, a Computer Science student with strong motivation in 
            technology, community involvement, event coordination, and collaborative work environments.

            Throughout my academic journey at Cebu Institute of Technology - University, I’ve gained 
            experience in communication, project coordination, leadership, documentation, and 
            productivity tools—skills strengthened through active participation in student organizations 
            such as the CIT-U Honor Society and the Computer Students Society.

            I enjoy learning new technologies, working with people, and contributing to meaningful projects that 
            help communities and organizations. I am adaptable, dedicated, and always eager to grow both 
            personally and professionally.
            """
        )

    st.subheader("My Analytical Impact")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.caption("Years Experience")
        st.metric("3+", "+1 year")

    with col2:
        st.caption("Projects Delivered")
        st.metric("14", "↑ 99% Success Rate")

    with col3:
        st.caption("Strong Competency")
        st.metric("Communication", "↑ Improved engagement")

    st.markdown("---")

    st.subheader("Educational Background")

    st.markdown(
        """
        - **B.S. in Computer Science (BSCS)**, Cebu Institute of Technology – University (2023 – Present)  
        - **Secondary Education**, University of Cebu – Main Campus (2021 – 2023) 
        - **Primary Education**, Don Vicente Rama Memorial Elementary School (2013 – 2021) 
        """
    )

    st.subheader("🎯 Skills")
    skills = {
        "Java": 50,
        "Python": 50,
        "Kotlin": 30,
        "PHP": 25,
        "HTML/CSS": 55,
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

    # -----------------------------------------
    # PROJECTS TAB
    # -----------------------------------------
    with tabs[0]:
        st.subheader("🚀 Projects")

        # PROJECT LIST
        projects = [
            {
                "name": "CookingIna! Ang Sarap!",
                "images": [
                    "https://imgur.com/a/qvecSTS",
                    "https://imgur.com/a/ba29rbA",
                ],
                "description": "2D Cooking Simulation Game developed using FXGL. Players can experience cooking various dishes while managing time and resources.",
            },
            {
                "name": "BALIKAW",
                "images": [
                    "https://imgur.com/a/qdBnYXo",
                    "https://imgur.com/a/vCD49Ys",
                ],
                "description": "Indie Cebuano horror game developed in Godot Engine. Players navigate through an old mansion while solving puzzles to uncover the story.",
            },
            {
                "name": "MatchIt Mania!",
                "images": [
                    "https://i.imgur.com/LDmL3je.jpeg",
                    "https://i.imgur.com/YTijnY9.jpeg",
                ],
                "description": "Matching puzzle game where players swap adjacent tiles to create matches of three or more, featuring power-ups and challenging levels."
            }
        ]

        # DISPLAY PROJECTS
        for project in projects:
            with st.expander(f"📌 {project['name']}"):
                colA, colB = st.columns(2)

                # Images
                colA.image(project["images"][0])
                colB.image(project["images"][1])

                # Description placeholder
                st.write("### 📝 Description")
                st.write(project["description"])

        st.markdown("---")

        st.markdown("### 📄 My Resume")
        st.markdown("[Click here to view my CV on Google Docs](https://docs.google.com/document/d/1eac6Cdl-W84E6a_jSmyd88HoeMaatVd1/edit?usp=sharing)"
)

# -----------------------------------------
# GALLERY TAB
# -----------------------------------------
with tabs[1]:
    st.subheader("🖼 Gallery")

    st.markdown("### 📄 My CV")
    st.markdown(
        "[Click here to view my CV on Google Docs](https://docs.google.com/document/d/1eac6Cdl-W84E6a_jSmyd88HoeMaatVd1/edit?usp=sharing)"
    )


    st.markdown("---")
    st.markdown("### 📚 Project Images")

    # PROJECT IMAGES (2 each)
    gallery_projects = [
        {
            "name": "CookingIna! Ang Sarap!",
            "images": [
                "https://via.placeholder.com/500x300?text=CookingIna+Image+1",
                "https://via.placeholder.com/500x300?text=CookingIna+Image+2",
            ]
        },
        {
            "name": "BALIKAW",
            "images": [
                "https://via.placeholder.com/500x300?text=BALIKAW+Image+1",
                "https://via.placeholder.com/500x300?text=BALIKAW+Image+2",
            ]
        },
        {
            "name": "EXPy",
            "images": [
                "https://via.placeholder.com/500x300?text=EXPy+Image+1",
                "https://via.placeholder.com/500x300?text=EXPy+Image+2",
            ]
        },
        {
            "name": "Jubuddy",
            "images": [
                "https://via.placeholder.com/500x300?text=Jubuddy+Image+1",
                "https://via.placeholder.com/500x300?text=Jubuddy+Image+2",
            ]
        },
        {
            "name": "MatchIt Mania!",
            "images": [
                "https://via.placeholder.com/500x300?text=MatchIt+Mania+Image+1",
                "https://via.placeholder.com/500x300?text=MatchIt+Mania+Image+2",
            ]
        }
    ]

    # DISPLAY IMAGES
    for proj in gallery_projects:
        st.markdown(f"#### {proj['name']}")
        col1, col2 = st.columns(2)
        col1.image(proj["images"][0])
        col2.image(proj["images"][1])
        st.markdown("---")


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
    col1.markdown("[GitHub](https://github.com/Fernsz1)")
    col2.markdown("[LinkedIn](https://www.linkedin.com/in/christian-luis-fernandez-051699383/)")
    col3.markdown("[Facebook](https://www.facebook.com/christianluis.fernandez/)")
