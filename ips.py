from requests import get
import pyperclip
import argparse


parser = argparse.ArgumentParser(description='IPS v2 (by u/impshum)')
parser.add_argument('length', nargs='?', default=1, type=int)
args = parser.parse_args()

url = f'https://loripsum.net/api/plaintext/{args.length}'
data = get(url).text.strip()
pyperclip.copy(data)
pyperclip.paste()
