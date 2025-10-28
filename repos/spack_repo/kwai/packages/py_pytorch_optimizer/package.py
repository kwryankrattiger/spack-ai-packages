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


class PyPytorchOptimizer(PythonPackage):
    """optimizer & lr scheduler & objective function collections in PyTorch"""

    homepage = "https://github.com/kozistr/pytorch_optimizer"
    pypi = "pytorch_optimizer/pytorch_optimizer-3.8.2.tar.gz"

    maintainers("kwryankrattiger", "johnwparent")


    license("Apache-2.0", checked_by="johnwparent")

    version("3.8.2", sha256="ec2a73dc1ecbd272c25f7caef15032c8b63f4103cd3e30529df76b39be589b08")

    depends_on("py-poetry-core@2.0.0:", type="build")

    depends_on("python@3.8:")
    depends_on("py-torch@1.10:")
