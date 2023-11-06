import pandas as pd

articles_df = pd.read_csv("shared_articles.csv")

interaction_df = pd.read_csv("users_interactions.csv")


print(articles_df.head(5))

print(interaction_df.head(5))