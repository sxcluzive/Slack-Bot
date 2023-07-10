import sqlite3
from bardapi import Bard
import os
# Connect to the database
conn = sqlite3.connect("userdata.db")

# Create a cursor
cursor = conn.cursor()

def get_table_name():
    # Execute the query to get the list of tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")

    # Fetch the results
    results = cursor.fetchone()

    # Close the connection
    conn.close()

    return results[0]


def convert_to_sql(query):
    token = os.environ['_BARD_API_KEY']
    bard = Bard(token=token)
    unfiltered_output = bard.get_answer("What is the SQL query to {} for the for sqlite database having table name ('users') where column names are only ('acquisition_campaign', 'android_manufacturer', 'android_model', 'android_os_version', 'android_app_version', 'acquisition_campaign', 'acquisition_source', 'city', 'state', 'onboarding_time', 'phone_carrier', 'phone_screen_dpi', 'phone_screen_height', 'phone_screen_width', 'name', 'age')".format(query))['content']

    text = unfiltered_output.replace('```', '')
    start = text.find('SELECT')
    end = text.find(';')

    if start != -1 and end != -1:
        raw_sql_query = text[start:end+1]
        print("executed query: ", raw_sql_query)
        return raw_sql_query
    else:
        return ("I couldn't run the query, Please try again with similiar keyword")
    

def format_result(result):
    final_output = ""
    for row in result:
        final_output += f"{row}\n"
    return final_output