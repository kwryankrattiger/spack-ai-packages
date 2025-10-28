# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import (
    maintainers,
    license,
    version,
    depends_on,
)


class PyLarkCython(PythonPackage):
    """Cython plugin for Lark, reimplementing the 
    LALR parser & lexer for better performance on CPython."""

    homepage = "https://github.com/lark-parser/lark_cython"
    pypi = "lark_cython/lark_cython-0.0.17.tar.gz"

    maintainers("kwryankrattiger", "johnwparent")

    license("MIT", checked_by="johnwparent")

    version("0.0.17", sha256="a311c4dba35a8bc19f623ec6829ff5421d7ff493ea1a64f591a29fb08d90e884")

    depends_on("c", type="build")
    depends_on("py-setuptools", type="build")
    depends_on("py-cython", type=("build", "run"))