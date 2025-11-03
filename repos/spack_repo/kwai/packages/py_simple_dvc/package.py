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


class PySimpleDvc(PythonPackage):
    """This repo aims to simplify DVC to just a data versioning tool
     (ignoring all of the experiment management stuff), 
     as well as provide other simple tools for easier local cache management.
    """
    homepage = "https://gitlab.kitware.com/computer-vision/simple_dvc"
    url = "https://files.pythonhosted.org/packages/d6/03/0e069b151d7814e7aa74b5191c86d229c19d1ffc2bfd849a73c9485bced0/simple_dvc-0.2.1-py3-none-any.whl"

    maintainers("kwryankrattiger", "johnwparent")

    license("Apache-2.0", checked_by="johnwparent")

    version("0.2.1", sha256="7b153e2c101525b467818e9cbb4024cdfb4ee414fb5770dba853e5144e418834")

    depends_on("py-setuptools", type="build")

    depends_on("py-ubelt@1.3.3:", when="python@3.6:")
    depends_on("py-pandas@2.1.1:", when="python@3.12:")
    depends_on("py-pandas@1.5.0:", when="python@3.11:")
    depends_on("py-pandas@1.3.5:", when="python@3.10:")
    depends_on("py-pandas@1.4.0:", when="python@3.8:")
    depends_on("py-pyyaml@6.0:", when="python@:3.12")
    depends_on("py-pyyaml@6.0.1:", when="python@3.12:4")
    depends_on("py-rich@11.2:", when="python@3.6:3.8")
    depends_on("py-rich@12.4.4:", when="python@3.8:")
    depends_on("py-scriptconfig@0.7.9:", when="python@3.8:")
    depends_on("py-packaging@21.3:")
    depends_on("py-ruamel-yaml@0.17.22:")
    depends_on("py-kwutil@0.2.3:")
    depends_on("py-argcomplete@1.0:")
    depends_on("py-cmd-queue@0.1.18:")
    depends_on("py-dvc@3.7.0:")


