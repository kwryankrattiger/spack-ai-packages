# Copyright Kitware, Inc. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import (
    maintainers,
    license,
    version,
    depends_on,
)


class PyDistinctipy(PythonPackage):
    """distinctipy is a lightweight python package providing functions to
    generate colours that are visually distinct from one another.
    """

    homepage = "https://distinctipy.readthedocs.io/"
    git = "https://github.com/alan-turing-institute/distinctipy"
    pypi = "distinctipy/distinctipy-1.3.4.tar.gz"

    maintainers("kwryankrattiger")

    license("MIT", checked_by="kwryankrattiger")

    version("1.3.4", md5="f5bf5cd679cfb88e510b233774bce2ee")

    depends_on("py-numpy@1.16.3:")
    depends_on("py-pandas@0.24.2:")
    depends_on("py-matplotlib@3.1.0:")
