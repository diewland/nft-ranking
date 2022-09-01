import sys
from pathlib import Path
sys.path.append(str(Path('.').absolute().parent))
from rank import *

URL = 'https://opensea.io/assets/ethereum/0xc6d12b8fc4eedea0163456697e81c8ae84bb0531'

rank2(URL, LP_SPEEDBOAT)
