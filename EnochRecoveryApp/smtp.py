import base64
import os.path
import pickle  # Added import for pickle
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request  # Added import for Request
from requests import HTTPError


# Notification system for client and enoch
def send_orientation_email(receiver_info, google_link):
    SCOPES = ["https://www.googleapis.com/auth/gmail.send"]
    credentials_path = os.path.join(os.path.dirname(__file__), "creds/credentials.json")

    # Load or obtain new credentials
    creds = None
    token_pickle_path = os.path.join(os.path.dirname(__file__), "creds/token.pickle")
    if os.path.exists(token_pickle_path):
        with open(token_pickle_path, "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(token_pickle_path, "wb") as token:
            pickle.dump(creds, token)

    service = build("gmail", "v1", credentials=creds)

    # Send email to Client
    message = MIMEText(
        f"""<html>
            <body>
            <h3>Hi {receiver_info['first_name']},</h3>
                <p>Thank you for registering for our impaired driver program orientation.</p>
                <p>Please do not forget to bring your <b>arrest packet</b> and <b>$233</b> in order to register for the program.</p>
                <p>Orientation Appointment:</p>
                <ul>
                    <li>Date: {receiver_info['date']}</li>
                    <li>Time: {receiver_info['time']}</li>
                    <li>Location: {receiver_info['location']}</li>
                </ul>
                <p><a href="{google_link}">Save to Google Calendar</a></p>
            <h5>If you would like to reschedule your orientation please contact us below:</h5>
            <h5>Email: <a href="mailto:enochrecoveryddp@gmail.com"><b>enochrecoveryddp@gmail.com</a></b></h5>
            <h5>Cell: <b><a href="tel:9176352875">(917) 635-2875</b></a></h5>
            </body>
        </html>""",
        "html",
    )

    # Set headers for the message
    message["to"] = receiver_info["email"]
    message["subject"] = "Enoch Recovery Orientation"

    create_message = {"raw": base64.urlsafe_b64encode(message.as_bytes()).decode()}

    try:
        message = (
            service.users().messages().send(userId="me", body=create_message).execute()
        )
        print(f'sent message to {message} Message Id: {message["id"]}')
    except HTTPError as error:
        print(f"An error occurred: {error}")
        message = None

    message = MIMEText(
        f"""<html>
            <body>
            <h3>Hi Enoch,</h3>
                <p>{receiver_info['first_name']} {receiver_info['last_name']} has registered for orientation</p>
                <p>Here is {receiver_info['first_name']}'s contact info:</p>
                <ul>
                    <li>Phone:<a href="tel:{receiver_info['phone']}">{receiver_info['phone']}</a></li>
                    <li>Email: {receiver_info['email']}</li>
                </ul>
                <p>Orientation Appointment:</p>
                <ul>
                    <li>Date: {receiver_info['date']}</li>
                    <li>Time: {receiver_info['time']}</li>
                    <li>Location: {receiver_info['location']}</li>
                </ul>
                <p><a href="{google_link}">Save to Google Calendar</a></p>
            </body>
        </html>""",
        "html",
    )

    # Set headers for the message
    message["to"] = "enochrecoveryddp@gmail.com"  # TODO: Change to Enochs address
    message["subject"] = "New Orientation Request"

    create_message = {"raw": base64.urlsafe_b64encode(message.as_bytes()).decode()}

    try:
        message = (
            service.users().messages().send(userId="me", body=create_message).execute()
        )
        print(f'sent message to {message} Message Id: {message["id"]}')
    except HTTPError as error:
        print(f"An error occurred: {error}")
        message = None
