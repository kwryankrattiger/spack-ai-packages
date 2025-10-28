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

    # FIXME: Add a build backend, usually defined in pyproject.toml. If no such file
    # exists, use setuptools.
    # depends_on("py-setuptools", type="build")
    # depends_on("py-hatchling", type="build")
    # depends_on("py-flit-core", type="build")
    # depends_on("py-poetry-core", type="build")

    depends_on("py-ubelt@1.3.3:")
    depends_on("py-pandas")
    depends_on("py-kwutil@0.2.3:")
    depends_on("py-pyyaml@6.0.1:")
    depends_on("py-ruamel-yaml@0.17.22:")
    depends_on("py-argcomplete@1.0:")
    depends_on("py-packaging@21.3:")
    depends_on("py-scriptconfig@0.7.9:")
    depends_on("py-rich@12.4.4:")
    depends_on("py-cmd-queue@0.1.18:")
    depends_on("py-dvc@3.7.0:")


