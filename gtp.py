import requests
from concurrent.futures import ThreadPoolExecutor

# Brute-force guessthepin.com

url = 'https://www.guessthepin.com/prg.php'

def myPost(i):
    requests.post(url, data = {'guess': f'{i:04d}'})

with ThreadPoolExecutor(max_workers=10000) as pool:
    pool.map(myPost, [i for i in range (10000)])