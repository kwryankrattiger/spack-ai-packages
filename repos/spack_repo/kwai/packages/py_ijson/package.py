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


class PyIjson(PythonPackage):
    """Ijson is an iterative JSON parser with standard Python iterator
    interfaces.
    """

    homepage = "https://github.com/ICRAR/ijson"

    git = "https://github.com/ICRAR/ijson"
    pypi = "ijson/ijson-3.2.1.tar.gz"

    maintainers("kwryankrattiger")

    license("BSD-3-Clause")

    version("3.2.1", md5="b014b3a68d306a6a311451374a0689ba")

    depends_on("py-setuptools@58.0.4:", type=("build"))
