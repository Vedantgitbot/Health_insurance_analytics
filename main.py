import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.figure_factory as ff
from sklearn.preprocessing import StandardScaler

# Load model and scaler
model = joblib.load("insurance_model.pkl")
scaler = joblib.load("insurance_scaler.pkl")

# Region mapping
data = pd.read_csv("cleaned_insurance_data.csv")
region_map = {"Southwest": 0, "Southeast": 1, "Northwest": 2, "Northeast": 3}

# Function to predict charges
def predict_charges(age, bmi, children, sex, smoker, region):
    input_data = pd.DataFrame([[age, bmi, children, sex, smoker, region]],
                              columns=['Age', 'BMI', 'Children', 'Sex', 'Smoker', 'Region'])
    input_data_scaled = scaler.transform(input_data)
    predicted_charges = model.predict(input_data_scaled)
    return predicted_charges[0]

# Streamlit UI
st.set_page_config(page_title="Insurance Charges Prediction", layout="wide")

# Set background color to white
st.markdown(
    """
    <style>
        body {
            background-color: white !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Insurance Charges Prediction")

# Layout Setup
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Enter Details")
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
    children = st.number_input("Children", min_value=0, max_value=10, value=0)
    sex = st.selectbox("Sex", ["Male", "Female"], index=0)
    smoker = st.selectbox("Smoker", ["No", "Yes"], index=0)
    region_name = st.selectbox("Region", ["Southwest", "Southeast", "Northwest", "Northeast"])
    
    # Convert categorical inputs to numerical values
    sex = 0 if sex == "Male" else 1
    smoker = 0 if smoker == "No" else 1
    region = region_map[region_name]

    # Prediction Button
    if st.button("Predict Charges"):
        with st.spinner("Calculating..."):
            predicted_charges = predict_charges(age, bmi, children, sex, smoker, region)
        st.success(f"Predicted Insurance Charges: **${predicted_charges:.2f}**")

with col2:
    st.subheader("Data Visualizations")
    
    # Age Distribution
    fig_age = px.histogram(data, x="Age", marginal="box", nbins=30, color_discrete_sequence=["#636EFA"], title="Age Distribution")
    st.plotly_chart(fig_age, use_container_width=True)
    
    # BMI Distribution
    fig_bmi = px.histogram(data, x="BMI", marginal="box", nbins=30, color_discrete_sequence=["#EF553B"], title="BMI Distribution")
    st.plotly_chart(fig_bmi, use_container_width=True)
    
    # Insurance Charges Distribution
    fig_charges = px.histogram(data, x="Charges", marginal="box", nbins=30, color_discrete_sequence=["#00CC96"], title="Insurance Charges Distribution")
    st.plotly_chart(fig_charges, use_container_width=True)
    
    # Correlation Heatmap
    corr = data[['Age', 'BMI', 'Children', 'Sex', 'Smoker', 'Region', 'Charges']].corr()
    fig_corr = px.imshow(corr, text_auto=True, color_continuous_scale="Viridis", title="Feature Correlation Heatmap")
    st.plotly_chart(fig_corr, use_container_width=True)
