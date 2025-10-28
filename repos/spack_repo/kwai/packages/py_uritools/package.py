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


class PyUritools(PythonPackage):
    """This module provides RFC 3986 compliant functions for parsing,
    classifying and composing URIs and URI references, largely replacing the
    Python Standard Library's urllib.parse module.
    """

    homepage = ""
    git = ""
    pypi = "uritools/uritools-5.0.0.tar.gz"

    maintainers("kwryankrattiger")

    license("MIT")

    version("5.0.0", md5="28cf165ca4b711b91bcec2d569cb1415")

    depends_on("py-setuptools@46.4.0:", type=("build"))
