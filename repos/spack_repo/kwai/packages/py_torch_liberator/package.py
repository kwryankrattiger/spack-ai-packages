# Copyright Kitware, Inc. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTorchLiberator(PythonPackage):
    """Torch Liberator is a Python module containing a set of tools for reading and
writing relevant parts of deep networks."""

    homepage = "https://gitlab.kitware.com/computer-vision/torch_liberator"
    url = "https://files.pythonhosted.org/packages/66/33/cb0d53200183b597a459e5017d5ef2d37730d679feb3088d6dde121a8d7e/torch_liberator-0.2.1-py3-none-any.whl"

    maintainers("kwryankrattiger", "johnwparent")

    license("Apache-2.0", checked_by="johnwparent")

    version("0.2.1", sha256="5aacbfb0327508e3d54e4a8b1cce2ee95b8fa7576da9b8493acac9ecf69e1440")

    depends_on("py-setuptools", type="build")
    depends_on("py-ubelt@1.2.4:")
    depends_on("py-liberator@0.0.1:")
    depends_on("py-torch@1.13.0:", when="python@3.11:4.0")
    depends_on("py-torch@1.11.0:", when="python@3.10:3.11")
    depends_on("py-torch@1.9.0:", when="python@3.9:3.10")
    depends_on("py-torch@1.9.0:", when="python@3.6.0:3.9.0")
    depends_on("py-numpy@1.23.2:", when="python@3.11:4.0")
    depends_on("py-numpy@1.21.6:", when="python@3.10:3.11")
    depends_on("py-numpy@1.19.3:", when="python@3.6:3.10")
    depends_on("py-networkx@2.6.2:", when="python@3.7")
    depends_on("py-networkx@2.5.1:", when="python@3.6:3.7")
    depends_on("py-networkx-algo-common-subtree@0.2.0:")

