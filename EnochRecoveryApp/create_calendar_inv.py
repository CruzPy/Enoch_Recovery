from datetime import datetime, timedelta
from urllib.parse import quote
import pytz


def create_calendar_inv(date_str, time_str, location_str):
    # Combine date and time strings, and convert to a datetime object
    datetime_str = f"{date_str} {time_str}"
    formatted_datetime = datetime.strptime(datetime_str, "%Y-%m-%d %I:%M %p")

    # Assume the input time is in Eastern Standard Time (EST)
    est_timezone = pytz.timezone("America/New_York")
    formatted_datetime = est_timezone.localize(formatted_datetime)

    # Convert local time to UTC
    formatted_datetime_utc = formatted_datetime.astimezone(pytz.utc)

    # Calculate the end time (30 minutes later)
    end_time_utc = formatted_datetime_utc + timedelta(minutes=30)

    # Format datetime in ISO 8601 format
    formatted_datetime_iso = formatted_datetime_utc.strftime("%Y%m%dT%H%M%SZ")
    end_time_iso = end_time_utc.strftime("%Y%m%dT%H%M%SZ")

    # URL encode the location
    encoded_location = quote(location_str)

    # Create the Google Calendar link
    google_calendar_link = (
        f"https://www.google.com/calendar/render?action=TEMPLATE"
        f"&text=Enoch%20Recovery%20DDP%20Orientation"
        f"&dates={formatted_datetime_iso}/{end_time_iso}"
        f"&details=DDP%20Program%20Orientation%20Session%20&location={encoded_location}"
    )

    return google_calendar_link

