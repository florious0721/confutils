import os

from utils import link_tree
from pathlib import Path

HOME = Path(os.getenv('HOME'))
LINKHOME = Path('/dat/links/')

link_tree(HOME, LINKHOME)
