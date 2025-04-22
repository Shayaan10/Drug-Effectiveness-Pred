import streamlit as st
import joblib

# ----------------- Page Config -----------------
st.set_page_config(
    page_title="Drug Effectiveness Predictor",
    page_icon="💊",
    layout="centered"
)

# ----------------- Dark Theme Background -----------------
def set_background():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://images.unsplash.com/photo-1605902711622-cfb43c4437d2?ixlib=rb-4.0.3&auto=format&fit=crop&w=1950&q=80");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: #ffffff;
        }}
        .css-18e3th9 {{
            background-color: rgba(0, 0, 0, 0.6);
            padding: 2rem;
            border-radius: 12px;
        }}
        .stButton>button {{
            background-color: #00ffff;
            color: black;
            font-weight: bold;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background()

# ----------------- Model Loading -----------------
model = joblib.load("drug_model.pkl")

# ----------------- Header -----------------
st.markdown("<h1 style='text-align: center; color: #00ffff;'>💊 Drug Effectiveness Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #cccccc;'>Enter the patient's health details to predict drug effectiveness.</p>", unsafe_allow_html=True)

# ----------------- Input Section -----------------
st.markdown("### 🔍 Patient Health Data")

col1, col2 = st.columns(2)
with col1:
    a1 = st.number_input("👤 Age", min_value=1, max_value=120, value=30)
    a2 = st.number_input("💉 Blood Pressure (mmHg)", min_value=50, max_value=200, value=120)
    a3 = st.number_input("🩸 Cholesterol Level (mg/dL)", min_value=100, max_value=400, value=200)
with col2:
    a4 = st.number_input("❤️ Heart Rate (bpm)", min_value=30, max_value=200, value=70)
    a5 = st.number_input("📏 BMI", min_value=10.0, max_value=50.0, value=22.0)

# ----------------- Prediction -----------------
if st.button("Predict"):
    prediction = model.predict([[a1, a2, a3, a4, a5]])[0]
    if prediction == 1:
        st.success("✅ The drug is likely **Effective** for this patient.")
    else:
        st.error("❌ The drug is likely **Not Effective** for this patient.")
