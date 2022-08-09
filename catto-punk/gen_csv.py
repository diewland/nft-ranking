import sys
from pathlib import Path
sys.path.append(str(Path('.').absolute().parent))
from rank import *

URL = 'https://quixotic.io/asset/0xd88FB5809a51d5C42fEcF0e69055EEAC0C70b23C'

F_1 = 'Background'
F_2 = 'Body'
F_3 = 'Headgear'
F_4 = 'Mouse'
F_5 = 'Glasses'
ATTRS = [ F_1, F_2, F_3, F_4, F_5 ]
CSV_FIELDS += ATTRS

rank(URL, ATTRS, LP_SPEEDBOAT)
