pkgname = "neuswc"
pkgver = "0_git20261029"
_commit = "050726e3aa6f084512516e8d563fddbacb8dc2de"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddefault_library=both",
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
    "neuwld-devel",
    "wayland-protocols",
    "xcb-util-wm-devel",
    "xwayland-devel",
]
pkgdesc = "Library for simple wayland compositors"
license = "MIT"
url = "https://git.sr.ht/~shrub900/neuswc"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "b98b96a1f8e37916da5a4072f91aa3e486091d19a3ab8fcbab5aacc78a6fe38e"
file_modes = {"usr/bin/swc-launch": ("root", "root", 0o4755)}


def post_install(self):
    self.install_license("LICENSE")


@subpackage("neuswc-devel")
def _(self):
    self.depends += [pkgname]
    return self.default_devel()
