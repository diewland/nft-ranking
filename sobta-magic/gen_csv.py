import sys
from pathlib import Path
sys.path.append(str(Path('.').absolute().parent))
from rank import *

URL = "https://qx.app/asset/0x2A6D4EA1c0ef6060665AbB853523807E8f3f2873/{}"

rank2(URL, LP_SPEEDBOAT)
