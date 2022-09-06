import sys
from pathlib import Path
sys.path.append(str(Path('.').absolute().parent))
from rank import *

#URL = "https://qx.app/asset/0xCB84Dff87847D8fC9aAD011E2D48b41AddBAA740/{}"
URL = "https://ipfs.io/ipfs/QmX1SBUGgvGyAtgeThWu5KMvMi2vVWSe4xUdUDGekvXWqF/{}.png"

rank2(URL, LP_SPEEDBOAT)
