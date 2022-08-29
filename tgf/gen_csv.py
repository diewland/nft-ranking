import sys
from pathlib import Path
sys.path.append(str(Path('.').absolute().parent))
from rank import *

#URL = "https://opensea.io/assets/ethereum/0x83186a1d477346ca123ef195413e447c74c6cef7"
URL = "https://cloudflare-ipfs.com/ipfs/bafybeico3kuczc67wj7kracsagie4luzk2wq3ya6oxubwsqqo6lbadmgle/{}.png"

F_1 = 'Background Color'
F_2 = 'Ghost Name'
F_3 = 'Ghost Type'
F_4 = 'Ghost Level'
ATTRS       = [ F_1, F_2, F_3, F_4 ]
CSV_FIELDS += ATTRS

rank(URL, ATTRS, LP_SPEEDBOAT)
