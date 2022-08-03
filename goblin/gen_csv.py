import sys
from pathlib import Path
sys.path.append(str(Path('.').absolute().parent))
from rank import *

URL = 'https://quixotic.io/asset/0x0f027dD51D793b91e630AdFb268a61A54fe1c7Bc'

F_1 = 'Bg'
F_2 = 'Body'
F_3 = 'Eye'
F_4 = 'Earring'
F_5 = 'Hair'
F_6 = 'Clothing'
F_7 = 'Mouth'
ATTRS       = [ F_1, F_2, F_3, F_4, F_5, F_6, F_7 ]
CSV_FIELDS += ATTRS

rank(URL, ATTRS)
