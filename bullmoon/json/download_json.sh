# https://www.bullmoonnft.com/collection1/json/4
# 0-5500

for (( i=$1; i<=$2; i++ )); do
  url="https://www.bullmoonnft.com/collection1/json/$i"
  wget --user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36" $url
done
