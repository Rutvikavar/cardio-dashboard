import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

# -----------------------
# Page Config
# -----------------------
st.set_page_config(
    page_title="Cardio Health Dashboard",
    page_icon="❤️",
    layout="wide"
)

# -----------------------
# Custom Dark + Glass CSS
# -----------------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f172a, #0a192f);
}

.main {
    background-color: transparent;
}

.glass-card {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(15px);
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 0 20px rgba(0,255,150,0.1);
}

.metric-title {
    font-size: 14px;
    color: #9CA3AF;
}

.metric-value {
    font-size: 28px;
    font-weight: bold;
    color: #00ffcc;
}

.section-title {
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 10px;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# -----------------------
# Dummy Cardio Data
# -----------------------
heart_rate = np.random.normal(75, 5, 24)
steps = 7166
spo2 = 98
stress = 32
cardio_score = 8.7
calories = 1850
hydration = 2.4

# -----------------------
# Navbar
# -----------------------
col1, col2 = st.columns([6, 2])
with col1:
    st.markdown("<h2 style='color:white;'>Cardio Health Dashboard</h2>", unsafe_allow_html=True)

with col2:
    st.text_input("Search")
    st.markdown("👤 Rutu")

st.markdown("---")

# -----------------------
# Hero Metrics Section
# -----------------------
col1, col2, col3, col4 = st.columns(4)

metrics = [
    ("Heart Rate", f"{int(heart_rate[-1])} BPM"),
    ("Cardio Score", f"{cardio_score}/10"),
    ("Oxygen Level", f"{spo2}%"),
    ("Stress Level", f"{stress}%")
]

for col, (title, value) in zip([col1, col2, col3, col4], metrics):
    with col:
        st.markdown(f"""
        <div class="glass-card">
            <div class="metric-title">{title}</div>
            <div class="metric-value">{value}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("")

# -----------------------
# Heart Rate Trend Graph
# -----------------------
st.markdown('<div class="section-title">Heart Rate Trend</div>', unsafe_allow_html=True)

df = pd.DataFrame({
    "Hour": list(range(24)),
    "Heart Rate": heart_rate
})

fig = px.line(
    df,
    x="Hour",
    y="Heart Rate",
    markers=True,
)

fig.update_layout(
    template="plotly_dark",
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font_color="white"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------
# Lower Sections
# -----------------------
col1, col2 = st.columns(2)

# Step Counter Card
with col1:
    st.markdown('<div class="section-title">Step Counter</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="glass-card">
        <div class="metric-value">{steps}</div>
        <div class="metric-title">Steps Today</div>
    </div>
    """, unsafe_allow_html=True)

# Weekly Sessions
with col2:
    st.markdown('<div class="section-title">Weekly Cardio Sessions</div>', unsafe_allow_html=True)

    session_data = pd.DataFrame({
        "Session": ["Running", "Cycling", "HIIT"],
        "Duration (mins)": [120, 90, 60]
    })

    fig2 = px.bar(session_data, x="Session", y="Duration (mins)")
    fig2.update_layout(
        template="plotly_dark",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="white"
    )

    st.plotly_chart(fig2, use_container_width=True)

# -----------------------
# Sleep & Nutrition
# -----------------------
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="section-title">Sleep & Recovery</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="glass-card">
        Deep Sleep: 72% <br>
        REM: 28% <br>
        Recovery Score: 85%
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown('<div class="section-title">Nutrition Summary</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="glass-card">
        Calories: {calories} kcal <br>
        Hydration: {hydration} L <br>
        Protein: 110g
    </div>
    """, unsafe_allow_html=True)

# -----------------------
# Achievements
# -----------------------
st.markdown('<div class="section-title">Achievements & Goals</div>', unsafe_allow_html=True)
st.progress(0.7, text="Weekly Cardio Goal 70% Complete")
st.progress(0.5, text="Hydration Goal 50% Complete")