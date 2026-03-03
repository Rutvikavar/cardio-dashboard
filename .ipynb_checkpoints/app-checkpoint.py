import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Cardio Health Analytics",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Professional Dark Theme CSS
# -----------------------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f172a, #0a192f);
}

.block-container {
    padding-top: 2rem;
}

.glass {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(12px);
    border-radius: 18px;
    padding: 20px;
    box-shadow: 0 4px 30px rgba(0,0,0,0.3);
}

.metric-title {
    font-size: 14px;
    color: #9CA3AF;
}

.metric-value {
    font-size: 30px;
    font-weight: bold;
    color: #00FFC6;
}

.section-title {
    font-size: 22px;
    font-weight: 600;
    margin-bottom: 15px;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Sidebar Controls
# -----------------------------
st.sidebar.title("User Settings")
selected_user = st.sidebar.selectbox("Select User", ["Rutu", "Guest"])
days = st.sidebar.slider("Select Days of Data", 7, 30, 24)

st.sidebar.markdown("---")
st.sidebar.info("Live Health Monitoring Dashboard")

# -----------------------------
# Dummy Data Generation
# -----------------------------
np.random.seed(42)
heart_rate = np.random.normal(75, 5, days)
steps = np.random.randint(6000, 12000)
spo2 = np.random.randint(95, 100)
stress = np.random.randint(20, 50)
cardio_score = round(np.random.uniform(7.5, 9.5), 1)
calories = np.random.randint(1600, 2400)
hydration = round(np.random.uniform(1.8, 3.5), 1)

# -----------------------------
# Header
# -----------------------------
st.title("❤️ Cardio Health Analytics Dashboard")
st.caption(f"Last Updated: {datetime.now().strftime('%d %B %Y, %H:%M:%S')}")

st.markdown("---")

# -----------------------------
# KPI Section
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

kpis = [
    ("Heart Rate", f"{int(heart_rate[-1])} BPM"),
    ("Cardio Score", f"{cardio_score}/10"),
    ("Oxygen Level", f"{spo2}%"),
    ("Stress Level", f"{stress}%")
]

for col, (title, value) in zip([col1, col2, col3, col4], kpis):
    with col:
        st.markdown(f"""
        <div class="glass">
            <div class="metric-title">{title}</div>
            <div class="metric-value">{value}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("")

# -----------------------------
# Heart Rate Trend
# -----------------------------
st.markdown('<div class="section-title">Heart Rate Trend</div>', unsafe_allow_html=True)

df = pd.DataFrame({
    "Day": list(range(1, days+1)),
    "Heart Rate": heart_rate
})

fig = px.line(df, x="Day", y="Heart Rate", markers=True)
fig.update_layout(
    template="plotly_dark",
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font_color="white"
)

st.plotly_chart(fig, width='stretch')

# -----------------------------
# Activity & Sessions
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="section-title">Daily Steps</div>', unsafe_allow_html=True)
    st.metric("Steps Today", steps)

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

    st.plotly_chart(fig2, width='stretch')

# -----------------------------
# Wellness Section
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="section-title">Sleep & Recovery</div>', unsafe_allow_html=True)
    st.metric("Recovery Score", "85%")
    st.progress(0.85)

with col2:
    st.markdown('<div class="section-title">Nutrition Summary</div>', unsafe_allow_html=True)
    st.metric("Calories", f"{calories} kcal")
    st.metric("Hydration", f"{hydration} L")

# -----------------------------
# Goals
# -----------------------------
st.markdown('<div class="section-title">Goals Progress</div>', unsafe_allow_html=True)
st.progress(0.7, text="Cardio Goal - 70%")
st.progress(0.5, text="Hydration Goal - 50%")

st.success("System Status: All health metrics stable ✅")