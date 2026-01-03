from conf import *
from subprocess import check_call as call
from utils import fstab
from utils import pacman
from utils.user import User, keep_user, Group, keep_group

import logging
import sys
import utils

target = Path('/')
confdest = target/'etc'
bootconf = confdest/'cmdline.d/01-root.conf'
ftpath = confdest/'fstab'

def all_users(u: list[User]):
    for i in u:
        keep_user(i)
def all_groups(g: list[Group]):
    for i in g:
        keep_group(i)

steps = [
    lambda: call([
        'reflector', '-a', '72',
        '-c', 'CN', '-f', '3',
        '--save', '/etc/pacman.d/mirrorlist'
    ]),
    lambda: pacman.keep(pkgsA + pkgsB + pkgsaur),
    lambda: utils.synca(confsrc, confdest),
    lambda: fstab.rootopt(rootdev, bootconf),
    lambda: fstab.genfstab(fstablist, ftpath),
    lambda: utils.bootloader(target, efi),
    lambda: utils.initramfs(None),
    lambda: utils.service_preset(None),
    lambda: utils.synctime(),
    lambda: utils.genlocale(),
    lambda: all_groups(groups),
    lambda: all_users(users),
]

if len(sys.argv) > 1:
    for i in sys.argv[1:]:
        steps[int(i)]()
else:
    for i in steps:
        i()
