# Demographic Data Analyzer

import pandas as pd
from google.colab import files
uploaded = files.upload()
df = pd.read_csv(next(iter(uploaded)))

print("Number of columns:", df.head())
# How many people of each race are represented in this dataset?
# This should be a Pandas series with race names as the index labels. (race column)
race_count = df['race'].value_counts()
print("-------------Number of people represented in this dataset-------------- :", race_count)

# What is the average age of men?
average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
print("-------------Average age of mean is-------------------- :",average_age_men)

# What is the percentage of people who have a Bachelor's degree?
perc = df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]   # simple meaning:-
                  # no. of people with bachelor's degree / total no. of people ; df.shape[0] will filter rows
percentage_bachelors = round(perc * 100, 5)
print("-----------------Percentage of bachelors is--------------- :",percentage_bachelors)

# What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
higher_ed = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
filter = higher_ed[higher_ed['salary'] == '>50K']
percentage_advanced_education = round((len(filter) / len(higher_ed)) * 100, 2)
print("------------percentage of people with advanced education :-----------", percentage_advanced_education)

# What percentage of people without advanced education make more than 50K?
percentage_wo_advanced_education = 100 - percentage_advanced_education
print("------------percentage of people without advanced education :-----------", percentage_wo_advanced_education)

# What is the minimum number of hours a person works per week?
min_work_hours = df['hours-per-week'].min()
print("------------minimum number of hours a person works per week :-----------", min_work_hours)

# What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
num_min_workers = df[df['hours-per-week'] == min_work_hours]
salary = num_min_workers[num_min_workers['salary'] == ">50K"].sum()
rich_percentage = round(salary * 100, 2)
print("------------percentage of the people who work the minimum number of hours per week have a salary of more than 50K :-----------", rich_percentage)

# Which country has the highest percentage of people that earn >50K and what is that percentage?
more_than_50k = df[df['salary'] == '>50K']['native-country'].value_counts()
top_country = more_than_50k.idxmax()            #The idxmax() function in Pandas returns the index label of the first occurrence of the maximum value in a Series or column of a DataFrame.
highest_earning_country_percentage = round(more_than_50k.max() / df['native-country'].value_counts().max() * 100, 2)
print("--------------The country is",top_country, "and percentage is ", highest_earning_country_percentage,"------------------")

# Identify the most popular occupation for those who earn >50K in India.
india_occupation = df[df['native-country'] == 'India']
salary1 = india_occupation[india_occupation['salary'] == '>50K']['occupation'].value_counts()
top_IN_occupation = salary1.idxmax()
print("--------------The most popular occupation is--------------",top_IN_occupation)
