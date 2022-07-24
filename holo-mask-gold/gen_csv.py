import sys
from pathlib import Path
sys.path.append(str(Path('.').absolute().parent))
from rank import *

URL = 'https://quixotic.io/asset/0x8B50FDe10E6D2256b12DD839F92130C5D20c1E51'

F_BG        = 'Background'
F_MASK      = 'Mask'
F_EYE       = 'Eye'
F_MOUTH     = 'Mouth'
F_HEAD      = 'Head'
F_HOLO_SUIT = 'Holo Suit'
ATTRS       = [ F_BG, F_MASK, F_EYE, F_MOUTH, F_HEAD, F_HOLO_SUIT ]
CSV_FIELDS += ATTRS

rank(URL, ATTRS, LP_SPEEDBOAT)
