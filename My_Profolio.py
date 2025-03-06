import streamlit as st
from streamlit_option_menu import option_menu
import plotly.graph_objects as go
import smtplib
from email.message import EmailMessage

# Page configuration
st.set_page_config(
    page_title="My Digital Footprint",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Theme configuration
def apply_theme_css(theme):
    if theme == "Dark":
        st.markdown("""
        <style>
        :root {
            --primary-color: #2ecc71;
            --background-color: #1a1a1a;
            --text-color: #eaeaea;
            --card-bg: #2d2d2d;
            --code-bg: #3a3a3a;
        }
        .stApp {
            background-color: var(--background-color) !important;
            color: var(--text-color) !important;
        }
        .stMarkdown, .stCodeBlock {
            color: var(--text-color) !important;
        }
        .css-1d391kg {
            background-color: var(--card-bg) !important;
        }
        .st-bd {
            background-color: var(--code-bg) !important;
        }
        .st-cq {
            background-color: var(--card-bg) !important;
        }
        .project-card {
            background: var(--card-bg) !important;
            border: 1px solid #4a4a4a !important;
            color: var(--text-color) !important;
        }
        .testimonial {
            background: var(--card-bg) !important;
            border-left: 4px solid var(--primary-color) !important;
            color: var(--text-color) !important;
        }
        .contact-form {
            background: var(--card-bg) !important;
            padding: 20px !important;
            border-radius: 10px !important;
        }
        input, textarea {
            background: var(--code-bg) !important;
            color: var(--text-color) !important;
            border: 1px solid #4a4a4a !important;
        }
        </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <style>
        :root {
            --primary-color: #4CAF50;
            --background-color: #ffffff;
            --text-color: #333333;
            --card-bg: #f5f5f5;
            --code-bg: #eaeaea;
        }
        .stApp {
            background-color: var(--background-color) !important;
            color: var(--text-color) !important;
        }
        .stMarkdown, .stCodeBlock {
            color: var(--text-color) !important;
        }
        .css-1d391kg {
            background-color: var(--card-bg) !important;
        }
        .st-bd {
            background-color: var(--code-bg) !important;
        }
        .st-cq {
            background-color: var(--card-bg) !important;
        }
        .project-card {
            background: var(--card-bg) !important;
            border: 1px solid #dddddd !important;
            color: var(--text-color) !important;
        }
        .testimonial {
            background: var(--card-bg) !important;
            border-left: 4px solid var(--primary-color) !important;
            color: var(--text-color) !important;
        }
        .contact-form {
            background: var(--card-bg) !important;
            padding: 20px !important;
            border-radius: 10px !important;
        }
        input, textarea {
            background: var(--code-bg) !important;
            color: var(--text-color) !important;
            border: 1px solid #dddddd !important;
        }
        </style>
        """, unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    selected = option_menu(
        "Navigation",
        ["Home", "Projects", "Skills", "Timeline", "Contact"],
        icons=['house', 'book', 'bar-chart', 'clock', 'envelope'],
        menu_icon="cast",
        default_index=0
    )
    st.markdown("---")
    theme = st.radio("Theme", ["Dark", "Light"], index=0)
    apply_theme_css(theme)

# Home Section
if selected == "Home":
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("profile_pic.jpg", width=150)
    with col2:
        st.markdown(f'<h1 style="color: var(--primary-color);">Juma Filberto George Andrea</h1>', unsafe_allow_html=True)
        st.markdown('<div style="color: var(--text-color);">Computer Science Student | Software Engineer</div>', unsafe_allow_html=True)
        st.markdown('<div style="color: var(--text-color);">📍 Ruhengeri, Rwanda</div>', unsafe_allow_html=True)
        st.markdown('<div style="color: var(--text-color);">🎓 INES Ruhengeri - Computer Science</div>', unsafe_allow_html=True)
        with open("resume.pdf", "rb") as pdf_file:
            st.download_button("📄 Download Resume", data=pdf_file.read(), file_name="Juma_Resume.pdf")

    st.markdown("## About Me")
    st.markdown('<div style="color: var(--text-color);">Passionate about leveraging technology to solve real-world problems. '
                'Experienced in full-stack development and machine learning projects. '
                'Always eager to collaborate on innovative solutions.</div>', unsafe_allow_html=True)

# Projects Section
elif selected == "Projects":
    st.title("My Projects")
    project_types = ["All", "Individual", "Group", "Dissertation"]
    selected_type = st.selectbox("Filter by Type", project_types)

    projects = [
        {
            "title": "Visit Rwanda Tourism Site",
            "type": "Group",
            "description": "A tourism site to experience different tourism locations and recommendations",
            "code": "https://github.com/your-repo",
            "image": "https://via.placeholder.com/150"
        },
        {
            "title": "Library Management System",
            "type": "Individual",
            "description": "A library management system to manage borrows, books, and fine calculations for overdue books",
            "code": "https://github.com/your-repo",
            "image": "https://via.placeholder.com/150"
        },
        {
            "title": "Agrishield - AI Crop Disease Detection",
            "type": "Dissertation",
            "description": "AI-based crop analyzer to detect diseases and suggest remedies for smallholder farmers",
            "code": "https://github.com/your-repo",
            "image": "https://via.placeholder.com/150"
        }
    ]

    filtered_projects = [p for p in projects if selected_type == "All" or p["type"] == selected_type]
    for project in filtered_projects:
        st.markdown(f"""
        <div class="project-card">
            <h3>{project['title']}</h3>
            <p>Type: {project['type']}</p>
            <p>{project['description']}</p>
            <a href="{project['code']}">View Code</a>
        </div>
        """, unsafe_allow_html=True)

# Skills Section
elif selected == "Skills":
    st.title("Technical Skills")
    skills = {
        "Python": 90,
        "JavaScript": 75,
        "Machine Learning": 85,
        "SQL": 80,
        "Cloud Computing": 70
    }

    for skill, level in skills.items():
        st.markdown(f"**{skill}**")
        st.progress(level / 100, text=f"{level}%")

    st.title("Certifications")
    st.markdown("""
    <div style="display: flex; gap: 15px; flex-wrap: wrap; color: var(--text-color);">
        <img src="https://dummyimage.com/100x100/000/fff.png&text=Java+SoloLearn" 
             style="background: var(--code-bg); padding: 5px; border-radius: 5px;">
        <img src="https://dummyimage.com/100x100/000/fff.png&text=Python+SoloLearn" 
             style="background: var(--code-bg); padding: 5px; border-radius: 5px;">
    </div>
    """, unsafe_allow_html=True)

# Timeline Section
elif selected == "Timeline":
    st.title("My Journey")
    milestones = [
        {"date": "2022", "event": "Started Computer Science Degree"},
        {"date": "2021", "event": "Learned programming languages"},
        {"date": "2025", "event": "Published Research Paper"},
        {"date": "2023", "event": "Completed Internship at Ikugugu Company"}
    ]

    axis_color = "#ffffff" if theme == "Dark" else "#000000"
    paper_bgcolor = 'rgba(0,0,0,0)' if theme == "Dark" else 'rgba(255,255,255,1)'

    fig = go.Figure(go.Scatter(
        x=[m['date'] for m in milestones],
        y=[1] * len(milestones),
        mode='markers+text',
        text=[m['event'] for m in milestones],
        textposition="bottom center",
        marker=dict(size=15, color="#2ecc71"),
        textfont=dict(color=axis_color),
        showlegend=False
    ))

    fig.update_layout(
        title="Academic & Professional Milestones",
        xaxis=dict(
            showgrid=False,
            showline=True,
            linecolor=axis_color,
            tickfont=dict(color=axis_color),
            tickvals=[m['date'] for m in milestones]
        ),
        yaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
        height=400,
        plot_bgcolor=paper_bgcolor,
        paper_bgcolor=paper_bgcolor,
        font=dict(color=axis_color)
    )

    st.plotly_chart(fig, use_container_width=True)

    st.title("Testimonials")
    testimonials = [
        {"name": "Sameh Sederia", "quote": "He is a very creative individual with technical skills"},
        {"name": "Ujama Surur", "quote": "Interactive and good team player"}
    ]

    cols = st.columns(2)
    for i, testimonial in enumerate(testimonials):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="testimonial">
                <p>"{testimonial['quote']}"</p>
                <strong>- {testimonial['name']}</strong>
            </div>
            """, unsafe_allow_html=True)

# Contact Section
elif selected == "Contact":
    st.title("Let's Connect!")

    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Name", key="name")
        email = st.text_input("Email", key="email")
        subject = st.text_input("Subject", key="subject")
        message = st.text_area("Message", key="message")
        submitted = st.form_submit_button("Send")

        if submitted:
            try:
                msg = EmailMessage()
                msg["From"] = email
                msg["To"] = st.secrets["email"]["username"]
                msg["Subject"] = subject
                msg.set_content(f"Name: {name}\nEmail: {email}\n\n{message}")

                with smtplib.SMTP(st.secrets["email"]["smtp_server"], st.secrets["email"]["port"]) as server:
                    server.starttls()
                    server.login(st.secrets["email"]["username"], st.secrets["email"]["password"])
                    server.send_message(msg)
                st.success("Message sent successfully!")
            except Exception as e:
                st.error(f"Failed to send message: {str(e)}")

    st.markdown("""
      <div style="margin-top: 20px;">
        <a href="https://snapchat.com" target="_blank">
            <img src="https://camo.githubusercontent.com/ef26b5ea4908f7fb3f1697e2fc5f440f1562d92de3adc7bba20839c69570cd2d/68747470733a2f2f6564656e742e6769746875622e696f2f537570657254696e7949636f6e732f696d616765732f7376672f736e6170636861742e737667" width="40" style="margin: 0 10px;"/>
        </a>
        <a href="https://github.com/Darth-Vader-Dark" target="_blank">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" width="40" style="margin: 0 10px;"/>
        </a>
        <a href="mailto:filbertogeorge@gmail.com">
            <img src="https://camo.githubusercontent.com/7f7b46dc6de3f79de9b7f5134096433206eb80e7e84b948e67f55f496cf799f4/68747470733a2f2f6564656e742e6769746875622e696f2f537570657254696e7949636f6e732f696d616765732f7376672f676d61696c5f6f6c642e737667" width="40" style="margin: 0 10px;"/>
        </a>
    </div>
    """, unsafe_allow_html=True)