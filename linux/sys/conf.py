from pathlib import Path
from utils.fstab import FstabEntry as Fse

efi = Path('/efi')
confsrc = Path('./etc/')

efidev = Path('/dev/disk/by-label/linuxefi')
rootdev = Path('/dev/disk/by-label/root')
swapdev = Path('/dev/disk/by-label/swap')

ssdopts = 'ssd,noatime,space_cache=v2,compress=zstd'

fstablist = [
    Fse(efidev, Path('/efi'), 'defaults', False, 2),
    Fse(swapdev, None, 'nofail', False, 0),
    Fse(rootdev, Path('/'), 'rw,subvol=/@arch,' + ssdopts, False, 1),
    Fse(rootdev, Path('/dat'), 'rw,subvol=/@data,nofail' + ssdopts, False, 2),
    Fse(rootdev, Path('/home'), 'rw,subvol=/@home,nofail' + ssdopts, False, 2),
]

pkgsA = [
    'base', 'base-devel', 'binutils',
    'coreutils', 'efibootmgr', 'grub',
    'linux', 'linux-lts', 'mkinitcpio', 'systemd',

    'bluez', 'bluez-utils',
    'linux-firmware-atheros',
    'linux-firmware-broadcom',
    'linux-firmware-mediatek',
    'linux-firmware-other',
    'linux-firmware-realtek',

    'inotify-tools', 'cryptsetup', 'gptfdisk',
    'lvm2', 'ncdu', 'parted', 'smartmontools',

    'btrfs-progs', 'dosfstools', 'e2fsprogs',
    'exfatprogs', 'udftools', 'xfsprogs',

    'inetutils', 'iptables-nft', 'iwd', 'net-tools',
    'nftables', 'systemd-resolvconf',

    'lsof', 'man-db', 'man-pages',
    'sysstat', 'usbutils',

    'arch-install-scripts', 'expac', 'reflector',
    'lostfiles', 'pacman', 'pacman-contrib',

    'intel-ucode', 'intel-media-driver',
    'libvpl', 'linux-firmware-intel',
    'vpl-gpu-rt', 'vulkan-intel',

    'mesa', 'mesa-utils',
    'vulkan-mesa-layers', 'vulkan-tools',
    'sdl2',

    # ThinkBook14 2025
    'acpi_call-lts', 'brightnessctl',
    'sof-firmware', 'tlp', 'tp_smapi-lts',

    'bash', 'bash-completion',
    'git',
    'tmux',
    'ed', 'nano', 'neovim',
    'gawk', 'grep', 'sed', 'the_silver_searcher',
    'convmv', 'rsync', 'tree',
]
pkgsB = [
    'gzip', 'xz', 'zstd',
    'squashfs-tools', 'squashfuse',
    '7zip',

    'clang', 'dart-sass', 'dotnet-sdk-8.0',
    'gcc', 'love', 'python', 'scdoc',
    'gdb', 'python-lsp-server', 'strace', 'uncrustify',
    'debuginfod',
    'jq',
    'autoconf', 'cmake', 'meson', 'ninja', 'npm',
    'gtk4', 'pypinyin',
    'python-sphinx', 'python-sphinx-furo',

    'gnupg', 'oath-toolkit', 'pass',

    'aria2', 'curl', 'openssh', 'socat', 'mihomo',

    'alsa-utils', 'lsp-plugins-lv2', 'element',
    'pipewire', 'pipewire-alsa',
    'pipewire-jack', 'pipewire-pulse',
    'pulsemixer',
    'ffmpeg', 'fdkaac', 'mkvtoolnix-cli',
    'opus-tools', 'vorbis-tools', 'opustags',

    'fastfetch', 'fzf',
    'hyperfine', 'moreutils',
    'qrencode', 'zbar',

    'wayland', 'wayland-protocols',
    'wayland-utils', 'wl-clipboard',
    'dbus-broker-units', 'qt5-wayland',
    'qt6-wayland', 'xorg-xwayland',
    'opentabletdriver',

    'noto-fonts', 'noto-fonts-cjk', 'noto-fonts-emoji',
    'ttf-inconsolata',
    'ttf-nerd-fonts-symbols', 'ttf-nerd-fonts-symbols-mono',

    'fcitx5-configtool', 'fcitx5-gtk',
    'fcitx5-qt', 'fcitx5-rime',
    'rime-double-pinyin',

    'hyprland',
    'alacritty', 'foot', 'fuzzel', 'waylock',
    'wev', 'wlr-randr', 'wtype', 'slurp',
    'hypridle', 'xdg-desktop-portal-hyprland',
    'dconf-editor',

    'mpv', 'gimp', 'picard',
    'wf-recorder', 'kdenlive', 'tenacity',
    'easyeffects', 'pavucontrol-qt',
    'imv', 'obs-studio', 'grim',

    'libnotify', 'mako', 'wob',
    'hicolor-icon-theme', 'kvantum', 'kvantum-qt5',

    'android-file-transfer', 'android-tools',

    'aegisub-ttools-meson-git', 'anki-bin',
    'zen-browser-bin', 'waybar-strip',
]
