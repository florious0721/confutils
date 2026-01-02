import os
import subprocess
import sys

os.chdir(os.getenv('HOME'))

dest = sys.argv[1]
backuplist = [
    '.zen',
    '.config/MusicBrainz',
    '.local/bin',
    '.local/share/applications',
    '.local/share/bash-completion',
    '.local/share/easyeffects',
    '.local/share/fcitx5',
    '.local/share/icons',
    '.local/share/mihomo',
    '.local/share/nvim',
    '.local/share/singbox',
    '.local/share/themes',
]

subprocess.check_call(['tar', '-acf', dest] + backuplist)
