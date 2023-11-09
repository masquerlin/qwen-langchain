import requests
import sys,os
root_path = os.path.join(os.path.dirname(__file__),'..')
sys.path.append(os.path.join(os.path.dirname(__file__),'../..'))
sys.path.append(root_path)
from config.load_update_config import read_config, update_config
config = read_config(os.path.join(root_path,'../config/config.yaml'))
local_url = config['url']['local_api_url']


def chat(question, history):
    resp = requests.post(
        url=local_url,
        json={'prompt':question, 'history':history},
        headers={"Content-Type": "application/json;charset=utf-8"}
    )
    return resp.json()['response'], resp.json()['history']

history = []
while True:
    response, history = chat(input("question:"), history)
    print("answer:", response)