# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-liberator
#
# You can edit this file again by typing:
#
#     spack edit py-liberator
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyLiberator(PythonPackage):
    """Liberator is a Python library that “liberates” 
    (i.e. statically extracts) class / function 
    source code from an existing python library into a single standalone module."""

    homepage = "https://gitlab.kitware.com/python/liberator"
    url = "https://files.pythonhosted.org/packages/fc/c1/eae54ed45772538913ac182095044f4564b6ce0d70ed2b6eb462fae19d29/liberator-0.1.1-py3-none-any.whl"

    maintainers("kwryankrattiger", "johnwparent")


    license("Apache-2.0", checked_by="johnwparent")

    version("0.1.1", sha256="75d9faf87b6e5e8a0285853097fd5643823d59c84ed143b9be96d948bbe12b9a")


    depends_on("py-setuptools", type="build")

    depends_on("py-astunparse@1.6.3:")
    depends_on("py-ubelt@1.3.3:")
    depends_on("py-pyflakes@2.2.0:")
    depends_on("py-pygtrie@2.3.3:")

