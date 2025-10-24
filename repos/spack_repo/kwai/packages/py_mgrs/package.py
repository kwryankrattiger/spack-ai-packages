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


class PyMgrs(PythonPackage):
    """Converting to and from MGRS and Decimal Degrees."""

    homepage = "https://github.com/hobuinc/mgrs"
    git = "https://github.com/hobuinc/mgrs"
    pypi = "mgrs/mgrs-1.5.0.tar.gz"

    maintainers("kwryankrattiger")

    license("MIT", checked_by="kwryankrattiger")

    version("1.5.0", md5="88226c656e2c1ea951586bd6b5bbace1")

    depends_on("py-setuptools@58.0.4:", type=("build"))
