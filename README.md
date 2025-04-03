# Crop Production Prediction Project

## Overview
The **Crop Production Prediction App** is a machine learning-powered web application built using **Streamlit**. It predicts crop production based on various input parameters such as area, crop type, year, harvested area, and yield. The prediction is powered by a **Random Forest model** trained on historical crop production data.

## Features
- **User-friendly Interface:** Built with Streamlit for easy interaction.
- **Machine Learning Model:** Uses a trained Random Forest model for predictions.
- **Dropdown Selections:** Allows users to select area and crop type from available options.
- **Dynamic Input Fields:** Users can enter year, harvested area, and yield to get predictions.
- **Instant Predictions:** Provides real-time crop production estimates based on input values.

## Project Structure
```
Crop_Production_Prediction/
    FOASTST_data.csv                # Data Set
│── preprocessed_crop_production_data.csv  # Preprocessed data file
│── CropproductionEDA.ipynb            # Analysis of the data
│── cropproduction_model.ipynb         # Code for the model

│── crop_production_model.pkl          # Trained machine learning model
│── Crop.py                            # Streamlit app for prediction
│── README.md                          # Project documentation
```

## Installation
### Prerequisites
Ensure you have Python installed on your system.

### Install Required Libraries
Run the following command to install dependencies:
```sh
pip install streamlit pandas scikit-learn pickle5
```

## How to Run the App
1. Clone the repository or download the project files.
3. Navigate to the project directory.
4. Run the Streamlit app using the command:
   ```sh
   streamlit run Crop.py
   ```
5. The app will launch in your browser, allowing you to make predictions.

## Usage
1. **Select Area & Crop Type** from dropdown menus.
2. **Enter Year** (between 2000 and 2100).
3. **Provide Area Harvested** (in hectares).
4. **Enter Yield** (kg per hectare).
5. Click **Predict Production** to see the estimated crop production.

## Dependencies
- Python 3.x
- Streamlit
- Pandas
- Scikit-learn
- Pickle

## Troubleshooting
- If you get an error regarding missing `FOASTAT_data.csv`, ensure the dataset file is present in the project directory.
- If the model file (`crop_production_model.pkl`) is missing, retrain the model or place the correct file in the directory.

## Future Enhancements
- Adding more crop-related features for improved prediction accuracy.
- Enhancing visualization with charts and graphs.
- Allowing users to upload their datasets for custom predictions.

## Author
Shanmugapriya

## License
This project is licensed under the MIT License.

