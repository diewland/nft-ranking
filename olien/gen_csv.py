import sys
from pathlib import Path
sys.path.append(str(Path('.').absolute().parent))
from rank import *

URL = 'https://quixotic.io/asset/0x69a68eb548A37ee475D9f89646945588558796D1'

F_1         = 'Background'
F_2         = 'Body'
F_3         = 'Tattoo'
F_4         = 'Nose'
F_5         = 'Mouth'
F_6         = 'Eyes'
F_7         = 'On eyes'
F_8         = 'Clothes'
F_9         = 'Accessorie'
F_10        = 'Head'
F_11        = 'Smokes'
ATTRS       = [ F_1, F_2, F_3, F_4, F_5, F_6, F_7, F_8, F_9, F_10, F_11 ]
CSV_FIELDS += ATTRS

rank(URL, ATTRS)
