from pathlib import Path

for i in range(1, 3333+1):
    if not Path('./json/{}.json'.format(i)).exists():
        url="https://cloudflare-ipfs.com/ipfs/bafybeidkjkldl7ud2zfeimvxzngrcxugv5c7vaesfu22euvuhjd7vuiyoe/{}.json".format(i)
        cmd="wget --user-agent=\"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36\" {}".format(url)
        print(cmd)
