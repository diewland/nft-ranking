import sys
from pathlib import Path
sys.path.append(str(Path('.').absolute().parent))
from rank import *

URL = 'https://quixotic.io/asset/0xb91b2276bd5A98994Bf1f496E3886f688f8d4581'

F_AURA      = 'aura'
F_WEAPON    = 'weapon'
F_BODY      = 'body'
F_EYE       = 'eye'
F_CLOTHES   = 'clothes'
F_ACC_EAR   = 'accessory_ear'
F_MOUTH     = 'mouth'
F_ACC_FACE  = 'accessory_face'
F_HAIR      = 'hair'
F_HEADGEAR  = 'headgear'
F_STYLE     = 'style'
ATTRS       = [ F_AURA, F_WEAPON, F_BODY, F_EYE, F_CLOTHES, F_ACC_EAR, F_MOUTH, F_ACC_FACE, F_HAIR, F_HEADGEAR, F_STYLE ]
CSV_FIELDS += ATTRS

rank(URL, ATTRS)
