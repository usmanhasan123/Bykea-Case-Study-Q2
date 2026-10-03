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
    df = pd.read_csv(uploaded_file)

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
