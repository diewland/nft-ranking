# https://cloudflare-ipfs.com/ipfs/bafybeie6ocfwo2jxmbwfozjcfuqssw6x5uytyvx54ss3unwjmq5jn5ybga/4999
# 0-4999

for (( i=$1; i<=$2; i++ )); do
  url="https://cloudflare-ipfs.com/ipfs/bafybeie6ocfwo2jxmbwfozjcfuqssw6x5uytyvx54ss3unwjmq5jn5ybga/$i"
  wget --user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36" $url
done
