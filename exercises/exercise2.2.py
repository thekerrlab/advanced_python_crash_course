import pylab as pl
import pandas as pd

pd_data = pd.read_csv('data/Okinawa_weather_data.csv', sep=';')
grouped_data = pd_data.groupby('Day').aggregate(['mean', 'std'])
temp = grouped_data['Wind Speed  [10 m above gnd]']
pl.plot(temp.index, temp['mean'])
pl.fill_between(temp.index, temp['mean'] - 2*temp['std'], temp['mean'] + 2*temp['std'], alpha=0.2)
pl.xlabel('Day')
pl.ylabel('Wind speed (knots)')