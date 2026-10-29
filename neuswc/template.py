pkgname = "neuswc"
pkgver = "0_git20261002"
_commit = "d1ec3e24c7e0b7400dc5c0e4dfb7194e805a489d"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dudev=enabled",
    "-Dxwayland=enabled",
]
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = [
    "libinput-devel",
    "libxkbcommon-devel",
    "neuwld-devel-static",
    "wayland-protocols",
    "xcb-util-wm-devel",
    "xwayland-devel",
]
pkgdesc = "Library for simple wayland compositors"
license = "MIT"
url = "https://git.sr.ht/~shrub900/neuswc"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "fb00eb77282f34c64be372a5e0730d86b500b27491b041c5cf63a4195cf5fae9"
file_modes = {"usr/bin/swc-launch": ("root", "root", 0o4755)}


def post_install(self):
    self.install_license("LICENSE")


@subpackage("neuswc-devel")
def _(self):
    self.depends += [pkgname]
    return self.default_devel()
