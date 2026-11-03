pkgname = "neuwld"
pkgver = "0_git20261026"
pkgrel = 0
_commit = "712fa71be579f3796b3cd500de87c736a8617dd7"
build_style = "meson"
configure_args = [
    "-Ddefault_library=both",
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
sha256 = "6821c577f5f3274ed7462247fedcc7e8653758223d9cb95525b2b42d1474fa03"


def post_install(self):
    self.install_license("COPYING")


@subpackage("neuwld-devel")
def _(self):
    self.depends += [pkgname]
    return self.default_devel()
