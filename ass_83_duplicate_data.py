"""This file is for blah blah blah"""
import numpy as np
import pandas as pd

df_alarms = pd.read_excel("data/Alarm Survey Data.xlsx")

df_alarms[df_alarms.isna().any(axis=1)]
df_alarms.isna().sum()
df_alarms.sleep_quality.value_counts(dropna=False)

df_alarms.sleep_quality.fillna(2).value_counts(dropna=False)
df_alarms.sleep_quality.fillna(2, inplace=True)
df_alarms.info()

# duplicate data assignment
df_alarms[df_alarms.duplicated()]
df_alarms = df_alarms[~df_alarms.duplicated()]
df_alarms
