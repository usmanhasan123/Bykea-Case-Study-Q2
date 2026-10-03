import streamlit as st
import pandas as pd

from inference import predict_csv


st.title("Sticky Customer Prediction")

st.write(
    "Upload a CSV file containing customer data to generate predictions."
)

uploaded_file = st.file_uploader(
    "Upload CSV",
    type=["csv"]
)

if uploaded_file is not None:

    # Read uploaded CSV
    # df = pd.read_csv(uploaded_file)
    categorical_columns = ['parent_region_id', 'child_region_id', 'product_code',
                           'acquired_by', 'purchase_weekday', 'acquisition_weekday']
    numeric_columns = ['first_purchase_amount', 'days_to_first_purchase',
                       'purchase_hour', 'acquisition_hour']
    df = pd.read_csv(uploaded_file, dtype={c: str for c in ['customer_id'] + categorical_columns})
    
    df = df.dropna(subset=['sticky_target']).copy()
    
    for column in categorical_columns:
        df[column] = df[column].fillna('Unknown').astype('category')
    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors='coerce')
    df['sticky_target'] = df['sticky_target'].astype(int)

    st.subheader("Uploaded Data")
    st.dataframe(df.head())

    if st.button("Generate Predictions"):

        try:
            # Call inference pipeline
            predictions_df = predict_csv(df)

            st.success("Predictions generated successfully.")

            st.subheader("Prediction Results")
            st.dataframe(predictions_df.head())

            # Convert dataframe to CSV
            csv = predictions_df.to_csv(index=False).encode("utf-8")

            st.download_button(
                label="Download Predictions",
                data=csv,
                file_name="predictions.csv",
                mime="text/csv"
            )

        except Exception as e:
            st.error(f"Prediction failed: {e}")
