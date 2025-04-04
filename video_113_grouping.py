"""blah, blah, blah"""

import pandas as pd

data = {
    'type': ['green', 'black', 'black', 'herbal', 'herbal', 'herbal', 'herbal', 'oolong'],
    'name': ['sencha', 'chai', 'ceylon', 'mint', 'ginger', 'chamomile', 'tumeric', 'green oolong'],
    'temp': [180, 210, 200, 212, 212, 200, 175, 190]
}

tea = pd.DataFrame(data)
tea.groupby('type')['temp'].mean().reset_index()

tea.groupby('type')['temp'].agg(
    ['min', 'max', 'count', 'nunique']).reset_index()

(tea.groupby('type')['temp']
 .agg(['min', 'max', 'count', 'nunique'])
 .reset_index())

tea_temps = tea.groupby('type')['temp'].mean().reset_index()
tea_temps.plot.barh()
