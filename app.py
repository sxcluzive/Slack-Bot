import os
import sqlite3
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from scheduler import scheduler
from bardapi import Bard
from query_parser import *
import logging


app = App(token=os.environ["SLACK_BOT_TOKEN"])

@app.message("hey")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    #say(f"Hey there <@{message['user']}>!") 
     say(
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"Hey there <@{message['user']}>!, how can I help you"},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Click Here to verify if you are allowed to ask questions"},
                    "action_id": "button_click"
                }
            }
        ],
        text=f"Hey there <@{message['user']}>!"
    )
     
@app.action("button_click")
def approve_request(ack, say):
    # Acknowledge action request
    ack()
    say("Request approved 👍")
    @app.message(".*")
    def answer_query(message, say):
        print(message)
        # Connect to the database
        conn = sqlite3.connect("userdata.db")
        cursor = conn.cursor()
        # Get the user query from the message text
        query = message["text"]
        # Convert the query to SQL using openAI or any other API
        sql = convert_to_sql(query)
        # Execute the SQL query on the database cursor
        try:
            cursor.execute(sql)
            # Fetching the result
            result = cursor.fetchall()
            say(format_result(result))
        except Exception as FatalError:
            say(str("Either we don't have any matching result of your query of something went wrong from our end, please try again with new prompt"))
            
            logging.info(FatalError)


if __name__ == "__main__":
    # Create an app-level token with connections:write scope
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()
    

