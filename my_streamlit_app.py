import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.figure_factory as ff
import matplotlib.pyplot as plt

st.title('Cars Dataset Study')

# Load the data
@st.cache_data
def load_data():
    cars_df = pd.read_csv("https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv")
    return cars_df

df = load_data()

df['continent'] = df['continent'].str.strip()
df['continent'] = df['continent'].str.strip().str.replace('.', '')

# Add a selectbox and a sidebar:
continent = st.sidebar.selectbox(
    'Which continent do you want to analyze?',
    ('All', 'US', 'Japan', 'Europe')
)

# Filter the data for the chosen continent or not at all if 'All' is chosen
if continent != 'All':
    df = df[df['continent'] == continent]

# If 'All' is chosen, calculate the correlation matrix and draw the heatmap between car attributes
if continent == 'All':
    # Calculate the correlation matrix
    corr_matrix = df.corr()

    # Draw the heatmap of the correlation matrix
    fig, ax = plt.subplots(figsize=(10, 10))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", 
                cmap='coolwarm', cbar=True, ax=ax)
    plt.title('Correlation Heatmap of Car Attributes') 
    st.pyplot(fig)

    st.markdown('**We can see that the biggest correlations (>0.90) are weight/cubicinches, hp/cubicinches and cylinders/cubicinches**')
    

# List of numerical columns
num_cols = ['mpg', 'cylinders', 'cubicinches', 'hp', 'weightlbs', 'time-to-60', 'year']

# Draw the distribution charts
for col in num_cols:
    fig, ax = plt.subplots()
    sns.histplot(df[col], kde=True, ax=ax)
    plt.title(f"Distribution of {col} for {continent}")
    st.pyplot(fig)

