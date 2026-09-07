import pandas as pd

bookings = pd.read_csv("data/bookings.csv")
sessions = pd.read_csv("data/sessions.csv")
hotels = pd.read_csv("data/hotels.csv")

confirmed_bookings = bookings[bookings["booking_status"] == "confirmed"]
bookings_with_date= confirmed_bookings.merge(sessions, on="session_id")
bookings_with_date["session_date"]= pd.to_datetime(bookings_with_date["session_date"])
bookings_with_date["month"]= bookings_with_date["session_date"].dt.strftime("%Y-%m")

monthly_revenue = bookings_with_date.groupby("month")["booking_price_eur"].sum()
monthly_commission = bookings_with_date.groupby("month")["commission_eur"].sum()
monthly_bookings = bookings_with_date.groupby("month")["booking_id"].count()

print("Monthly booking price total:")
print(monthly_revenue)
print("\nMonthly commission revenue:")
print(monthly_commission)
print("\nMonthly booking count:")
print(monthly_bookings)

hotel_revenue = bookings_with_date.groupby("hotel_id")["commission_eur"].sum()
top_hotels= hotel_revenue.sort_values(ascending=False).head(10)
print("\nTop 10 hotels by commission revenue:")
print(top_hotels)

top_hotels_named = top_hotels.reset_index().merge(hotels, on="hotel_id")
print("\nTop 10 hotels by commission revenue (with names):")
print(top_hotels_named)
monthly_commission.to_csv("data/monthly_commission.csv", header=["commission_eur"])