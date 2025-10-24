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


class PyFire(PythonPackage):
    """Python Fire is a library for automatically generating command line
    interfaces (CLIs) from absolutely any Python object.
    """

    homepage = "https://github.com/google/python-fire"

    git = "https://github.com/google/python-fire"
    pypi = "fire/fire-0.7.1.tar.gz"

    maintainers("kwryankrattiger")

    license("Apache-2.0", checked_by="kwryankrattiger")

    version("0.7.1", md5="182fc2764d8e891964ae3ad2861102dd")

    depends_on("py-setuptools@45:", type=("build"))
