import streamlit as st
import pandas as pd

st.header("File Upload & Visualization App")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Visualization")
    chart_type = st.selectbox("Select chart type", ["Line", "Bar", "Area"])
    columns = df.select_dtypes(include=['number']).columns.tolist()

    if columns:
        x_axis = st.selectbox("X-axis", columns)
        y_axis = st.multiselect("Y-axis", columns, default=columns[:1])

        if y_axis:
            if chart_type == "Line":
                st.line_chart(df.set_index(x_axis)[y_axis])
            elif chart_type == "Bar":
                st.bar_chart(df.set_index(x_axis)[y_axis])
            elif chart_type == "Area":
                st.area_chart(df.set_index(x_axis)[y_axis])
    else:
        st.warning("No numeric columns found for visualization.")

st.markdown("---")
st.write("Engineer: **Samy**")