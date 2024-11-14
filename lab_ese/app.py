import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st
from sklearn.cluster import KMeans

# Set up page config
st.set_page_config(page_title="Women's Empowerment Analysis", layout="wide")

# Title and introduction
st.title("Women's Empowerment and Gender Parity Analysis")
st.write("""
This app provides an analysis of Women's Empowerment Index (WEI) and Global Gender Parity Index (GGPI) for different countries.
""")

# Section 1: Load Data
@st.cache_data
def load_data():
    return pd.read_csv('./data/data.csv')

df = load_data()

# Sidebar for raw data toggle
if st.sidebar.checkbox("Show raw data"):
    st.write("## Raw Data")
    st.dataframe(df)

# Section 2: Data Preprocessing
st.sidebar.header("Data Preprocessing")
st.sidebar.write("Check for missing values and convert columns to numeric.")

# Check missing values
st.write("### Missing Values")
missing_values = df.isnull().sum()
st.write(missing_values[missing_values > 0])

# Convert columns to numeric where necessary
df['Women\'s Empowerment Index (WEI) - 2022'] = pd.to_numeric(df['Women\'s Empowerment Index (WEI) - 2022'], errors='coerce')
df['Global Gender Parity Index (GGPI) - 2022'] = pd.to_numeric(df['Global Gender Parity Index (GGPI) - 2022'], errors='coerce')

# Drop duplicates
df.drop_duplicates(inplace=True)

# Main analysis area
tabs = st.selectbox("Select a section to explore", ["Overview", "Visualizations", "Clustering", "Conclusions"])

if tabs == "Overview":
    st.write("""
    ### Overview of the Data
    - **Women's Empowerment Index (WEI)** and **Global Gender Parity Index (GGPI)** are the key indicators.
    - Data includes various regions and empowerment groups, offering valuable insights into gender parity.
    """)

elif tabs == "Visualizations":
    # 1. Distribution of WEI
    st.header("1. Distribution of Women's Empowerment Index (WEI)")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Histogram of WEI - 2022")
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.histplot(df['Women\'s Empowerment Index (WEI) - 2022'], kde=True, bins=20, color='mediumvioletred', ax=ax)
        ax.set(title='Histogram of WEI - 2022', xlabel='WEI - 2022', ylabel='Frequency')
        st.pyplot(fig)

    with col2:
        st.subheader("Box Plot of WEI - 2022")
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.boxplot(x='Women\'s Empowerment Index (WEI) - 2022', data=df, color='skyblue', ax=ax)
        ax.set(title='Box Plot of WEI - 2022', xlabel='WEI - 2022')
        st.pyplot(fig)

    # 2. Correlation Matrix
    st.header("2. Correlation Matrix")
    corr_matrix = df[['Women\'s Empowerment Index (WEI) - 2022', 'Global Gender Parity Index (GGPI) - 2022']].corr()
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, ax=ax)
    ax.set(title='Correlation Matrix')
    st.pyplot(fig)

    # 3. Regional Comparison
    st.header("3. Regional Comparison")
    region_avg_wei = df.groupby('Sustainable Development Goal regions')['Women\'s Empowerment Index (WEI) - 2022'].mean().reset_index()
    fig = px.bar(region_avg_wei, x='Sustainable Development Goal regions', y='Women\'s Empowerment Index (WEI) - 2022',
                 title='Average WEI by Region', labels={'Women\'s Empowerment Index (WEI) - 2022': 'Average WEI - 2022'},
                 color='Women\'s Empowerment Index (WEI) - 2022', color_continuous_scale='Viridis')
    st.plotly_chart(fig)

elif tabs == "Clustering":
    st.header("Clustering Analysis")
    num_clusters = st.slider("Select number of clusters:", 2, 5, 3)

    # K-Means clustering
    features = df[['Women\'s Empowerment Index (WEI) - 2022', 'Global Gender Parity Index (GGPI) - 2022']].dropna()
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    df['Cluster'] = kmeans.fit_predict(features)

    fig = px.scatter(df, x='Global Gender Parity Index (GGPI) - 2022', y='Women\'s Empowerment Index (WEI) - 2022',
                     color='Cluster', title='Clustering of Countries', labels={'Global Gender Parity Index (GGPI) - 2022': 'GGPI - 2022', 'Women\'s Empowerment Index (WEI) - 2022': 'WEI - 2022'},
                     color_continuous_scale='Viridis')
    st.plotly_chart(fig)

elif tabs == "Conclusions":
    st.header("Conclusions and Action Items")
    st.write("""
    - **Prioritize Gender Parity Initiatives**: A strong correlation exists between gender parity and empowerment levels.
    - **Targeted Interventions**: Regions and groups with lower empowerment indices need targeted strategies to address socio-economic factors.
    - **Continued Research and Data Collection**: Regular monitoring and dataset expansion are crucial for understanding and improving women's empowerment globally.
    """)

# Expandable section for advanced visualizations
with st.expander("Show More Visualizations"):
    # Additional Visualizations (e.g., violin plots, pie charts, etc.)
    st.subheader("5. Pie Chart of WEI by Empowerment Group")
    group_counts = df['Women\'s Empowerment Group - 2022'].value_counts()
    fig, ax = plt.subplots(figsize=(8, 8))
    colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854']
    ax.pie(group_counts, labels=group_counts.index, autopct='%1.1f%%', startangle=140, colors=colors, wedgeprops={'edgecolor': 'black'})
    ax.set(title="Proportion of Countries by Women's Empowerment Group - 2022")
    st.pyplot(fig)

    # Hexbin Plot: Density of WEI vs GGPI
    st.subheader("6. Density Analysis: WEI vs GGPI")
    fig, ax = plt.subplots(figsize=(8, 6))
    hb = ax.hexbin(df['Global Gender Parity Index (GGPI) - 2022'], df['Women\'s Empowerment Index (WEI) - 2022'], gridsize=30, cmap='YlGnBu', mincnt=1)
    plt.colorbar(hb, ax=ax, label='Density')
    ax.set(title='Density of WEI vs GGPI', xlabel='GGPI - 2022', ylabel='WEI - 2022')
    st.pyplot(fig)
