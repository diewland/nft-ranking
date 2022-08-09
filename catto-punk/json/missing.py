import os.path

for i in range(0, 10000+1):
    if not os.path.exists(str(i)):
        url = "https://api.speedboat.studio/CattoPunk-01/uri/{}".format(i)
        print("wget --no-cache {}".format(url))
