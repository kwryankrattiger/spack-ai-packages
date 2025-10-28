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


class PySuntime(PythonPackage):
    """Simple sunset and sunrise time calculation python library.
    """

    homepage = "https://github.com/SatAgro/suntime"
    git = "https://github.com/SatAgro/suntime"
    pypi = "suntime/suntime-1.3.2.tar.gz"

    maintainers("kwryankrattiger")

    license("LGPLv3")

    version("1.3.2", md5="0f6226410557351f4a21786ffade7c79")

    depends_on("py-setuptools@41.0.1:", type=("build"))
