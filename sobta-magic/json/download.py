import sys
from pathlib import Path
sys.path.append(str(Path('.').absolute().parent.parent))
from smart_download import *

URL_DOWNLOAD = "https://cloudflare-ipfs.com/ipfs/bafybeifuownwzsuifhg5xajhfnbdtyugblnztxwnaf33ixetjxy4ktzcyu/{}.json"
FROM_ID = 1
TO_ID = 559

smart_download(URL_DOWNLOAD, FROM_ID, TO_ID)
