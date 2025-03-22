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
