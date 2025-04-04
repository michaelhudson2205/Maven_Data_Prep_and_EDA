"""blah blah blah"""
import pandas as pd
import seaborn as sns

student_data = pd.read_csv('data/student_data.csv')
student_data.head()

sns.pairplot(student_data)

# 123 DEMO Distributions

student_data['Cups of Coffee'].value_counts().sort_index()
sns.histplot(student_data['Cups of Coffee'], bins=11, color='green')

student_data['Hours Studied']
student_data['Hours Studied'].round().value_counts().sort_index()
sns.histplot(student_data['Hours Studied'], bins=5, color='purple')

# 129 DEMO Scatter Plots
sns.scatterplot(data=student_data, x='Hours of Sleep', y='Grade on Test')
student_data[student_data['Hours of Sleep'] < 3]

# 131 DEMO Correlations
student_data.corr()
