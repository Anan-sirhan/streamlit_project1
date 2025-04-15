import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import ylabel, xlabel, subplots, subplot

st.write("**Welcome** to my first Streamlit project!")
st.title("Mental Health in Tech – Data Analysis Dashboard")
st.markdown("""
### Introduction

This dashboard presents an exploratory data analysis (EDA) of the **OSMI Mental Health in Tech Survey**.  
The goal of this project is to better understand mental health trends among people working in the tech industry.  
The analysis includes data visualizations, interactive filters, and insights based on factors such as gender, age, country, and workplace conditions.

The project is built using **Python** and **Streamlit**, and is designed for clarity, accessibility, and future expansion.
""")

# Step 2: Load and Clean the Data
st.header("Step 1: Load and Clean the Data")
#load dataset
df=pd.read_csv("survey.csv")
st.write("df=pd.read_csv(survey.csv)")
#clean column names (remove extra spaces)
df.columns = df.columns.str.strip()
print(df.columns)
#show the first rows
st.write("Here are the first few rows the dataset after cleaning:")
st.write("df.head(5)")
# Step 2: Exploratory Data Analysis (EDA)
st.write("Perform initial exploration of the dataset to understand its structure, check for missing values, and see the general distribution of data")
st.write(df.describe())
st.write("df.isnall().sum()")

st.header("Step 2:Graph Visualization")
# Gender Distribution Bar Graph"
#This section of the dashboard creates a bar chart showing the distribution of respondents by gender.
##It includes Three categories: Female, Male,other, and displays the total number of respondents at the top.

# Create bar chart
# Group by gender
# Clean Gender column
df['Gender'] = df['Gender'].str.strip().str.lower()
df['Gender'] = df['Gender'].apply(lambda x: 'Male' if x in ['male', 'm']
                                  else 'Female' if x in ['female', 'f']
                                  else 'Other')
# Count values
gender_counts = df['Gender'].value_counts()

# Create bar chart
fig, ax = plt.subplots()
gender_counts.plot(kind='bar', ax=ax, color=['blue', 'pink', 'gray'])
# Add titles and labels
ax.set_title("Gender Distribution")
ax.set_xlabel("Gender")
ax.set_ylabel("Number of Respondents")
ax.set_xticklabels(gender_counts.index, rotation=0)
# Show in Streamlit
st.header(" Gender Distribution")
st.markdown("""
This chart shows how respondents identify their gender: **Female**, **Male**, or grouped as **Other**.
""")
st.write(df['Country'].value_counts())
st.pyplot(fig)
import seaborn as sns
import matplotlib.pyplot as plt

st.header("Country of Residence Distribution")
st.markdown("This chart shows the number of survey respondents from each country.")
top_countries=df['Country'].value_counts().nlargest(10)
top_country_names=top_countries.index
df_top = df[df['Country'].isin(top_country_names)]
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(data=df_top, y='Country', order=top_country_names, palette='viridis', ax=ax)

df.columns

ax.set_title("Top 10 Countries by Number of Respondents")
ax.set_xlabel("Number of Respondents")
ax.set_ylabel("Country")

st.pyplot(fig)
#Add a title to the Streamlit app section
st.header("Treatment Seeking by Gender")

#Group the data by Gender and Treatment response
# This gives us a count of how many people of each gender answered Yes or No
treatment_counts = df.groupby(['Gender', 'treatment']).size().unstack()

#Create a figure for the bar chart (simple approach)
fig,ax = plt.subplots()

#Plot the grouped data as a bar chart
# We use different colors to represent Yes and No
treatment_counts.plot(kind='bar', ax=ax ,color=['lightcoral', 'lightgreen'])

#Add a title and axis labels to make the chart readable
ax.set_title("How Different Genders Seek Mental Health Treatment")
ax.set_xlabel("Gender")
ax.set_ylabel("Number of Respondents")

#Add a legend to show what the colors mean (Yes or No)
ax.legend(title="Sought Treatment", labels=["No", "Yes"])

#Display the chart in the Streamlit app
st.pyplot(fig)


#Drop any missing (NaN) values from the 'age' column to avoid errors in plotting.
df['Age'] = df['Age'].dropna()
# Set up the plot size (10 inches wide by 6 inches tall).
plt.figure(figsize=(10,6))
# Plot a histogram with a Kernel Density Estimate (KDE) to show the distribution of ages.
#'bins=20' controls the number of bars in the histogram, and 'color='red' sets the color of the plot.
sns.histplot(df['Age'], kde=True, bins=20, color='red')
# Add title and labels to the plot for clarity.
plt.title("Age Distribution", fontsize=16)  # Title of the plot.
plt.xlabel("Age", fontsize=12)  # Label for the x-axis.
plt.ylabel("Frequency", fontsize=12)  # Label for the y-axis.
# Display the plot on the streamlit.
st.pyplot(plt)
# Display basic statistics about the 'age' data, such as mean, standard deviation, and percentiles.
age_stats = df['Age'].describe()
st.write(age_stats)
# Add an explanation to the Streamlit app
st.write("""
### Age Distribution
This histogram shows the distribution of ages in the dataset. The x-axis represents the age values, and the y-axis shows the frequency of each age group. 
The Kernel Density Estimate (KDE) curve provides a smoothed view of the distribution, helping us to better understand the data's shape.
""")



#Replace missing values (NaN) with "No Answer"
df['self_employed'] = df['self_employed'].fillna("No Answer")
#Add a section title in Streamlit
st.header("Self Employment Status of Respondents")
#Count how many people chose each option
self_employment_counts = df['self_employed'].value_counts()
#Create the bar chart
fig, ax = plt.subplots()
ax.bar(self_employment_counts.index, self_employment_counts.values, color=['orange', 'skyblue', 'gray'])
# Add labels and title
ax.set_title("Self Employment Status")
ax.set_xlabel("Employment Type")
ax.set_ylabel("Number of Respondents")

#Show the chart in the Streamlit app
st.pyplot(fig)

#Replace missing values in the 'mental_health_interfere_with_work' column
df['work_interfere'] = df['work_interfere'].fillna("No Answer")
#Add a header in the Streamlit app
st.header("How Mental Health Affects Work")
#Count the number of responses per category
work_interfere_counts = df['work_interfere'].value_counts()
#Create a bar chart
fig, ax = plt.subplots()
ax.bar(work_interfere_counts.index, work_interfere_counts.values, color='mediumseagreen')
#Add title and labels
ax.set_title("Mental Health Interference with Work")
ax.set_xlabel("Response")
ax.set_ylabel("Number of Respondents")
#Show the chart in the Streamlit app
st.pyplot(fig)

st.header("Relationship Between Family History and Seeking Treatment")
# We group the data by 'family_history' and 'treatment' to see how many people
# with or without family history of mental illness have sought treatment
family_treatment_counts = df.groupby(['family_history', 'treatment']).size().unstack()
# We create a bar chart to compare the counts
fig, ax = plt.subplots()
family_treatment_counts.plot(kind='bar', ax=ax, color=['mediumpurple', 'darkorange'])
# Add title and axis labels
ax.set_title("Treatment Seeking Based on Family Mental Health History")
ax.set_xlabel("Family History of Mental Illness")
ax.set_ylabel("Number of Respondents")
# Add a legend to explain colors
plt.legend(title="Sought Treatment", labels=["No", "Yes"])
# Show the chart in Streamlit
st.pyplot(fig)
# Add explanation text
st.write("""
This chart compares the number of people who have or haven't sought mental health treatment
based on whether they have a family history of mental illness.
It helps us understand if family history influences the decision to seek help.
""")

st.header("Company Mental Health Benefits")
# Count the responses to the 'benefits' question
benefits_counts = df['benefits'].value_counts()
# Create the bar chart
fig, ax = plt.subplots()
benefits_counts.plot(kind='bar', ax=ax, color='teal')
# Add chart labels
ax.set_title("Does the Company Offer Mental Health Benefits?")
ax.set_xlabel("Response")
ax.set_ylabel("Number of Respondents")
# Display the chart in Streamlit
st.pyplot(fig)
# Explanation
st.write("""
This chart shows how respondents answered the question about whether their employer provides mental health benefits.
It helps us understand how common it is for companies in the tech industry to support mental well-being through formal benefits.
""")

# Transforming and Formatting Employee Count Data: Replacing Month Abbreviations and Applying Conditional Formatting
df["no_employees"] = df["no_employees"].astype(str)
df["no_employees"] = df["no_employees"].str.replace("May", "5", regex=False)
df["no_employees"] = df["no_employees"].str.replace("Jun", "6", regex=False)

st.header("Company Size Distribution")
# Count how many respondents are in each company size category
company_size_counts = df['no_employees'].value_counts().sort_index()
# Create a bar chart
fig, ax = plt.subplots()
company_size_counts.plot(kind='bar', ax=ax, color='mediumslateblue')
# Add labels and title
ax.set_title("Distribution of Respondents by Company Size")
ax.set_xlabel("Company Size (Number of Employees)")
ax.set_ylabel("Number of Respondents")
# Rotate x-axis labels for better readability
plt.xticks(rotation=45)
# Show the chart in Streamlit
st.pyplot(fig)

# Explanation
st.write("""
This chart displays how many survey respondents work in companies of different sizes.
It helps us understand whether mental health challenges and awareness are more discussed in small or large organizations.
""")

country_filter = st.selectbox("Select Country", df['Country'].unique())
gender_filter = st.selectbox("Select Gender", df['Gender'].unique())
age_filter = st.slider("Select Age Range", min_value=int(df['Age'].min()), max_value=int(df['Age'].max()), value=(int(df['Age'].min()), int(df['Age'].max())))
filtered_df = df[(df['Country'] == country_filter) &
                 (df['Gender'] == gender_filter) &
                 (df['Age'] >= age_filter[0]) &
                 (df['Age'] <= age_filter[1])]
st.write(f"Filtered Data for Country: {country_filter}, Gender: {gender_filter}, Age Range: {age_filter[0]} - {age_filter[1]}")
st.write(filtered_df)

plt.figure(figsize=(10,6))
sns.histplot(filtered_df['Age'], kde=True, bins=20, color='red')
plt.title(f"Age Distribution in {country_filter} for {gender_filter}", fontsize=16)
plt.xlabel("Age", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
st.pyplot(plt)

age_stats = filtered_df['Age'].describe()
st.write(age_stats)


import base64

 #--- Download CSV Button ---
def generate_csv_download_link(dataframe):
    csv = dataframe.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # encode to base64
    href = f'<a href="data:file/csv;base64,{b64}" download="filtered_data.csv">📥 Download Filtered Data as CSV</a>'
    return href

st.markdown(generate_csv_download_link(filtered_df), unsafe_allow_html=True)

st.markdown("""
---
### 📝 Summary

This dashboard allows users to filter mental health survey data by Country, Gender, and Age.  
You can explore trends and download the filtered data as a CSV file for further analysis.
""")

