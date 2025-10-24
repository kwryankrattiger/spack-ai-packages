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


class PyKwutil(PythonPackage):
    """The Kitware utility module."""

    homepage = "https://ubelt.readthedocs.io/en/latest"
    git = "https://gitlab.kitware.com/computer-vision/kwutil"
    pypi = "kwutil/kwutil-0.3.8.tar.gz"

    maintainers("kwryankrattiger")

    license("Apache-2.0", checked_by="kwryankrattiger")

    version("0.3.8", md5="f5253f307299b94f8c0577f05e635847")

    depends_on("py-setuptools@58.0.4:", type=("build"))

    depends_on("py-ubelt@1.3.6:")
    depends_on("py-lazy-loader@0.1:")
    depends_on("py-progiter@1.1.0:")

    # Optional deps (may require variants?)
    depends_on("py-numpy@2.1.0:", when="^python@3.13:")
    depends_on("py-numpy@1.26.0:", when="^python@3.12")
    depends_on("py-numpy@1.23.2:", when="^python@3.11")
    depends_on("py-numpy@1.21.6:", when="^python@3.10")
    depends_on("py-numpy@1.19.3:")

    depends_on("py-py-cpuinfo@9.0.0:")
    depends_on("py-fasteners@0.16.3:")
    depends_on("py-text-unidecode@1.3:")
    depends_on("py-pytimeparse@1.1.8:")
    depends_on("py-parse@1.19.0:")
    depends_on("py-python-dateutil@2.8.2:")
    depends_on("py-rich@12.3.0:")
    depends_on("py-ruamel-yaml@0.17.22:")
    depends_on("py-pyyaml@6.0.1:")
    depends_on("py-pygtrie@2.5.0:")

    depends_on("py-pint@0.24.4:", when="^python@3.13:")
    depends_on("py-pint@0.23:", when="^python@3.12")
    depends_on("py-pint@0.18:")

    depends_on("py-psutil@5.9.6:", when="^python@3.13:")
    depends_on("py-psutil@5.9.1:", when="^python@3.12")
    depends_on("py-psutil@5.9.1:", when="^python@3.11")
    depends_on("py-psutil@5.7.3:", when="^python@3.10")
    depends_on("py-psutil@5.6.3:")
