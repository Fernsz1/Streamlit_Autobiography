import streamlit as st
import pandas as pd
from datetime import datetime

# ---------------------------------------------
# Sidebar Navigation
# ---------------------------------------------

# Sidebar Profile

st.set_page_config(layout="wide")

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

    st.markdown("---")

    st.subheader("📈 My Analytical Impact")

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

    st.subheader("🎓 Educational Background")

    st.markdown(
        """
        - **B.S. in Computer Science (BSCS)**, Cebu Institute of Technology – University (2023 – Present) 
        - **Secondary Education**, University of Cebu – Main Campus (2021 – 2023)
        - **Primary Education**, Don Vicente Rama Memorial Elementary School (2013 – 2021)
        """
    )

    st.markdown("---")
    
    st.subheader("💻 Technical Skills & Expertise")
    st.write(
        """
        A comprehensive overview of my technical competencies. These reflect both academic experience and 
        hands-on project development, all organized by category.
        """
    )

    # --- REORGANIZED SKILLS INTO TABS ---
    tab1, tab2, tab3 = st.tabs(["🔹 Core Languages", "🛠️ Frameworks & Tools", "💡 Core Concepts"])

    with tab1:
        st.write("My proficiency in core programming languages, from low-level systems to high-level scripting.")
        langs = {
            "Python (Beginner)": 30,
            "Java / Kotlin (Advanced OOP & Mobile)": 85,
            "C++ (Intermediate Data Structures)": 65,
            "C (Low-Level Systems Programming)": 60,
            "GDScript (Intermediate Godot Game Development)": 70,
            "SQL (Database Querying & Optimization)": 70,
        }

        for l, p in langs.items():
            st.write(f"**{l}**")
            st.progress(p)

    with tab2:
        st.write("The ecosystem of tools, libraries, and frameworks I use to build and deploy applications.")
        
        st.write("#### 📱 Mobile & Game Development")
        st.markdown(
            """
            - **Android SDK / Studio**
            - **Godot (Basic 3D Development)**
            - **JavaFX (Desktop UI Development)**
            """
        )

        st.write("#### 🌐 Data & Web Development")
        st.markdown(
            """
            - **Streamlit (Interactive Web Dashboards)**
            - **Pandas / NumPy (Data Manipulation & Analysis)**
            - **Matplotlib / Seaborn (Data Visualization)**
            """
        )

        st.write("#### 🔧 Version Control / DevOps")
        st.markdown(
            """
            - **Git / GitHub (Proficient in Branching, PRs, Collaboration)**
            - **Docker (Basic Containerization & Environments)**
            - **JIRA / Agile (Team Workflow & Task Management)**
            """
        )

    with tab3:
        st.write("The fundamental computer science principles that guide my development practices.")
        st.markdown(
            """
            - **Object-Oriented Programming (OOP):** Strong command of abstraction, modular design, and clean architecture.
            - **Data Structures & Algorithms (DSA):** Solid understanding of lists, trees, graphs, hashing, and time complexity.
            - **Database Management:** Experience with SQL (MySQL) and basic NoSQL concepts (Firebase/MongoDB).
            - **Debugging & Testing:** Skilled in systematic debugging, error tracing, and writing unit tests for code reliability.
            """
        )

    st.markdown("---")
    st.markdown("### 📄 My Resume")

    # --- ADDED INTRODUCTORY TEXT HERE ---
    st.write(
        "For a more detailed breakdown of my qualifications, academic background, and professional experience, "
        "please feel free to view my full CV."
    )
    # ----------------------------------------
    
    st.markdown(
        "[Click here to view my CV on Google Docs](https://docs.google.com/document/d/1eac6Cdl-W84E6a_jSmyd88HoeMaatVd1/edit?usp=sharing)"
    )

# ---------------------------------------------
# PORTFOLIO
# ---------------------------------------------
elif page == "Portfolio":
    st.title("💼 My Portfolio")
    st.subheader("🚀 Projects")

    # PROJECT LIST
    # PROJECT LIST
    projects = [
        {
            "name": "CookingIna! Ang Sarap!",
            "images": [
                "https://i.imgur.com/ihpMuPz.jpeg",
                "https://i.imgur.com/z1JBoZf.jpeg",
            ],
            "description": "Step into a fast-paced 2D cooking simulation built with the **FXGL (JavaFX Game Engine) library**. "
                           "Players are challenged to manage time and resources effectively, "
                           "preparing and serving a variety of dishes against the clock to satisfy customers.",
        },
        {
            "name": "BALIKAW",
            "images": [
                "https://i.imgur.com/z2x1jFq.jpeg",
                "https://i.imgur.com/ntxkaPG.png",
            ],
            "description": "Immerse yourself in an atmospheric indie horror game with a unique Cebuano theme. "
                           "Developed in the **Godot Engine**, players must navigate a dark, old mansion, "
                           "solving intricate puzzles and uncovering clues to piece together the haunting narrative. "
                           "Play it here --> https://sahoooo.itch.io/balikaw",
        },
        {
            "name": "MatchIt Mania!",
            "images": [
                "https://i.imgur.com/LDmL3je.jpeg",
                "https://i.imgur.com/YTijnY9.jpeg",
            ],
            "description": "A vibrant and addictive match-3 puzzle game designed for mobile. "
                           "Players swap adjacent tiles to create matches, unleashing powerful boosters "
                           "and tackling increasingly challenging levels that test strategic thinking.",
        },
        {
            "name": "EXPy",
            "images": [
                "https://i.imgur.com/Ypk95tg.jpeg",
                "https://i.imgur.com/f8OarSh.jpeg",
            ],
            "description": "A gamified solo learning application to make Python programming accessible and engaging. "
                           "This app helps users learn via interactive lessons, quizzes, and coding challenges. "
                           "Key features include an XP system, a competitive leaderboard, and a 'learning streak' tracker to motivate users.",
        },
        {
            "name": "Jubuddy",
            "images": [
                "https://i.imgur.com/K7TwAK7.jpeg",
                "https://i.imgur.com/aWslnFZ.jpeg",
            ],
            "description": "A smart budget planner app with a unique social twist. "
                           "While it helps users track expenses and set savings goals, its core feature allows you "
                           "to invite a 'Buddy' to view each other's progress, providing shared motivation and accountability.",
        }
    ]

    # DISPLAY PROJECTS
    # DISPLAY PROJECTS
    for project in projects:
        colA, colB = st.columns(2)
            
        # --- THIS WILL AUTOMATICALLY SCALE THE IMAGES ---
        colA.image(project["images"][0], use_column_width='always')
        colB.image(project["images"][1], use_column_width='always')
        # ------------------------------------------------

        # Description placeholder
       
        st.write("###  " + project["name"])
        st.write(project["description"])
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

    st.markdown("---")

    st.subheader("🌍 Socials")
    
    st.write(
        "Feel free to check out my profiles and connect with me on other platforms:"
    )

    col1, col2, col3 = st.columns(3)
    
    # --- ADDED EMOJIS TO YOUR LINKS ---
    col1.markdown("[GitHub 🐙](https://github.com/Fernsz1)")
    col2.markdown("[LinkedIn 💼](https://www.linkedin.com/in/christian-luis-fernandez-051699383/)")
    col3.markdown("[Facebook 📘](https://www.facebook.com/christianluis.fernandez/)")
