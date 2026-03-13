import pandas as pd

url = 'https://www.daraz.pk/#hp-categories'

df = pd.read_html(url)
print(df)
