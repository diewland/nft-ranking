import os.path

#dl_url = "https://img.tofunft.com/ipfs/bafybeibp3zquj3tsqa2abpugefy2wsoxkxgtt7imj6bsrw3qabi2ekp3au/{}.json"
dl_url = "https://cloudflare-ipfs.com/ipfs/bafybeibp3zquj3tsqa2abpugefy2wsoxkxgtt7imj6bsrw3qabi2ekp3au/{}.json"

dl_range = range(1, 3333+1)
#dl_range = range(1500, 2000+1)

for i in dl_range:
    if not os.path.exists("{}.json".format(i)):
        url = dl_url.format(i)
        print("wget --no-cache {}".format(url))
