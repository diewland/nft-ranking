import sys
from pathlib import Path
sys.path.append(str(Path('.').absolute().parent))
from rank import *

URL = "https://qx.app/asset/0x0a71bAb4673A408465e33B638d41e96F4f1652c4/{}"

rank2(URL, LP_SPEEDBOAT)
