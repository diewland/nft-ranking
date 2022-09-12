# https://www.bittoondao.io/collection1/metadata/1160
# 20220902 0-1800
# 20220903 0-2105
# 20220912 0-2115

for (( i=$1; i<=$2; i++ )); do
  url="https://www.bittoondao.io/collection1/metadata/$i"
  wget --user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36" $url
done
