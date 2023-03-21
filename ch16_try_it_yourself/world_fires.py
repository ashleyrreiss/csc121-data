#----- 16-9 -----#

import csv

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    lons, lats, brights = [], [], []
    for row in reader:
        lons.append(row[1])
        lats.append(row[0])
        brights.append(float(row[2]))

    data = [{
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'text': brights,
        'marker': {
            'size': [.05*bright for bright in brights],
            'color': brights,
            'colorscale': 'YlOrRd',
            'colorbar': {'title': 'Brightness'},
        },
    }]


my_layout = Layout(title='World Fires')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='world_fires.html')
