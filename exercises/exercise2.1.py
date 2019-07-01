import pylab as pl
import sciris as sc

filename = 'data/Okinawa_weather_data.csv'
data = pl.loadtxt(filename, delimiter=';', skiprows=1)

pl.figure()
pl.plot(data[:,5:10], lw=2)

pl.figure()
pl.scatter(data[:,5],data[:,6])
pl.xlabel('temperature (deg C)')
pl.ylabel('rel. humidity')