pkgname = "neuwld-devel-static"
pkgver = "0_git20260813"
pkgrel = 0
_commit = "554f827cadfdfcc276c709dbffa3b2b04c70cf7c"
build_style = "meson"
configure_args = [
    "-Ddoxygen=enabled",
    "-Ddrivers=intel,nouveau",
    "-Ddrm=enabled",
    "-Dwayland=enabled",
]
hostmakedepends = [
    "doxygen",
    "meson",
    "pkgconf",
]
makedepends = [
    "fontconfig-devel",
    "libdrm-devel",
    "wayland-devel",
]
pkgdesc = "Simple wayland drawing library"
license = "MIT"
url = "https://git.sr.ht/~shrub900/neuwld"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "b2bf77350f260cca046091d28f4a8af89cc495d1d983f3bbed8e2e39f5be86c1"


def post_install(self):
    self.install_license("COPYING")
