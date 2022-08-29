import os.path

dl_url = "https://cloudflare-ipfs.com/ipfs/bafybeie6ocfwo2jxmbwfozjcfuqssw6x5uytyvx54ss3unwjmq5jn5ybga/{}"
dl_range = range(0, 4999+1)

for i in dl_range:
    if not os.path.exists("{}".format(i)):
        url = dl_url.format(i)
        print("wget --no-cache {}".format(url))
