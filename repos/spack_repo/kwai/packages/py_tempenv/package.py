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


class PyTempenv(PythonPackage):
    """Manage environment variables in a temporary scope.
    """

    homepage = "https://github.com/jeking3/tempenv"
    git = "https://github.com/jeking3/tempenv"
    pypi = "tempenv/tempenv-2.1.0.tar.gz"

    maintainers("kwryankrattiger")

    license("MIT", checked_by="kwryankrattiger")

    version("2.1.0", md5="aeaaa613ca8ad32db5a7363b20726f49")
    version("2.0.0", md5="e2a629c4d796135f5d271b06408de678")
    version("1.1.0", md5="0b1648e943fa407741c5857b2ac621f6")
    version("1.0.0", md5="f51baf8fee8f5d52f4b000b76b4a0ed7")

    depends_on("py-setuptools", type=("build"))
