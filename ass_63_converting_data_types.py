"""This file is for blah blah blah"""
import pandas as pd

alarms = pd.read_excel("data/Alarm Survey Data.xlsx")

alarms.dtypes
alarms.info()
alarms.head()

alarms.alarm_rating = pd.to_numeric(
    alarms.alarm_rating.str.replace(' stars', ''))

alarms.dtypes
