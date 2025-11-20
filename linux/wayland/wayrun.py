from functools import reduce
from pathlib import Path
from setting import *

def wayrun_sh(p: Path):
    with open(p, 'wt') as f:
        f.write('#!/bin/bash\n')
        for k, v in ENV.items():
            f.write(f"export {k}='{v}'\n")
        f.write(f'dbus-run-session -- {Apps.WM}')

