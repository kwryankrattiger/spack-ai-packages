# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAlbumentations(PythonPackage):
    """Albumentations is a Python library for image augmentation.
    Image augmentation is used in deep learning and computer vision
    tasks to increase the quality of trained models."""

    homepage = "https://albumentations.ai/"
    pypi = "albumentations/albumentations-2.0.8.tar.gz"

    maintainers("johnwparent", "kwryankrattiger")


    license("MIT", checked_by="johnwparent")

    version("2.0.8", sha256="4da95e658e490de3c34af8fcdffed09e36aa8a4edd06ca9f9e7e3ea0b0b16856")

    depends_on("py-setuptools", type="build")

    depends_on("py-numpy@1.24.4:")
    depends_on("py-scipy@1.10:")
    depends_on("py-pyyaml")
    depends_on("py-typing-extensions@4.9:")
    depends_on("py-pydantic@2.9.2:")
    depends_on("py-albucore@0.0.24")
    depends_on("py-eval-type-backport")

