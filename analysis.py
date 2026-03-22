import pandas as pd

data = pd.read_csv("search_evaluation_sample.csv")

print("Total queries evaluated:", len(data))
print("Relevance rating distribution:")
print(data["relevance_rating"].value_counts())