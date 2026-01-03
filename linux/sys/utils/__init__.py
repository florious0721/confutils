from pathlib import Path
from subprocess import check_call

def aurlist(aur: Path, aurlist: Path):
    with open(aurlist, 'wt') as f:
        f.write('SigLevel = Optional TrustAll\nServer = file://' + str(aur))

def synca(src: Path, dest: Path):
    check_call(['rsync', '-lr', '--mkpath', f'{src}/', f'{dest}/'])

def bootloader(root: Path, efi: Path):
    check_call([
        'bootctl', 'install',
        f'--root={root}', f'--esp-path={efi}'
    ])

def initramfs(root: Path | None = None):
    if root: check_call(['arch-chroot', root, 'mkinitcpio', '-P'])
    else: check_call(['mkinitcpio', '-P'])

def unlock_root(root: Path):
    check_call(['arch-chroot', root, 'passwd', '-du', 'root'])

def service_preset(root: Path | None = None):
    if root: check_call(['arch-chroot', root, 'systemctl', 'preset-all'])
    else: check_call(['systemctl', 'preset-all'])

def genlocale():
    check_call(['locale-gen'])
def synctime():
    check_call(['hwclock', '--systohc'])
