from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

# all of this is bad placeholder code that I can't really improve on until I know how our actual database is structured and imported / exported to the front end
def get_query_result(placeholder_query_vars):
    input_info = f"idk how this works outside of what I've done for a significantly more simple project, it will most definately be unnecessary here"
    result_json = requests.get(input_info).json()

    return result_json


if __name__ == "__main__":
    print('\n*** Get Database Query results ***\n')

    query_vars = input("\nPlease enter query info: ")

    result_json = get_query_result(query_vars)

    print("\n")
    pprint(result_json)