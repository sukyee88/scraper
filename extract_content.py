import pandas as pd

df = pd.read_csv('scrape1.csv', index_col=0)

existing_links = list(df['Link'])

link = ['/news/article/cinemark-cnk-stock-poised-for-comeback-in-2023']
print(link[0] in existing_links)
