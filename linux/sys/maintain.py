from conf import *
from subprocess import check_call as call
from utils import fstab
from utils import pacman

import logging
import sys
import utils

target = Path('/')
confdest = target/'etc'
bootconf = confdest/'cmdline.d/01-root.conf'
ftpath = confdest/'fstab'

steps = [
    lambda: call([
        'reflector', '-a', '72',
        '-c', 'CN', '-f', '3',
        '--save', '/etc/pacman.d/mirrorlist'
    ]),
    lambda: pacman.keep(pkgsA + pkgsB),
    lambda: utils.synca(confsrc, confdest),
    lambda: fstab.rootopt(rootdev, bootconf),
    lambda: fstab.genfstab(fstablist, ftpath),
    lambda: utils.initramfs(None),
    lambda: utils.bootloader(target, efi),
    lambda: utils.service_preset(None),
]

if len(sys.argv) > 1:
    for i in sys.argv[1:]:
        steps[int(i)]()
else:
    for i in steps:
        i()
