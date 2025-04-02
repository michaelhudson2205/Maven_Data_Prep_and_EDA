import numpy as np
import pandas as pd

pens = pd.read_excel('data/Pen Sales Data.xlsx')
pens.head()
pens.info()

reviews = pens['Review'].str.split('|')
reviews.head()

pens[['User Name', 'Review Text']] = pd.DataFrame(reviews.to_list())
pens.head()

pens['Leak or Spill'] = pens['Review'].str.contains('leak|spill', regex=True)
pens.head()
