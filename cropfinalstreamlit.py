
import streamlit as st
import pandas as pd
import pickle

# --- Load Trained Model ---
with open(r"C:\Users\R.R. Dharun raagav\Desktop\Shanmuga priya projects Ml project\crop_production_model.pkl", "rb") as f:
    model = pickle.load(f)

# --- Load Encoded Column Structure ---
with open(r"C:\Users\R.R. Dharun raagav\Desktop\Shanmuga priya projects Ml project\final_encoded_dataset.pkl", "rb") as f:
    final_columns = pickle.load(f)

# --- Extract Options for Dropdowns from Encoded Column Names ---
areas = sorted([col.replace("Area_", "") for col in final_columns if col.startswith("Area_")])
items = sorted([col.replace("Item_", "") for col in final_columns if col.startswith("Item_")])
years = list(range(2026, 2101))  # Future prediction range

# --- Streamlit UI ---
st.set_page_config(page_title="Crop Production Predictor", page_icon="🌾")
st.title("🌾 Crop Production Prediction App")
st.markdown("Predict estimated **crop production (in tons)** for future years using a trained ML model.")

# --- User Inputs ---
area = st.selectbox("🌍 Select Country / Area", areas)
item = st.selectbox("🌽 Select Crop Type", items)
year = st.selectbox("📅 Select Year for Prediction", years)
area_harvested = st.number_input("📐 Area Harvested (in hectares)", min_value=0.0, step=100.0)
yield_ = st.number_input("🌿 Yield (kg per hectare)", min_value=0.0, step=100.0)

# --- Prepare Encoded Input ---
input_dict = {
    "Area harvested": area_harvested,
    "Yield": yield_,
    f"Year_{year}": 1,
    f"Area_{area}": 1,
    f"Item_{item}": 1
}

# Create a blank dataframe with all model columns filled as 0
input_encoded = pd.DataFrame(columns=final_columns)
input_encoded.loc[0] = 0  # Initialize all to 0

# Assign values from user input
for col in input_dict:
    if col in input_encoded.columns:
        input_encoded.at[0, col] = input_dict[col]

# --- Prediction ---
if st.button("🔮 Predict Production"):
    if input_encoded.sum().sum() == 0:
        st.error("⚠️ Invalid input. Please check the values selected.")
    else:
        prediction = model.predict(input_encoded)
        st.success(f"✅ Predicted Crop Production: **{prediction[0]:,.2f} tons**")
