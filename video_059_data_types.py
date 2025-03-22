"""This file is for blah blah blah"""
import pandas as pd

run_times = pd.read_excel("data/Run Times.xlsx")

run_times.dtypes
run_times.info()
run_times.Fee
clean_fee = run_times.Fee.str.replace('$', '')
clean_fee
run_times.Fee = pd.to_numeric(clean_fee)
run_times.info()
pd.to_numeric(run_times['Warm Up Time'], errors='coerce')
run_times['Warm Up Time']
run_times['Warm Up Time'] = pd.to_numeric(
    run_times['Warm Up Time'].astype('str').str.replace(' min', ''))
run_times.info()
run_times.dtypes
run_times.Rain.astype('int')
