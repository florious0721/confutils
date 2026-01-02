from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from subprocess import check_output

import json
import subprocess

@dataclass
class FstabEntry:
    fs: Path
    mountpoint: Path | None
    options: str
    dump: bool
    fsck: int

def fsinfo(fs: Path) -> dict:
    r = json.loads(check_output(['lsblk', '-fJ', fs]))
    return r['blockdevices'][0]

def fstab_line(entry: FstabEntry) -> str:
    info = fsinfo(entry.fs)
    return 'UUID={} {} {} {} {} {}\n'.format(
        info['uuid'], entry.mountpoint or 'none', info['fstype'],
        entry.options, int(entry.dump), entry.fsck
    )

def genfstab(conf: list[FstabEntry], fstab_path: Path):
    s = ''
    for i in conf:
        s += fstab_line(i)
    with open(fstab_path, 'wt', encoding='utf-8') as f:
        ps = subprocess.Popen(['column', '-t'], stdin=subprocess.PIPE, stdout=f)
        ps.stdin.write(s.encode())
        ps.stdin.close()

def rootopt(fs: Path, opt_path: Path):
    with open(opt_path, 'wt') as f:
        f.write('root=UUID={}'.format(fsinfo(fs)['uuid']))
