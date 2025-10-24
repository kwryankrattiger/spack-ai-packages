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
#     spack install py-kwcoco
#
# You can edit this file again by typing:
#
#     spack edit py-kwcoco
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import (
    maintainers,
    license,
    version,
    depends_on,
)


class PyKwcoco(PythonPackage):
    """The kwcoco package is a Python module and command line utility for
    reading, writing, modifying, and interacting with computer vision datasets
    """

    url = "https://github.com/Kitware/kwcoco"
    pypi = "kwcoco/kwcoco-1.1.0.tar.gz"

    maintainers("kwryankrattiger")

    license("Apache-2.0", checked_by="kwryankrattiger")

    version("0.8.8", md5="")

    depends_on("py-delayed_image@0.4.2:")
    depends_on("py-jsonschema@3.2.0:")
    depends_on("py-kwarray@0.6.19:")
    depends_on("py-kwimage@0.11.1:")
    depends_on("py-packaging@21.3:")
    depends_on("py-parse@1.19.0:")
    depends_on("py-safer@4.4.1:")
    depends_on("py-scriptconfig@0.7.10:")
    depends_on("py-sortedcontainers@2.3.0:")
    depends_on("py-ubelt@1.3.6:")
    depends_on("py-uritools@3.0.0:")

    depends_on("py-xarray@2023.10.0:", when="^python@3.13:")
    depends_on("py-xarray@0.17.0:", when="^python@3.8:3.12")

    depends_on("py-networkx@2.8:")

    depends_on("py-scipy@1.14.1:", when="^python@3.13:")
    depends_on("py-scipy@1.11.2:", when="^python@3.12:")
    depends_on("py-scipy@1.9.2:", when="^python@3.11:")
    depends_on("py-scipy@1.8.0:", when="^python@3.8:3.10")

    depends_on("py-numpy@1.26.0:", when="^python@3.12")
    depends_on("py-numpy@1.23.2:", when="^python@3.11")
    depends_on("py-numpy@1.21.6:", when="^python@3.10")
    depends_on("py-numpy@1.19.3:", when="^python@3.8:3.9")

    depends_on("py-pandas@2.2.3:", when="^python@3.13:")
    depends_on("py-pandas@2.1.1:", when="^python@3.12")
    depends_on("py-pandas@1.5.0:", when="^python@3.11")
    depends_on("py-pandas@1.4.2:", when="^python@3.8:3.10:")

    depends_on("py-scikit-learn@1.1.3:", when="^python@3.11")
    depends_on("py-scikit-learn@1.1.0:", when="^python@3.10")
    depends_on("py-scikit-learn@1.0.2:", when="^python@3.8:3.9")

    depends_on("py-psutil@5.9.6:", when="^python@3.11:")
    depends_on("py-psutil@5.9.1:", when="^python@3.10")
    depends_on("py-psutil@5.7.3:", when="^python@3.9")
    depends_on("py-psutil@5.6.3:", when="^python@3.8")

    depends_on("py-rich@12.3.0:")
