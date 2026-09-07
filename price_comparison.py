import pandas as pd

offers = pd.read_csv("data/offers_clean.csv")

cheapest_idx= offers.groupby(["hotel_id", "date_scraped"])["price_eur"].idxmin()
cheapest_offers = offers.loc[cheapest_idx]
cheapest_counts= cheapest_offers["provider_name"].value_counts()
print(cheapest_counts)
cheapest_counts.to_csv("data/cheapest_by_provider.csv", header=["times_cheapest"])