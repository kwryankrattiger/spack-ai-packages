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


class PyPortion(PythonPackage):
    """The portion library provides data structure and operations for
    intervals in Python.
    """

    homepage = "https://github.com/AlexandreDecan/portion"

    git = "https://github.com/AlexandreDecan/portion"
    pypi = "portion/portion-2.6.1.tar.gz"

    maintainers("kwryankrattiger")

    license("LGPL-3.0-only")

    version("2.6.1", md5="aeac36a6949dfa5f38722fdf56e0fd0e")

    depends_on("py-hatchling", type="build")
