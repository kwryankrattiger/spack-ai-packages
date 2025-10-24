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


class PyProgiter(PythonPackage):
    """Prints loop progress. A single-threaded alternative to tqdm."""

    homepage = "https://github.com/Erotemic/progiter"
    git = "https://github.com/Erotemic/progiter"
    pypi = "progiter/progiter-2.0.0.tar.gz"

    maintainers("kwryankrattiger")

    license("Apache-2.0", checked_by="kwryankrattiger")

    version("2.0.0", md5="dd4cf8c7f0d6482245fa261db1b54a95")

    depends_on("py-setuptools@58.0.4:", type=("build"))
    depends_on("py-rich@12.3.0:")
