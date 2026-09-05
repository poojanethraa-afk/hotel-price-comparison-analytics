import pandas as pd

sessions = pd.read_csv("data/sessions.csv")
clicks = pd.read_csv("data/clicks.csv")
bookings = pd.read_csv("data/bookings.csv")

total_searches = len(sessions)
total_clicks = len(clicks)
total_bookings = len(bookings[bookings["booking_status"] == "confirmed"])

print("Searches:", total_searches)
print("Clicks:", total_clicks)
print("Confirmed bookings:", total_bookings)

click_through_rate = (total_clicks / total_searches) * 100
booking_rate = (total_bookings / total_clicks) * 100
overall_conversion = (total_bookings / total_searches) * 100

print("Click-through rate:", round(click_through_rate, 2), "%")
print("Click-to-booking rate:", round(booking_rate, 2), "%")
print("Overall conversion rate:", round(overall_conversion, 2), "%")

#merging tables
clicks_with_device = clicks.merge(sessions, on="session_id")

confirmed_bookings = bookings[bookings["booking_status"] == "confirmed"]

bookings_with_device = confirmed_bookings.merge(sessions, on="session_id")

searches_by_device= sessions.groupby("device_type").size()
clicks_by_device= clicks_with_device.groupby("device_type").size()
bookings_by_device= bookings_with_device.groupby("device_type").size()

print("Searches by device:")
print(searches_by_device)
print("\nClicks by device:")
print(clicks_by_device)
print("\nBookings by device:")
print(bookings_by_device)

conversion_by_device = (bookings_by_device / searches_by_device) * 100
print("\nConversion rate by device (%):")
print(conversion_by_device)