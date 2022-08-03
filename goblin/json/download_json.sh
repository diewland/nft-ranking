# https://natoboram.gitlab.io/public-gateway-cacher/
# https://cloudflare-ipfs.com/ipfs/bafybeidkjkldl7ud2zfeimvxzngrcxugv5c7vaesfu22euvuhjd7vuiyoe/3333.json

for (( i=$1; i<=$2; i++ )); do
  url="https://cloudflare-ipfs.com/ipfs/bafybeidkjkldl7ud2zfeimvxzngrcxugv5c7vaesfu22euvuhjd7vuiyoe/$i.json"
  wget --user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36" $url
done
