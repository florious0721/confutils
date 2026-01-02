from conf import *
from subprocess import check_call as call
from utils import fstab
from utils import pacman

import logging
import utils

target = Path('/mnt')
confdest = target/'etc'
bootconf = confdest/'cmdline.d/01-root.conf'
ftpath = confdest/'fstab'

call([
    'reflector', '-a', '72',
    '-c', 'CN', '-f', '3',
    '--save', '/etc/pacman.d/mirrorlist'
])
pacman.strap(target, pkgsA)
utils.synca(confsrc, confdest)
fstab.rootopt(rootdev, bootconf)
fstab.genfstab(fstablist, ftpath)
utils.initramfs(target)
utils.bootloader(target, efi)
utils.unlock_root(target)
utils.service_preset(target)
