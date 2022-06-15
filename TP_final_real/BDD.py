from main import *
import json, pickle

def store_v_file():
    for v in vehiculos_API:
        with open('test.json', 'w') as store_file:
            json.dump(v, store_file)
            print(f"client stored")

store_v_file()