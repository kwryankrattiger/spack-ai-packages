# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-kwimage-ext
#
# You can edit this file again by typing:
#
#     spack edit py-kwimage-ext
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import (
    maintainers,
    license,
    version,
    extends,
    depends_on,
)


class PyKwimageExt(CMakePackage, CudaPackage):
    """The kwimage_ext module, which contains binary extensions for the kwimage
    module.
    """

    homepage = "https://gitlab.kitware.com/computer-vision/kwimage_ext"

    url = "https://gitlab.kitware.com/computer-vision/kwimage_ext/-/archive/v0.3.1/kwimage_ext-v0.3.1.tar.gz"
    git = "https://gitlab.kitware.com/computer-vision/kwimage_ext.git"

    maintainers("kwryankrattiger")

    license("Apache-2.0", checked_by="kwryankrattiger")

    version(
        "0.3.1",
        sha256="d3f24a19619c916e4e9416ed50423f2d7044e5399669054be82d40455159696e"
    )

    extends("python")

    depends_on("py-cffi@1.15:", type=("build"))
    depends_on("py-scikit-build@0.11:", type=("build"))
    depends_on("py-ubelt@0.10.1:", type=("build"))

    depends_on("py-numpy@2.3.2:")
    depends_on("py-cython@0.29.5:")
    depends_on("py-torch@2.2:")
    depends_on("py-torch@2.2: +cuda", when="+cuda")

    def cmake_args(self):
        return [
            self.define_from_variant("USE_CUDA", "cuda")
        ]
