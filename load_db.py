import sqlite3
import pandas as pd
conn= sqlite3.connect("database/hotel_analytics.db")

df= pd.read_csv("data/hotels.csv")
df.to_sql("hotels", conn, if_exists="replace", index=False)

df= pd.read_csv("data/offers.csv")
df.to_sql("offers", conn, if_exists="replace", index=False)

df= pd.read_csv("data/sessions.csv")
df.to_sql("sessions", conn, if_exists="replace", index=False)

df = pd.read_csv("data/clicks.csv")
df.to_sql("clicks", conn, if_exists="replace", index=False)

df = pd.read_csv("data/bookings.csv")
df.to_sql("bookings", conn, if_exists="replace", index=False)

conn.close()


