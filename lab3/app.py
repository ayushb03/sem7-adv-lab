import streamlit as st
import pandas as pd
import plotly.express as px

# Dataset: https://www.kaggle.com/datasets/mirichoi0218/insurance

df = pd.read_csv('data.csv')  

st.set_page_config(page_title="Healthcare Dashboard", layout="wide")

# App Title
st.title("Interactive Healthcare Dashboard: All Charts")

# ---------------- Display All Charts Below -----------------

# 1. Word Chart (Region Frequency)
st.subheader("Word Chart: Region Frequency")
region_counts = df['region'].value_counts().to_dict()
word_data = {'Region': list(region_counts.keys()), 'Count': list(region_counts.values())}
fig = px.treemap(word_data, path=['Region'], values='Count', title='Word Chart of Region Frequency')
fig.update_traces(textinfo='label+percent entry')
st.plotly_chart(fig)

# 2. Box and Whisker Plot (Charges by Smoker Status)
st.subheader("Box and Whisker Plot: Charges by Smoker Status")
fig = px.box(df, x='smoker', y='charges', color='smoker', title='Charges by Smoker Status')
st.plotly_chart(fig)

# 3. Violin Plot (Charges by Sex)
st.subheader("Violin Plot: Charges by Sex")
fig = px.violin(df, x='sex', y='charges', color='sex', box=True, points='all', title='Charges by Sex')
st.plotly_chart(fig)

# 4. Regression Plot (BMI vs Charges)
st.subheader("Regression Plot: BMI vs Charges")
fig = px.scatter(df, x='bmi', y='charges', trendline='ols', color='age', title='BMI vs Charges with Regression Line')
st.plotly_chart(fig)

# 5. 3D Chart (Age, BMI, Charges)
st.subheader("3D Chart: Age, BMI, and Charges")
fig = px.scatter_3d(df, x='age', y='bmi', z='charges', color='smoker', size='charges', opacity=0.7, title='3D Plot of Age, BMI, and Charges')
st.plotly_chart(fig)

# 6. Jitter Plot (Age vs Charges)
st.subheader("Jitter Plot: Age vs Charges")
fig = px.strip(df, x='age', y='charges', color='smoker', title='Jitter Plot: Age vs Charges')
st.plotly_chart(fig)

# 7. Line Chart (Age vs Charges)
st.subheader("Line Chart: Age vs Charges")
fig = px.line(df, x='age', y='charges', title='Line Chart: Age vs Charges', markers=True)
st.plotly_chart(fig)

# 8. Area Chart (Age vs Charges by Smoker Status)
st.subheader("Area Chart: Age vs Charges by Smoker Status")
fig = px.area(df, x='age', y='charges', color='smoker', title='Area Chart: Age vs Charges by Smoker Status')
st.plotly_chart(fig)

# 9. Waterfall Chart (Charges by Region)
st.subheader("Waterfall Chart: Charges by Region")
region_charges = df.groupby('region')['charges'].sum().sort_values(ascending=False)
fig = px.bar(x=region_charges.index, y=region_charges.values, title='Waterfall Chart: Charges by Region')
st.plotly_chart(fig)

# 10. Donut Chart (Smoker Distribution)
st.subheader("Donut Chart: Smoker Distribution")
fig = px.pie(df, names='smoker', hole=0.5, title='Donut Chart of Smokers')
fig.update_traces(textinfo='percent+label')
st.plotly_chart(fig)

# 11. Treemap (Charges by Region)
st.subheader("Treemap: Charges by Region")
fig = px.treemap(df, path=['region'], values='charges', color='charges', title='Treemap of Charges by Region')
st.plotly_chart(fig)

# 12. Funnel Chart (Charges by Region)
st.subheader("Funnel Chart: Charges by Region")
fig = px.funnel(df, x='region', y='charges', title='Funnel Chart: Charges by Region')
st.plotly_chart(fig)

# 13. Bar Chart (Charges by Region)
st.subheader("Bar Chart: Charges by Region")
fig = px.bar(df, x='region', y='charges', color='region', title='Bar Chart: Charges by Region')
st.plotly_chart(fig)

# 14. Pie Chart (Smoker Distribution)
st.subheader("Pie Chart: Smoker Distribution")
fig = px.pie(df, names='smoker', title='Pie Chart of Smokers')
fig.update_traces(textinfo='percent+label')
st.plotly_chart(fig)

# 15. Histogram (Distribution of Charges)
st.subheader("Histogram: Distribution of Charges")
fig = px.histogram(df, x='charges', nbins=30, title='Histogram of Charges Distribution')
st.plotly_chart(fig)

# 16. Timeline Chart (Charges by Age)
st.subheader("Timeline Chart: Charges by Age")
fig = px.line(df, x='age', y='charges', title='Timeline Chart: Charges by Age', markers=True)
st.plotly_chart(fig)

# 17. Scatter Plot (BMI vs Charges)
st.subheader("Scatter Plot: BMI vs Charges")
fig = px.scatter(df, x='bmi', y='charges', color='smoker', title='Scatter Plot: BMI vs Charges', size='charges', hover_data=['age'])
st.plotly_chart(fig)

# 18. Bubble Plot (Age, BMI, Charges)
st.subheader("Bubble Plot: Age, BMI, and Charges")
fig = px.scatter(df, x='age', y='charges', size='bmi', color='smoker', title='Bubble Plot: Age, BMI, Charges', hover_data=['region'])
st.plotly_chart(fig)