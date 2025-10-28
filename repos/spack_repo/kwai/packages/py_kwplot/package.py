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


class PyKwplot(PythonPackage):
    """The kwplot module is a wrapper around matplotlib and can be used for
    visualizing algorithm results.
`   """

    homepage = "https://gitlab.kitware.com/computer-vision/kwplot"
    git = "https://gitlab.kitware.com/computer-vision/kwplot"
    pypi = "kwplot/kwplot-0.3.8.tar.gz"

    maintainers("kwryankrattiger")

    license("Apache-2.0", checked_by="kwryankrattiger")

    version("0.5.4", md5="7de077cd3fe887300fec94cb701889b5")

    depends_on("py-setuptools@41.0.1:", type=("build"))

    depends_on("py-ubelt@1.3.6:")
    depends_on("py-scriptconfig@0.7.3:")
    depends_on("py-kwarray@0.6.19:")
    depends_on("py-kwimage@0.10:")
    depends_on("py-kwutil@0.3.2:")

    depends_on("py-numpy@1.26.0:", when="^python@3.12:")
    depends_on("py-numpy@1.23.2:", when="^python@3.11")
    depends_on("py-numpy@1.21.6:", when="^python@3.10")
    depends_on("py-numpy@1.19.3:")

    depends_on("py-matplotlib@3.9.2:", when="^python@3.13:")
    depends_on("py-matplotlib@3.7.3:", when="^python@3.12")
    depends_on("py-matplotlib@3.6.2:")

    # Optional deps (may require variants?)
    depends_on("py-pandas@2.1.1:", when="^python@3.13:")
    depends_on("py-pandas@1.5.0:")

    depends_on("py-seaborn@0.11.2:")
