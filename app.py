import streamlit as st
import pandas as pd
from datetime import datetime

# ---------------------------------------------
# Sidebar Navigation
# ---------------------------------------------

# Sidebar Profile
st.sidebar.markdown(
    """
    <style>
        /* Fix sidebar width so it cannot be resized */
        [data-testid="stSidebar"] {
            min-width: 300px;
            max-width: 300px;
        }

        /* Center alignment for sidebar */
        .sidebar .sidebar-content {
            text-align: center;
        }

        /* Bigger rounded profile picture */
        .profile-pic {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 200px;     /* bigger size */
            height: 200px;    /* bigger size */
            border-radius: 50%;
            object-fit: cover;
            border: 4px solid #4CAF50;
            box-shadow: 0px 0px 12px rgba(0,0,0,0.35);
            margin-top: 15px;
        }

        .sidebar-name {
            font-size: 22px;
            font-weight: bold;
            margin-top: 12px;
            text-align: center;
        }

        .sidebar-role {
            font-size: 14px;
            color: #cccccc;
            margin-bottom: 25px;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar Profile Section
st.sidebar.markdown(
    f"""
    <img src="https://i.imgur.com/oS4rwXF.jpeg" class="profile-pic">
    <div class="sidebar-name">Christian Luis C. Fernandez</div>
    <div class="sidebar-role">Game Developer • Designer • Prompt Engineer • Data Analyst</div>
    """,
    unsafe_allow_html=True
)

# Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to:", ["About Me", "Portfolio", "Contact"])
# ---------------------------------------------
# ABOUT ME
# ---------------------------------------------
if page == "About Me":
    st.title("👤 About Me")
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
    st.subheader("🚀 Projects")

    # PROJECT LIST
    projects = [
        {
            "name": "CookingIna! Ang Sarap!",
            "images": [
                "https://i.imgur.com/ihpMuPz.jpeg",
                "https://i.imgur.com/z1JBoZf.jpeg",
            ],
            "description": "2D Cooking Simulation Game developed using FXGL. Players can experience cooking various dishes while managing time and resources.",
        },
        {
            "name": "BALIKAW",
            "images": [
                "https://i.imgur.com/z2x1jFq.jpeg",
                "https://i.imgur.com/ntxkaPG.png",
            ],
            "description": "Indie Cebuano horror game developed in Godot Engine. Players navigate through an old mansion while solving puzzles to uncover the story. Play it here --> https://sahoooo.itch.io/balikaw",
        },
        {
            "name": "MatchIt Mania!",
            "images": [
                "https://i.imgur.com/LDmL3je.jpeg",
                "https://i.imgur.com/YTijnY9.jpeg",
            ],
            "description": "Matching puzzle game where players swap adjacent tiles to create matches of three or more, featuring power-ups and challenging levels."
        },
        {
            "name": "EXPy",
            "images": [
                "https://i.imgur.com/Ypk95tg.jpeg",
                "https://i.imgur.com/f8OarSh.jpeg",
            ],
            "description": "A python solo learining application that helps users learn Python programming through interactive lessons and quizzes."
        },
        {
            "name": "Jubuddy",
            "images": [
                "https://i.imgur.com/K7TwAK7.jpeg",
                "https://i.imgur.com/aWslnFZ.jpeg",
            ],
            "description": "Smart budget planner app that helps users track expenses, set savings goals, and manage finances effectively."
        }
    ]

    # DISPLAY PROJECTS
    for project in projects:
        colA, colB = st.columns(2)
            # Images
        colA.image(project["images"][0])
        colB.image(project["images"][1])

            # Description placeholder
        st.write("###  " + project["name"])
        st.write(project["description"])
        st.markdown("---")

        st.markdown("### 📄 My Resume")
        st.markdown("[Click here to view my CV on Google Docs](https://docs.google.com/document/d/1eac6Cdl-W84E6a_jSmyd88HoeMaatVd1/edit?usp=sharing)"
)


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
