import requests
import concurrent.futures

base_url = "https://www.geoguessr.com/api/v3/join-codes/"

# Bruteforces join codes, in this case geoguesssr
# Does not actually work because of protection, but would work in theory

def make_request(sequence):
    url = base_url + sequence + "?s=Manual"
    response = requests.get(url)
    return sequence, response.status_code

def try_sequence(sequence):
    status_code = make_request(sequence)
    if status_code != 404:
        print("Tried " + sequence)
        return sequence

def try_all_sequences():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        sequence_futures = []
        for i in range(26):
            for j in range(26):
                for k in range(26):
                    for l in range(26):
                        sequence = chr(ord('A') + i) + chr(ord('A') + j) + chr(ord('A') + k) + chr(ord('A') + l)
                        sequence_futures.append(executor.submit(try_sequence, sequence))
        
        for future in concurrent.futures.as_completed(sequence_futures):
            result = future.result()
            if result:
                print("Found sequence:", result)
                return

try_all_sequences()
