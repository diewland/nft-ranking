import sys
from pathlib import Path
sys.path.append(str(Path('.').absolute().parent))
from rank import *

URL = "https://opensea.io/assets/ethereum/0xf488a1ac7aadd80755ae4f081a67e1e85820a8c3/{}"

rank2(URL, LP_SPEEDBOAT)
