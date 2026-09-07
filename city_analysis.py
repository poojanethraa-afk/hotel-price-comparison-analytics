import pandas as pd

sessions = pd.read_csv("data/sessions.csv")
bookings = pd.read_csv("data/bookings.csv")

sessions_by_city = sessions.groupby("city_searched").size()
confirmed_bookings= bookings[bookings["booking_status"] == "confirmed"]

bookings_with_city= confirmed_bookings.merge(sessions, on="session_id")
bookings_by_city= bookings_with_city.groupby("city_searched").size()

conversion_by_city= (bookings_by_city / sessions_by_city) * 100

conversion_by_city= conversion_by_city.sort_values(ascending=True)

print("Conversion rate by city (%):")
print(conversion_by_city.round(2))
conversion_by_city.to_csv("data/conversion_by_city.csv", header=["conversion_rate"])
