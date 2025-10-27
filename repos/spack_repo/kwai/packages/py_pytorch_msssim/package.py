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


class PyPytorchMsssim(PythonPackage):
    """Fast and differentiable MS-SSIM and SSIM for pytorch.
    """

    homepage = "https://github.com/VainF/pytorch-msssim"

    git = "https://github.com/VainF/pytorch-msssim"
    pypi = "pytorch_msssim/pytorch_msssim-0.1.5.tar.gz"

    maintainers("kwryankrattiger")

    license("MIT", checked_by="zackgalbreath")

    version("0.1.5", md5="9ae8d46eac9ac661c527a1fc6561ad02")

    depends_on("py-setuptools@45:", type=("build"))
    depends_on("py-torch@1.0.0:", type=("build", "run"))
