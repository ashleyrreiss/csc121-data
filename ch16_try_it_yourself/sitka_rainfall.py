#----- 16-1 -----#

import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get dates and high temperatures from this file
    dates, rains = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        rain = row[3]
        dates.append(current_date)
        rains.append(rain)
    
    # Plot the high temperatures
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, rains, c='red')

    # Format plot
    ax.set_title("Daily rainfall - 2018\nSitka, Alaska", fontsize=24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Rainfall", fontsize=16)
    ax.tick_params(axis='both', which='minor', width=.25, labelsize=8)

    plt.show()