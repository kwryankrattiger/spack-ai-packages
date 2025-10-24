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


class PyKwimage(PythonPackage):
    """The kwimage module handles low-level image operations at a high level.
    """

    homepage = "https://kwimage.readthedocs.io/"
    url = "https://github.com/Kitware/kwimage"

    maintainers("kwryankrattiger")

    license("Apache-2.0", checked_by="kwryankrattiger")

    version("0.11.6", md5="0123456789abcdef0123456789abcdef")

    depends_on("python@3.8:")

    depends_on("py-scipy@1.14.1:", when="^python@3.13:")
    depends_on("py-scipy@1.11.2:", when="^python@3.12")
    depends_on("py-scipy@1.9.2:", when="^python@3.11")
    depends_on("py-scipy@1.7.2:", when="^python@3.10")
    depends_on("py-scipy@1.5.4:", when="^python@3.8:3.9")

    depends_on("py-numpy@2.1.0:", when="^python@3.13:")
    depends_on("py-numpy@1.26.0:", when="^python@3.12")
    depends_on("py-numpy@1.23.2:", when="^python@3.11")
    depends_on("py-numpy@1.21.6:", when="^python@3.10")
    depends_on("py-numpy@1.19.3:", when="^python@3.8:3.9")

    depends_on("py-shapely@2.0.6:", when="^python@3.13:")
    depends_on("py-shapely@2.0.2:", when="^python@3.12")
    depends_on("py-shapely@1.8.5:", when="^python@3.11")
    depends_on("py-shapely@1.8.2:", when="^python@3.10")
    depends_on("py-shapely@1.7.1:", when="^python@3.8:3.9")

    depends_on("py-pillow@10.4.0:", when="^python@3.13:")
    depends_on("py-pillow@10.0.0:", when="^python@3.12")
    depends_on("py-pillow@9.2.0:", when="^python@3.11")
    depends_on("py-pillow@9.1.0:", when="^python@3.10")
    depends_on("py-pillow@8.0.0:", when="^python@:3.9")

    depends_on("py-scikit-image@0.25.1:", when="^python@3.13:")
    depends_on("py-scikit-image@0.22.0:", when="^python@3.12")
    depends_on("py-scikit-image@0.20.0:", when="^python@3.11")
    depends_on("py-scikit-image@0.19.0:", when="^python@3.10")
    depends_on("py-scikit-image@0.18.0:", when="^python@3.9")
    depends_on("py-scikit-image@0.17.2:", when="^python@3.8")

    depends_on("py-networkx@3.0:", when="^python@3.13:")
    depends_on("py-networkx@2.8:", when="^python@3.11:3.12")
    depends_on("py-networkx@2.7:", when="^python@3.8:3.10")

    depends_on("py-ubelt @ 1.3.3:")
    depends_on("py-kwarray@0.6.19:")
    depends_on("py-distinctipy@1.2.1:")
    depends_on("py-parse@1.14.0:")
    depends_on("py-affine@2.3.0:")

    depends_on("py-lazy_loader@0.4:")
