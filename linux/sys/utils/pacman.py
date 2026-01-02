from pathlib import Path as path

import subprocess
from subprocess import check_call as call
from subprocess import check_output

def strap(
    new_root: path, pkgs: list[str], silent = False,
    pacstrap_options: list[str] = ['-i'],
):
    """
    *new_root*: the root where *pkgs* will be installed.
    *pkgs*: packages to be installed.
    *pacstrap_options*: options passed to ``pacstrap``.
    *silent*: if set to ``True``, the output of ``pacman`` will be redirected to ``/dev/null``.
    """

    stdout = subprocess.DEVNULL if silent else None
    call(['pacstrap'] + pacstrap_options + [new_root] + pkgs, stdout=stdout)

def keep(
    pkgs: list[str],
    install_options: list[str] = [], db_options: list[str] = [],
    uninstall_options: list[str] = ['-nus'],
    silent: bool = False
):
    """
    *pkgs*: packages to be kept explicitly installed.
    *install_options*: options passed to ``pacman -S``.
    *db_options*: options passed to ``pacman -D``.
    *uninstall_options*: options passed to ``pacman -R``.
    *silent*: if set to ``True``, the output of ``pacman`` will be redirected to ``/dev/null``.
    """

    stdout = subprocess.DEVNULL if silent else None
    expect = set(pkgs)

    call(
        ['pacman', '-Syu', '--needed']
        + install_options + pkgs,
        stdout=stdout
    )
    call(
        ['pacman', '-D', '--asexplicit']
        + db_options + pkgs,
        stdout=stdout
    )

    pkgs_explicitly_installed = set(map(
        lambda x: x.split(' ')[0],
        check_output(['pacman', '-Qe']).decode().splitlines(keepends=False)
    ))

    pkgs_to_remove = list(pkgs_explicitly_installed - expect)
    if len(pkgs_to_remove) != 0:
        call(['pacman', '-R'] + uninstall_options + pkgs_to_remove, stdout=stdout)
