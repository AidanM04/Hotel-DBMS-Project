from dotenv import load_dotenv
from pprint import pprint
from json import loads
import requests
import os

load_dotenv()

# Back end connection functions that take specific key strings, sometimes ids, and sometimes json_info as inputs


def get_query_result(get_table):
    API_URL = f"https://8f22-2601-c6-d37f-9f10-39c5-d773-d355-3aea.ngrok-free.app/"
    API_URL += get_table
    result_json = requests.get(API_URL).json()

    return result_json

def add_to_table(add_table, json_arguments):
    API_URL = f"https://8f22-2601-c6-d37f-9f10-39c5-d773-d355-3aea.ngrok-free.app/"
    API_URL += add_table
    result_json = requests.post(API_URL, json= json_arguments, headers= {"Content-Type": "application/json"}).json()

    return result_json

def update_in_table(update_table, identification, json_arguments):
    API_URL = f"https://8f22-2601-c6-d37f-9f10-39c5-d773-d355-3aea.ngrok-free.app/"
    API_URL += f"{update_table}/{identification}"
    result_json = requests.put(API_URL, json= json_arguments, headers= {"Content-Type": "application/json"}).json()

    return result_json

def delete_from_table(delete_table, identification):
    API_URL = f"https://8f22-2601-c6-d37f-9f10-39c5-d773-d355-3aea.ngrok-free.app/"
    API_URL += f"{delete_table}/{identification}"
    result_json = requests.delete(API_URL).json()

    return result_json


# testing block
if __name__ == "__main__":
    #print('\n*** Get Database Query results ***\n')

    function = input("\nPlease enter function name: ")

    input_json = input("\nPlease enter json: ")

    inputjsondict = loads(input_json)

    print(type(inputjsondict))

    #result_json = add_to_table(function, input_json)

    #print("\n")
    #pprint(result_json)