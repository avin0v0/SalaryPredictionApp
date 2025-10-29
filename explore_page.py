import streamlit as st 
import pandas as pd;
import matplotlib.pyplot as plt

def tackle_country(categories,cutoff):
  cat_map={}
  for i in range(len(categories)):
    if categories.values[i] >= cutoff:
      cat_map[categories.index[i]] = categories.index[i]
    else:
      cat_map[categories.index[i]] = 'Other'
  return cat_map

def clean_exp(val):
  if val == 'Less than 1 year':
    return 0.5
  if val == 'More than 50 years':
    return 50
  return float(val)

def clean_degree(val):
  if 'Bachelor’s degree' in val:
    return 'Bachelor’s degree'
  if 'Professional degree (JD, MD, Ph.D, Ed.D, etc.)' in val:
    return 'Post Grad'
  if 'Master’s degree' in val:
    return 'Master’s degree'
  return 'Less than a Bachelors'

@st.cache_data
def load_data():
  df = pd.read_csv("survey_results_public.csv")
  df = df[["Country","EdLevel","YearsCodePro","Employment","ConvertedCompYearly"]]
  df = df.rename({"ConvertedCompYearly":"Salary"},axis=1)
  df=df[df['Salary'].notnull()]
  df=df.dropna()
  df[df['Employment'] == "Employed, full-time"]
  df= df.drop("Employment",axis=1)

  country_map=tackle_country(df['Country'].value_counts(),400)
  df['Country']=df['Country'].map(country_map)
  df=df[df["Salary"]<= 250000]
  df=df[df["Salary"]>= 10000]
  df=df[df["Country"]!="Other"]

  df['YearsCodePro']=df['YearsCodePro'].apply(clean_exp)
  df.EdLevel = df.EdLevel.apply(clean_degree)

  return df

df = load_data()

def show_explore_show():
  st.title("Explore Software Engineer Salaries")
  st.write(

  )
  data=df["Country"].value_counts()

  fig,ax = plt.subplots()
  ax.pie(data, labels=data.index,autopct="%1.1f%%", shadow=True, startangle=90)
  st.write("No. of data from different Countries")
  st.pyplot(fig)

  st.write("""
           
  ### Mean Salary Based On Country
           
           """)
  data=df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
  st.bar_chart(data) 

  st.write("""
           
  ### Mean Salary Based On Experience
           
           """)
  data=df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
  st.line_chart(data) 







  

