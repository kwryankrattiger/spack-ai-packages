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


class PyScriptconfig(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://gitlab.kitware.com/computer-vision/scriptconfig"
    git = "https://gitlab.kitware.com/computer-vision/scriptconfig"
    pypi = "scriptconfig/scriptconfig-0.8.4.tar.gz"

    maintainers("kwryankrattiger")

    license("Apache-2.0", checked_by="kwryankrattiger")

    version("0.8.4", md5="c6d26793133baff0e22f07a5e8e6b065")

    depends_on("py-ubelt@1.3.6:")
    depends_on("py-pyyaml@6.0.1:", when="^python@3.10:")
    depends_on("py-pyyaml@5.4.1:", when="^python@:3.9")

    depends_on("py-setuptools@58.0.4:", type=("build"))
