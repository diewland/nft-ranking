import sys
from pathlib import Path
sys.path.append(str(Path('.').absolute().parent))
from rank import *

URL = 'https://opensea.io/assets/ethereum/0xc6d12b8fc4eedea0163456697e81c8ae84bb0531'

F_1 = 'class'
F_2 = 'outfit'
F_3 = 'eyewear'
F_4 = 'skin'
F_5 = 'headwear'
F_6 = 'special'
ATTRS       = [ F_1, F_2, F_3, F_4, F_5, F_6 ]
CSV_FIELDS += ATTRS

rank(URL, ATTRS, LP_SPEEDBOAT)
