* :file:`/dat` Permanent storage.
  * :file:`aur`
    * :file:`pkgs` Packages built from :file:`../repos`.
    * :file:`repos` Repositories on `AUR <https://aur.archlinux.org>`_.
  * :file:`bin` Applications not managed by a package manager.
  * :file:`etc` Configuration moved from user's home directory for permanent storage.
  * :file:`links` Symlinks from :file:`/dat` to user's home directory.
  * :file:`usr`
    * :file:`archive`
    * :file:`audio`
    * :file:`documents`
    * :file:`pictures`
    * :file:`videos`
  * :file:`var`
    * :file:`cache` Cache for package manages and build tools.
    * :file:`downloads`
    * :file:`projects`
    * :file:`work`

* :file:`/home/aaaa` User's home directory.
  * :file:`.local/crypt` Mountpoint of the encrypted device.
  * :file:`.gnupg` -> :file:`.local/crypt/.gnupg`
  * :file:`.password-store` -> :file:`.local/crypt/.password-store`
  * :file:`.ssh` -> :file:`.local/crypt/.ssh`
