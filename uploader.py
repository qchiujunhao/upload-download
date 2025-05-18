import streamlit as st
import pandas as pd

st.title("📁 File Uploader")

# Upload file
uploaded_file = st.file_uploader("Choose a file", type=["csv", "tsv", "txt", "xlsx", "json"])

if uploaded_file is not None:
    st.success(f"Uploaded file: {uploaded_file.name}")
    st.write(f"File type: {uploaded_file.type}")
    st.write(f"File size: {uploaded_file.size / 1024:.2f} KB")

    # Show preview if it's a text or data file
    if uploaded_file.type in ["text/csv", "text/plain", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "application/json"]:
        try:
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith(".tsv"):
                df = pd.read_csv(uploaded_file, sep="\t")
            elif uploaded_file.name.endswith(".xlsx"):
                df = pd.read_excel(uploaded_file)
            elif uploaded_file.name.endswith(".json"):
                df = pd.read_json(uploaded_file)
            else:
                st.text(uploaded_file.read().decode("utf-8"))
                df = None

            if df is not None:
                st.subheader("Preview of Data:")
                st.dataframe(df.head())
        except Exception as e:
            st.error(f"Error reading file: {e}")

   #download button
    if df is not None:
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='data.csv',
            mime='text/csv',
        )