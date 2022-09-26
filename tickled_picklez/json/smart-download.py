import os.path
import random
import requests

FROM_ID = 0
TO_ID = 6999
URL_DOWNLOAD = "https://cloudflare-ipfs.com/ipfs/QmWPMzDPqbFS6KTaVVU4mZKuWDRKfJjAUM4sBVmtMBMKMo/{}"

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
    hdrs = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    r = requests.get(url, headers=hdrs)
    with open(output, 'wb') as outfile:
        outfile.write(r.content)
