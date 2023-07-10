Slack Bot

Description

This is a Slack bot that allows users to query a SQLite database using natural language. The bot uses Bard API to convert natural language queries to SQL statements, and then executes them on the database
cursor. The bot responds with the formatted results or an error message if something goes wrong.


Requirements
1. Python 3.6 or higher
2. slack_bolt
3. slack_sdk
4. bardapi
5. query_parser
6. sqlite3
7. scheduler
8. Bard API
9. os
10. logging


Installation

1. Clone this repository and navigate to the project folder.
2. # Python 3.6+ required
    python -m venv .venv
    source .venv/bin/activate
2. Install the required packages using pip install -r requirements.txt.
3. Create a Slack app and enable Socket Mode with the connections:write scope.
4. Generate a bot token (xoxb-) and an app-level token (xapp-) for your Slack app and save them as
environment variables SLACK_BOT_TOKEN and SLACK_APP_TOKEN respectively.
data provided in the data folder.
5. Authentication of Bard API
    Warning Do not expose the __Secure-1PSID

    Visit https://bard.google.com/
    F12 for console
    Session: Application → Cookies → Copy the value of __Secure-1PSID cookie.
    Note that while I referred to __Secure-1PSID value as an API key for convenience,   it    is not an officially provided API key. Cookie value subject to frequent changes. Verify the value again if an error occurs. Most errors occur when an invalid cookie value is entered.

6. Run the bot using python app.py.

Usage
1. Invite the bot to a channel or send a direct message to the bot.
2. Say “hey” to the bot and click on the button to verify if you are allowed to ask questions.
3. Type your natural language query and send it to the bot. For example, “How many users are there in Lucknow?” or “Show me the android details”.
4. The bot will respond with the results or an error message.

Limitations
1. The bot relies on the accuracy and performance of the bardapi service for
converting natural language queries to SQL statements. Some queries may not be parsed correctly or may not be supported by the engine or the service.
2. The bot only supports SQLite databases and queries that can be executed on a single database cursor.
3. Complex queries involving joins, subqueries, transactions, etc. may not work as expected.
The bot does not handle authentication, authorization, encryption, or any other security measures for
accessing the database. Use the bot at your own risk and do not expose sensitive data to the bot or other
users