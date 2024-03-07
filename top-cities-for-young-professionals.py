# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np

# Improved App title and introduction
st.title("Top Cities for Young Professionals")
st.markdown("""
Explore the top cities for job growth, vibrant communities, and high quality of life. This interactive guide provides insights into each city's job market, lifestyle, cultural scene, and more. Customize your search with filters and compare cities based on your preferences.
""")

# Simulated data for demonstration
cities_data = pd.DataFrame({
    "City": ["Austin, Texas", "Seattle, Washington", "Denver, Colorado", "Charlotte, North Carolina", "Nashville, Tennessee"],
    "Job Growth Rate (%)": [3.5, 2.8, 2.5, 3.0, 2.9],
    "Cost of Living Index": [130, 180, 120, 110, 100],
    "Quality of Life Index": [7.8, 8.0, 7.5, 7.2, 7.4]
})

# Filters for customization
st.sidebar.header("Customize Your Search")
selected_cities = st.sidebar.multiselect("Select Cities", options=cities_data["City"], default=cities_data["City"])

# Filter data based on selection
filtered_data = cities_data[cities_data["City"].isin(selected_cities)]

if not filtered_data.empty:
    # Display filtered data
    st.write("## Job Growth and Cost of Living in Selected Cities")
    st.dataframe(filtered_data)

    # Data Visualization
    st.write("### Job Growth Rate Comparison")
    st.bar_chart(filtered_data.set_index("City")["Job Growth Rate (%)"])

    st.write("### Cost of Living Index Comparison")
    st.bar_chart(filtered_data.set_index("City")["Cost of Living Index"])

    # Interactive Maps (placeholder example)
    # Assuming you have latitude and longitude data
    # For demonstration, we'll generate random coordinates
    # np.random.seed(42)  # For reproducibility
    # map_data = pd.DataFrame({
    #     'lat': np.random.rand(len(filtered_data)) * 10 + 35,  # Random latitudes
    #     'lon': np.random.rand(len(filtered_data)) * -10 - 100  # Random longitudes
    # })
    # st.map(map_data)

    # st.write("## Detailed City Profiles")
    # for city in selected_cities:
    #     st.subheader(city)
    #     # Here, you would include more detailed information about each city
    #     st.write(f"More detailed information about living, working, and leisure in {city}.")
else:
    st.warning("Please select at least one city to display information.")

st.write("## Conclusion")
st.markdown("""
Considering your career goals, lifestyle preferences, and desired community is crucial when exploring these cities. This tool aims to provide a starting point in your journey to finding the perfect city for your professional and personal life.
""")

# Run the app with the following command in your terminal:
# streamlit run your_script_name.py
