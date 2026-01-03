from dataclasses import dataclass
from pathlib import Path
from subprocess import call

@dataclass
class User:
    uid: int | None
    name: str
    comment: str | None
    primary_group: str | None
    supple_group: list[str]
    shell: Path

@dataclass
class Group:
    gid: int
    name: str

def keep_user(u: User):
    rc = call(['id', '-u', u.name])
    if rc == 0: cmd = ['usermod']
    elif rc == 1: cmd = ['useradd']
    else: raise ValueError('id returned neither 0 nor 1')
    cmd += [
        '-G', ','.join(u.supple_group),
        '-s', u.shell,
    ]
    if u.comment: cmd += ['-c', u.comment],
    if u.primary_group: cmd += ['-g', u.primary_group]
    if u.uid: cmd += ['-u', str(u.uid)]
    cmd.append(u.name)
    call(cmd)

def keep_group(g: Group):
    rc = call(['groupmems', '-g', g.name, '-l'])
    if rc == 0:
        call(['groupmod', '-g', str(g.gid), g.name])
    elif rc == 9:
        call(['groupadd', '-g', str(g.gid), g.name])
