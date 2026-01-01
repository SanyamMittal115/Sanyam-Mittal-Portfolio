import streamlit as st
import os

# Get the folder where app.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
resume_path = os.path.join(BASE_DIR, "Sanyam(Sunny) Mittal Resume.pdf")
# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Sanyam(Sunny) Mittal | Portfolio",
    page_icon="✨",
    layout="wide"
)

# ---------------- Dark Mode Toggle ----------------
if "dark" not in st.session_state:
    st.session_state.dark = False

toggle_col, _ = st.columns([1, 10])
with toggle_col:
    # Select slider with Light/Dark labels
    mode = st.select_slider(
        "Theme",
        options=["Light", "Dark"],
        value="Dark" if st.session_state.dark else "Light"
    )
    st.session_state.dark = mode == "Dark"

# ---------------- THEME COLORS ----------------
if st.session_state.dark:
    bg = "#0f172a"
    card = "#020617"
    text = "#e5e7eb"
    subtext = "#9ca3af"
else:
    bg = "#ffffff"
    card = "#ffffff"
    text = "#020617"
    subtext = "#6b7280"

# ---------------- Global CSS ----------------
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

/* Full page background */
body, .stApp, [class*="css"], .main {{
    background-color: {bg} !important;
    color: {text} !important;
}}

html {{
    scroll-behavior: smooth;
}}

a {{
    text-decoration: none;
}}

.nav {{
    position: sticky;
    top: 0;
    background: {bg};
    padding: 12px 0;
    z-index: 999;
    border-bottom: 1px solid #e5e7eb22;
    text-align: center;
}}

.nav a {{
    margin: 0 18px;
    font-weight: 600;
    color: {text};
    cursor: pointer;
}}

.hero {{
    padding: 90px 0 60px 0;
    text-align: center;
}}

.gradient-text {{
    background: linear-gradient(90deg, #7c3aed, #2563eb);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 3.5rem;
    font-weight: 700;
}}

.subtitle {{
    font-size: 1.3rem;
    color: {subtext};
    margin-top: 10px;
}}

.section {{
    margin-top: 90px;
}}

.card {{
    background: {card};
    border-radius: 18px;
    padding: 26px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.08);
    transition: transform 0.2s ease;
}}

.card:hover {{
    transform: translateY(-6px);
}}

.tag {{
    display: inline-block;
    background: #64748b22;
    border-radius: 999px;
    padding: 6px 14px;
    margin: 6px 6px 0 0;
    font-size: 0.9rem;
}}
</style>

<script>
// Smooth scroll for navbar links
document.querySelectorAll('.nav a').forEach(anchor => {{
    anchor.addEventListener('click', function (e) {{
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({{
            behavior: 'smooth'
        }});
    }});
}});
</script>
""", unsafe_allow_html=True)

# ---------------- NAVBAR ----------------
st.markdown("""
<div class="nav">
    <a href="#about">About</a>
    <a href="#education">Education</a>
    <a href="#skills">Skills</a>
    <a href="#projects">Projects</a>
    <a href="#resume">Resume</a>
    <a href="#contact">Contact</a>
</div>
""", unsafe_allow_html=True)

# ---------------- HERO ----------------
st.markdown("""
<div class="hero">
    <div class="gradient-text">Sanyam(Sunny) Mittal</div>
    <div class="subtitle">
        AI Strategist • Public Speaker • Student
    </div>
    <p class="subtitle">
        I built the AI so your product launches smarter.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------- ABOUT ----------------
st.markdown('<div id="about" class="section"></div>', unsafe_allow_html=True)
st.header("About")

left, right = st.columns([2, 1])
with left:
    st.markdown("""
    <div class="card">
        Hello, I’m Sanyam (Sunny) Mittal, an AI strategist and public speaker specializing in
        the design and analysis of coding projects that turn ideas into forward-looking innovations.
        Combining Python expertise with leadership and management experience, I improve
        pre-existing solutions while developing new AI products aligned with real consumer needs.
    </div>
    """, unsafe_allow_html=True)

with right:
    st.markdown("""
    <div class="card">
        📍 Atlanta, GA <br><br>
        💼 Aspiring SolEng/ PM/ AI<br><br>
        🌱 Always learning
    </div>
    """, unsafe_allow_html=True)

# ---------------- EDUCATION ----------------
st.markdown('<div id="education" class="section"></div>', unsafe_allow_html=True)
st.header("Education")

st.markdown("""
<div class="card">
    <b>Georgia Institute of Technology</b><br>
    B.S. in Business Administration (BSBA)<br>
    Concentration: Information Technology Management/ Minor: Information Systems and Computing <br><br>
    📅 2025 – present<br>
    📚 Relevant Coursework: Intro to Computing: Python, Accounting 1, Management Statistics
</div>
""", unsafe_allow_html=True)

# ---------------- SKILLS ----------------
st.markdown('<div id="skills" class="section"></div>', unsafe_allow_html=True)
st.header("Skills")

st.markdown("""
<div class="card">
    <span class="tag">Python</span>
    <span class="tag">Streamlit</span>
    <span class="tag">Excel</span>
    <span class="tag">Huggingface</span>
    <span class="tag">SQL</span>
    <span class="tag">Bilingual</span>
    <span class="tag">AI / ML</span>
</div>
""", unsafe_allow_html=True)

# ---------------- PROJECTS ----------------
st.markdown('<div id="projects" class="section"></div>', unsafe_allow_html=True)
st.header("Projects")

c1, c2, c3 = st.columns(3)
projects = [
    ("Calorie Tracker", "A calorie tracker using streamlit + python which shows my ability to merge csv and json data with streamlit functions", "https://sanyam-mittal-calorie-tracker-2jmyqcfqhah2qkmzribyez.streamlit.app/"),
    ("Videogame Analytics Engine", "An API based tool that can be used to play games, get game support and get recommendations through Gemini and Chatgpt", "https://sanyam-mittal-videogame-support-ggcjozgxpqenzavhthd9ug.streamlit.app/"),
    ("Resume Analysis Tool", "A Huggingface AI tool/ agent that analyzes my own resume through classification, summarization and NER based models to determine job fit", "https://huggingface.co/spaces/Sunny115/resume_analysis_tool"),
]

for col, p in zip([c1, c2, c3], projects):
    with col:
        st.markdown(f"""
        <div class="card">
            <h4>{p[0]}</h4>
            <p>{p[1]}</p>
            <a href="{p[2]}" target="_blank">View →</a>
        </div>
        """, unsafe_allow_html=True)

# ---------------- RESUME ----------------
st.markdown('<div id="resume" class="section"></div>', unsafe_allow_html=True)
st.header("Resume")

st.markdown(f"""
<style>
div.stDownloadButton > button {{
    color: {text} !important;
    background-color: {card};
    border-radius: 12px;
    font-weight: 600;
}}
</style>
""", unsafe_allow_html=True)
if os.path.exists(resume_path):
    with open(resume_path, "rb") as f:
        st.download_button(
            "📄 Download Resume",
            f,
            file_name="Sanyam(Sunny) Mittal Resume.pdf"
        )
else:
    st.error(f"Resume not found at {resume_path}")
    

# ---------------- CONTACT ----------------
st.markdown('<div id="contact" class="section"></div>', unsafe_allow_html=True)
st.header("Contact")

st.markdown("""
<div class="card">
    🎓 smittal303@gatech.edu<br>
    📧 mittal.sanyam115@gmail.com<br>
    💼 <a href="www.linkedin.com/in/sanyam-mittal-sunny115" target="_blank">LinkedIn</a><br>
    🐙 <a href="https://github.com/SanyamMittal115" target="_blank">GitHub</a>
</div>
""", unsafe_allow_html=True)