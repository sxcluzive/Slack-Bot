from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_bolt.app.async_app import AsyncApp
from slack_bolt.adapter.socket_mode.async_handler import AsyncSocketModeHandler
from query_parser import *
import os
import time
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

app = AsyncApp(token=os.environ["SLACK_BOT_TOKEN"])


def scheduler():
    while True:
        try:
            # Call the conversations.list method using the WebClient
            for result in client.conversations_list()["channels"]:
                channel_id = result["id"]
                
                # Call the conversations.history method using the WebClient
                history = client.conversations_history(channel=channel_id)
                print(history)
                # Get the timestamp of the first message in the channel
                first_message_ts = history["messages"][0]["ts"]
                # Calculate the time difference between now and the first message
                time_diff = int(time.time()) - int(float(first_message_ts))
                # Calculate the number of hours since the first message
                hours_since_first_message = time_diff // 3600
                # Calculate the number of seconds until the next hour
                seconds_until_next_hour = (hours_since_first_message + 1) * 3600 - time_diff
                # Wait until the next hour to send messages
                time.sleep(seconds_until_next_hour)
                # Send a message to the channel
                response = client.chat_postMessage(
                    channel=channel_id,
                    text="Hello, How can I help you today"
                )
                print("Message sent: ", response["ts"])
        except SlackApiError as e:
            print("Error sending message: {}".format(e))

if __name__ == "__main__":
    client = WebClient(token=os.environ["SLACK_BOT_TOKEN")
    scheduler()
