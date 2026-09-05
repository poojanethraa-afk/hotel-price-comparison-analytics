import pandas as pd
df= pd.read_csv("data/offers.csv")

# Clean the data by dropping rows with missing prices
df_clean= df.dropna(subset=["price_eur"])

print("Rows before:", len(df), "-> after dropping missing prices:", len(df_clean))

dupes= df_clean.duplicated().sum()

# Drop duplicates
print("Number of duplicate rows:", dupes)

df_clean= df_clean.drop_duplicates()

print("Rows after removing duplicates:", len(df_clean))

hotel_avg= df_clean.groupby("hotel_id")["price_eur"].mean()
df_clean["hotel_avg_price"] = df_clean["hotel_id"].map(hotel_avg)

# Flag prices that are more than 3x this hotel's own average

df_clean["is_outlier"]= df_clean["price_eur"] > (df_clean["hotel_avg_price"] * 3)

# Remove the flagged outlier rows

outliers= df_clean["is_outlier"].sum()
print("Number of outlier rows:", outliers)

df_clean= df_clean[~df_clean["is_outlier"]]
print("Rows after removing outliers:", len(df_clean))

