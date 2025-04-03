import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

# Load the trained model
model_path = r"C:\Users\R.R. Dharun raagav\Desktop\Shanmuga priya projects Ml project\crop_production_model.pkl"
with open(model_path, "rb") as file:
    model = pickle.load(file)

# Load dataset to extract unique states and crops
# Assuming the dataset was used for training, extract unique values
csv_path = r"C:\Users\R.R. Dharun raagav\Desktop\Shanmuga priya projects Ml project\Preprocessed_crop_production_data.csv"  # Ensure this CSV is available
try:
    df = pd.read_csv(csv_path)
    unique_areas = df["Area"].unique().tolist()
    unique_crops = df["Item"].unique().tolist()
    
    # Fit label encoders
    le_area = LabelEncoder()
    le_item = LabelEncoder()
    df["Area"] = le_area.fit_transform(df["Area"])
    df["Item"] = le_item.fit_transform(df["Item"])
    
except FileNotFoundError:
    st.error("Dataset file not found. Please ensure 'crop_data.csv' is available.")
    unique_areas = []
    unique_crops = []
    le_area = None
    le_item = None

# Streamlit App
st.title("Crop Production Prediction App")

# User Inputs
area = st.selectbox("Select Area (State/Country)", unique_areas)
crop = st.selectbox("Select Crop Name", unique_crops)
year = st.number_input("Enter Year", min_value=2000, max_value=2100, step=1)
area_harvested = st.number_input("Enter Area Harvested (in hectares)", min_value=1)
yield_value = st.number_input("Enter Yield (kg/ha)", min_value=1)

if st.button("Predict Production"):
    if le_area and le_item:
        area_encoded = le_area.transform([area])[0]
        crop_encoded = le_item.transform([crop])[0]
        
        # Prepare input data
        input_data = pd.DataFrame([[area_encoded, crop_encoded, year, area_harvested, yield_value]],
                                  columns=['Area', 'Item', 'Year', 'Area harvested', 'Yield'])
        
        # Make prediction
        prediction = model.predict(input_data)
        st.success(f"Predicted Crop Production: {prediction[0]:,.2f} tons")
    else:
        st.error("Error: Label encoding failed. Ensure dataset is loaded correctly.")
