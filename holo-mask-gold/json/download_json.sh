# https://api.speedboat.studio/Holo-Mask--Gold/uri/1444
# 0-1444

for (( i=$1; i<=$2; i++ )); do
  url="https://api.speedboat.studio/Holo-Mask--Gold/uri/$i"
  wget --no-cache $url
done
