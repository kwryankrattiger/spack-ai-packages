# Copyright Kitware, Inc. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPytorchIgnite(PythonPackage):
    """Ignite is a high-level library to help with training 
    and evaluating neural networks in PyTorch flexibly and transparently."""

    homepage = "https://pytorch-ignite.ai/"
    pypi = "pytorch-ignite/pytorch-ignite-0.5.0.dev20221021.tar.gz"


    maintainers("johnwparent", "kwryankrattiger")


    license("BSD-3-Clause", checked_by="johnwparent")

    version("0.5.0.dev20221021", sha256="75b51b97f8302b42775d094458e1d5e334a5e26325301d36e2a6370a7184a03d")

    depends_on("py-hatchling", type="build")

    depends_on("python@3.9:3.13")
    depends_on("py-torch@1.10:", type=("build", "run"))

