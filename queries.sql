-- What's the search-to-click-to-booking funnel, broken down by device type?
SELECT s.device_type, COUNT(DISTINCT s.session_id) AS total_sessions, COUNT(DISTINCT c.click_id) AS total_clicks, COUNT(DISTINCT b.booking_id) AS total_bookings
FROM sessions AS s
LEFT JOIN clicks AS c
ON s.session_id = c.session_id
LEFT JOIN bookings AS b
ON s.session_id = b.session_id AND b.booking_status = 'confirmed'
GROUP BY s.device_type
