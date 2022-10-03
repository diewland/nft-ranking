import sys
from pathlib import Path
sys.path.append(str(Path('.').absolute().parent.parent))
from smart_download import *

URL_DOWNLOAD = "https://cloudflare-ipfs.com/ipfs/bafybeic7pphnmkwee4p4vw7f47c2faw42gtksevak2i7bxahbmlr4ddy6y/{}.json"
FROM_ID = 1
TO_ID = 806

smart_download(URL_DOWNLOAD, FROM_ID, TO_ID)
