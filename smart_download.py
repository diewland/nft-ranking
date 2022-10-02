import os.path
import random
import requests

def smart_download(download_url, from_id, to_id):

    def get_missing_ids():
        missing = []
        for id in range(from_id, to_id+1):
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
        url = download_url.format(random_id)
        output = "{}".format(random_id)

        # log
        print("[{}] {}".format(len(ids), url))

        # download
        hdrs = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        r = requests.get(url, headers=hdrs)
        with open(output, 'wb') as outfile:
            outfile.write(r.content)
