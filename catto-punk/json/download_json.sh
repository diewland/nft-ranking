# https://api.speedboat.studio/CattoPunk-01/uri/10000
# 0-10000

for (( i=$1; i<=$2; i++ )); do
  url="https://api.speedboat.studio/CattoPunk-01/uri/$i"
  wget --no-cache $url
done
