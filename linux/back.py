import os
import subprocess
import sys

os.chdir(os.getenv('HOME'))

dest = sys.argv[1]
backuplist = [
    '.zen',
    '.config/MusicBrainz',
    '.local/share/Anki2',
    '.local/share/applications',
    '.local/share/bash-completion',
    '.local/share/fcitx5',
    '.local/share/homebank',
    '.local/share/icons',
    '.local/share/nvim',
    '.local/share/singbox',
    '.local/share/themes',
]

subprocess.check_call(['tar', '-acf', dest] + backuplist)
