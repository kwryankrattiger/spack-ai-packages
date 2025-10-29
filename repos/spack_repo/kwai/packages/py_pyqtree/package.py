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


class PyPyqtree(PythonPackage):
    """
    """

    homepage = "http://github.com/karimbahgat/Pyqtree"
    git = "http://github.com/karimbahgat/Pyqtree"
    pypi = "Pyqtree/Pyqtree-1.0.0.tar.gz"

    maintainers("kwryankrattiger")

    license("MIT", checked_by="kwryankrattiger")

    version("1.0.0", md5="3eb40f0080e2a484df8d85b6f98324be")

    depends_on("py-setuptools", type=("build"))
