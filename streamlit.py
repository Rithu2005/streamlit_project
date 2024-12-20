import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Streamlit App Title
st.title("YouTube Channel Analysis")

# Data
columns = ["Name", "Brand channel", "Subscribers (millions)", "Primary language", "Category", "Country"]
data = [
    ["MrBeast", "No", 335, "English", "Entertainment", "United States"],
    ["T-Series", "Yes", 280, "Hindi", "Music", "India"],
    ["Cocomelon - Nursery Rhymes", "Yes", 186, "English", "Education", "United States"],
    ["SET India", "Yes", 180, "Hindi", "Entertainment", "India"],
    ["Vlad and Niki", "No", 129, "English", "Entertainment", "Russia"],
    ["Kids Diana Show", "Yes", 128, "English", "Entertainment", "United States"],
    ["Like Nastya", "No", 123, "English", "Entertainment", "United States"],
    ["Zee Music", "Yes", 112, "Hindi", "Music", "India"],
    ["PewDiePie", "No", 110, "English", "Entertainment", "Sweden"],
    ["WWE", "Yes", 105, "English", "Sports", "United States"],
]

df = pd.DataFrame(data, columns=columns)

# Display Dataset
st.subheader("Dataset Preview")
st.dataframe(df)

# Convert Subscribers column to numeric
df["Subscribers (millions)"] = pd.to_numeric(df["Subscribers (millions)"], errors="coerce")

# Visualization 1: Bar chart of top channels by subscribers
st.subheader("Top 10 YouTube Channels by Subscribers")
df_sorted = df.sort_values(by="Subscribers (millions)", ascending=False).head(10)

st.bar_chart(data=df_sorted.set_index("Name")["Subscribers (millions)"])

# Visualization 2: Pie chart of categories
st.subheader("Distribution of Categories")
category_counts = df["Category"].value_counts()

fig, ax = plt.subplots()
colors = plt.cm.Paired(np.arange(len(category_counts)))
ax.pie(category_counts, labels=category_counts.index, autopct="%1.1f%%", startangle=140, colors=colors)
ax.set_title("Category Distribution")
st.pyplot(fig)

# Visualization 3: Scatter plot of subscribers by country
st.subheader("Subscribers by Country")
unique_countries = df["Country"].unique()
colors = plt.cm.rainbow(np.linspace(0, 1, len(unique_countries)))

fig, ax = plt.subplots(figsize=(12, 6))
for i, country in enumerate(unique_countries):
    country_data = df[df["Country"] == country]
    ax.scatter(
        country_data["Name"],
        country_data["Subscribers (millions)"],
        label=country,
        color=colors[i],
        s=100,
        alpha=0.7,
    )
ax.set_title("Subscribers by Country")
ax.set_xlabel("Channel Name")
ax.set_ylabel("Subscribers (millions)")
ax.legend(title="Country", bbox_to_anchor=(1.05, 1), loc="upper left")
ax.tick_params(axis="x", rotation=45)
st.pyplot(fig)
st.balloons()
