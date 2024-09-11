import requests
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()

DOMAIN = '' # Your domain
TOKEN = os.environ['TOKEN'] # Your token

old_ip = ''

while True:
    new_ip = requests.get('https://icanhazip.com').content.decode('utf-8').strip()

    if new_ip != old_ip:
        old_ip = new_ip
        requests.get(f'https://www.duckdns.org/update?domains={DOMAIN}&token={TOKEN}&ip={new_ip}')

    else: sleep(60)