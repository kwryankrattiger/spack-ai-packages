# Copyright Kitware Inc. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import (
    maintainers,
    license,
    version,
    depends_on,
)


class PyUtm(PythonPackage):
    """Bidirectional UTM-WGS84 converter for python"""

    homepage = "pypi.python.org/pypi/utm"
    git = "https://github.com/Turbo87/utm"
    pypi = "utm/utm-0.8.1.tar.gz"

    maintainers("kwryankrattiger")

    license("MIT", checked_by="kwryankrattiger")

    version("0.8.1", sha256="634d5b6221570ddc6a1e94afa5c51bae92bcead811ddc5c9bc0a20b847c2dafa")

    depends_on("py-setuptools@58.0.4:", type=("build"))
    depends_on("py-numpy@2.2:")
