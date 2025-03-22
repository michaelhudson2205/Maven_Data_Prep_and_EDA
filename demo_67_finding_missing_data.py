"""This file is for blah blah blah"""
import numpy as np
import pandas as pd

df_grades = pd.read_excel("data/Student Grades.xlsx")

df_grades.head()
df_grades.info()

df_grades[df_grades.isna().any(axis=1)]

df_grades.Year.value_counts(dropna=False)
df_grades.isna().sum()

df_grades[df_grades.isna().any(axis=1)].dropna(subset=['Student', 'Class'])

df_grades.dropna(subset=['Student', 'Class'], inplace=True)
df_grades

df_grades[df_grades.Grade.isna()]
df_grades.Grade.mean()
df_grades.Grade.fillna(df_grades.Grade.mean(), inplace=True)
df_grades.Grade

df_grades[df_grades.isna().any(axis=1)]
df_grades[df_grades.Class == 'Freshman Seminar']
df_grades.loc[7, 'Year'] = 'Freshman'
df_grades.Year = np.where(df_grades.Year.isna(), 'Freshman', df_grades.Year)

df_grades.Class.value_counts()
df_grades.info()
df_grades[df_grades.Class.isin(['Exploratory Data Analysis', 'EDA'])]
df_grades[df_grades.Class.isin(['Intro to Python', 'Python'])]

df_grades.Year.value_counts()

df_grades.Grade.describe()
df_grades[df_grades.Grade > 100]

df_grades.Class = np.where(df_grades.Class == 'EDA',
                           'Exploratory Data Analysis', df_grades.Class)
df_grades.Class.value_counts()

df_grades.Class = np.where(df_grades.Class == 'Python',
                           'Intro to Python', df_grades.Class)
df_grades.Class.value_counts()

df_grades.Grade = np.where(df_grades.Grade > 100, 100, df_grades.Grade)
df_grades.Grade.describe()

df2_grades = pd.read_excel("data/Student Grades.xlsx")
df2_grades.head()
df2_grades.Class.value_counts()

class_mappings = {
    'Intro to Python': 'Intro to Python',
    'Intro to SQL': 'Intro to SQL',
    'EDA': 'Exploratory Data Analysis',
    'Freshman Seminar': 'Freshman Seminar',
    'Exploratory Data Analysis': 'Exploratory Data Analysis',
    'Python': 'Intro to Python'
}

df2_grades.Class = df2_grades.Class.map(class_mappings)

df2_grades.Class.value_counts()

run_times = pd.read_excel("data/Run Times.xlsx")
run_times.info()
run_times.Location = run_times.Location.str.lower().str.replace('the ',
                                                                '').str.strip('“”')
run_times
