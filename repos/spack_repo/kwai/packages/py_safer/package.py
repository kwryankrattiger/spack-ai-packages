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


class PySafer(PythonPackage):
    """safer helps prevent programmer error from corrupting files, socket
    connections, or generalized streams by writing a whole file or nothing.
    """

    homepage = "https://github.com/rec/safer"
    git = "https://github.com/rec/safer"
    pypi = "safer/safer-5.1.0.tar.gz"

    maintainers("kwryankrattiger")

    license("MIT")

    version("5.1.0", md5="c23771809ddbd402306616604f811150")

    depends_on("py-poetry-core", type=("build"))
