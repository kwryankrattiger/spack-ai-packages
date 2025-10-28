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


class PyKwarray(PythonPackage):
    """The kwarray module implements a small set of pure-python extensions to
    numpy and torch.
    """

    homepage = "https://kwarray.readthedocs.io"
    git = "https://github.com/Kitware/kwarray"
    pypi = "kwarray/kwarray-0.7.1.tar.gz"

    maintainers("kwryankrattiger")

    license("Apache-2.0", checked_by="kwryankrattiger")

    version("0.7.1", md5="109be1584c02ad339ae7a80c7666e9a7")

    depends_on("py-setuptools@41.0.1:", type=("build"))

    depends_on("py-ubelt@1.2.3:")

    depends_on("py-numpy@2.1.0:", when="^python@3.13:")
    depends_on("py-numpy@1.26.0:", when="^python@3.12")
    depends_on("py-numpy@1.23.2:", when="^python@3.11")
    depends_on("py-numpy@1.21.6:", when="^python@3.10")
    depends_on("py-numpy@1.19.3:", when="^python@3.8:3.9")

    depends_on("py-packaging@21.3:")
