import logging
import os

from pathlib import Path

log = logging.Logger('Utils', level=logging.WARN)

def symlink(src: Path, dest: Path):
    if not dest.exists():
        if dest.is_symlink():
            log.warning('%s may be a broken symlink, removing it.', dest)
            dest.unlink()
        dest.symlink_to(src)
    elif dest.samefile(src): return
    else:
        log.error("%s exists but it's not the same as %s!", dest, src)

def link_tree(truehome: Path, linkhome: Path):
    def _link(src: Path):
        for p in src.iterdir():
            if p.is_symlink():
                dest = truehome / p.relative_to(linkhome)
                symlink(p.resolve(), dest)
            elif p.is_dir():
                _link(p)
    _link(linkhome)
