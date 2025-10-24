# Copyright Kitware Inc. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import (
    maintainers,
    license,
    version,
)


class PyUbelt(PythonPackage):
    """Ubelt is a lightweight library of robust, tested, documented, and simple
    functions that extend the Python standard library
    """

    homepage = "https://ubelt.readthedocs.io/en/latest"
    url = "https://github.com/Erotemic/ubelt"

    maintainers("kwryankrattiger")

    license("Apache-2.0", checked_by="kwryankrattiger")

    version("1.4.0", md5="5c6a90b5153459867f0aca706592fad0")
