# https://img.tofunft.com/ipfs/bafybeibp3zquj3tsqa2abpugefy2wsoxkxgtt7imj6bsrw3qabi2ekp3au/1.json
# https://cloudflare-ipfs.com/ipfs/bafybeibp3zquj3tsqa2abpugefy2wsoxkxgtt7imj6bsrw3qabi2ekp3au/1.json
# 1-3333

for (( i=$1; i<=$2; i++ )); do
  #url="https://img.tofunft.com/ipfs/bafybeibp3zquj3tsqa2abpugefy2wsoxkxgtt7imj6bsrw3qabi2ekp3au/$i.json"
  url="https://cloudflare-ipfs.com/ipfs/bafybeibp3zquj3tsqa2abpugefy2wsoxkxgtt7imj6bsrw3qabi2ekp3au/$i.json"
  wget --user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36" $url
done
