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


class PyDelayedImage(PythonPackage):
    """The delayed image module lets you describe (a tree of) image operations
    to execute.
    """

    homepage = "https://gitlab.kitware.com/computer-vision/delayed_image"

    git = "https://gitlab.kitware.com/computer-vision/delayed_image"
    pypi = "delayed-image/delayed_image-0.4.6.tar.gz"

    maintainers("kwryankrattiger")

    license("APACHE-2.0")

    version("0.4.6", md5="a377fe56172a0051641b3dda8b0a1b78")

    depends_on("py-setuptools@41.0.1:", type=("build"))

    depends_on("py-kwarray@0.6.19:")
    depends_on("py-kwimage@0.11.0:")
    depends_on("py-networkx@2.7:")
    depends_on("py-numpy@1.19.3:")
    depends_on("py-ubelt@1.3.6:")
    depends_on("py-affine@2.3.0:")
