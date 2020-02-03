import requests
import pyperclip
import argparse
from dotenv import load_dotenv
import os

def count_clicks(token, bitlink):
    url_template = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'
    url = url_template.format(bitlink)
    payload = {'unit':'day', 'units': -1}
    headers={'Authorization': token}
    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    return response.json()['total_clicks']

def shorten_link(token, link):
    url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {'Authorization': token}
    payload = {'long_url': link}
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()['link']

def main():

    load_dotenv()

    parser = argparse.ArgumentParser(description='Сокращённые ссылки')
    parser.add_argument('url', type=str, help='Исходная ссылка')

    args = parser.parse_args()

    token = os.getenv('BITLY_TOKEN')

    try:
        if args.url.startswith('bit.ly'):
            clicks_count = count_clicks(token, args.url)
        else:
            bitlink = shorten_link(token, args.url)
    except requests.exceptions.HTTPError as e:
        clicks_count = None
        bitlink = None
        print(e)
    if args.url.startswith('bit.ly') and clicks_count:
        print('Всего кликов:', clicks_count)
    elif not args.url.startswith('bit.ly') and bitlink:
            print('Битлинк', bitlink)
            pyperclip.copy(bitlink) 

if __name__ == '__main__':
    main()
