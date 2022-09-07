import os.path
import random
import requests

FROM_ID = 1
TO_ID = 4998
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
URL_DOWNLOAD = "https://cloudflare-ipfs.com/ipfs/QmR4oXfK9Cr6hghQjqkQ2mH8N9h8mR9YFsv1vYzEwJHnZH/{}"

def get_missing_ids():
    missing = []
    for id in range(FROM_ID, TO_ID+1):
        if not os.path.exists("{}".format(id)):
            missing.append(id)
    return missing

def download(url, output):
    r = requests.get(url, headers=headers)
    with open(output, 'wb') as outfile:
        outfile.write(r.content)

while(len(get_missing_ids()) > 0):
    # get missing ids
    ids = get_missing_ids()

    # get random id
    random.shuffle(ids)
    random_id = ids[0]

    # build url
    url = URL_DOWNLOAD.format(random_id)
    output = "{}".format(random_id)

    # log
    print("[{}] {}".format(len(ids), url))

    # download
    r = requests.get(url, headers=HEADERS)
    with open(output, 'wb') as outfile:
        outfile.write(r.content)
