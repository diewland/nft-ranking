import os.path

#dl_url = "https://www.bullmoonnft.com/collection1/json/{}"
dl_url = "https://www.bullmoonnft.com/collection1/metadata/{}"
dl_range = range(0, 1885+1)

for i in dl_range:
    if not os.path.exists("{}".format(i)):
        url = dl_url.format(i)
        print("wget --no-cache {}".format(url))
