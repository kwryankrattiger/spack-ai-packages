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


class PyNdsampler(PythonPackage):
    """Fast random access to small regions in large images.
    """

    homepage = "https://ndsampler.readthedocs.io/"
    git = "https://gitlab.kitware.com/computer-vision/ndsampler"
    pypi = "ndsampler/ndsampler-2.0.0.tar.gz"

    maintainers("kwryankrattiger")

    license("Apache-2.0", checked_by="kwryankrattiger")

    version("0.8.1", md5="6f08a26cb423a5dcfb5aa2a58b3afa32")

    depends_on("py-setuptools@41.0.1:", type=("build"))

    depends_on("py-networkx@2.8:")
    depends_on("py-ubelt @ 1.3.6:")
    depends_on("py-parse @ 1.19.0:")
    depends_on("py-xarray@2023.10.0", when="^python@3.13:")
    depends_on("py-xarray@0.17.0:")
    depends_on("py-numpy@2.1.0:", when="^python@3.13:")
    depends_on("py-numpy@1.26.0:", when="^python@3.12")
    depends_on("py-numpy@1.23.2:", when="^python@3.11")
    depends_on("py-numpy@1.21.6:", when="^python@3.10")
    depends_on("py-numpy@1.19.3:")
    depends_on("py-scipy@1.14.1:", when="^python@3.13:")
    depends_on("py-scipy@1.11.2:", when="^python@3.12")
    depends_on("py-scipy@1.9.2:", when="^python@3.11")
    depends_on("py-scipy@1.8.0:", when="^python@3.10")
    depends_on("py-sortedcontainers@2.3.0:")
    depends_on("py-fasteners@0.14.1:")
    depends_on("py-atomicwrites @ 1.3.0:")
    depends_on("py-scikit-learn@1.5.2:", when="^python@3.13:")
    depends_on("py-scikit-learn@1.3.1:", when="^python@3.12")
    depends_on("py-scikit-learn@1.1.3:", when="^python@3.11")
    depends_on("py-scikit-learn@1.1.0:", when="^python@3.10")
    depends_on("py-scikit-learn@1.0.2:")
    depends_on("py-pillow@10.4.0:", when="^python@3.12:")
    depends_on("py-pillow@10.0.0:", when="^python@3.12:")
    depends_on("py-pillow@9.2.0:", when="^python@3.11")
    depends_on("py-pillow@9.1.0:", when="^python@3.10")
    depends_on("py-pyqtree@1.0.0:")
    depends_on("py-kwimage@0.11.1:")
    depends_on("py-kwarray@0.6.19:")
    depends_on("py-kwcoco@0.8.5:")
    depends_on("py-delayed-image@0.4.2:")
