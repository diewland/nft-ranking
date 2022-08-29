import sys
from pathlib import Path
sys.path.append(str(Path('.').absolute().parent))
from rank import *

URL = 'https://quixotic.io/asset/0xF811F2D6256C436Ea092B2401FE175167E4BC766'

F_1         = 'Background'
F_2         = 'Spotlight'
F_3         = 'Particles'
F_4         = 'Left Hand'
F_5         = 'Head'
F_6         = 'Eyes'
F_7         = 'Mouth'
F_8         = 'Hairstyle'
F_9         = 'Right Hand'
F_10        = 'Outfits'
ATTRS       = [ F_1, F_2, F_3, F_4, F_5, F_6, F_7, F_8, F_9, F_10 ]
CSV_FIELDS += ATTRS

rank(URL, ATTRS)
