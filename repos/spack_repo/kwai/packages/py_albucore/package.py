# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAlbucore(PythonPackage):
    """Albucore is a library of optimized atomic functions designed 
    for efficient image processing. These functions serve as the 
    foundation for AlbumentationsX, a popular image augmentation library."""

    homepage = "https://github.com/albumentations-team/AlbumentationsX"
    pypi = "albucore/albucore-0.0.33.tar.gz"

    maintainers("kwryankrattiger", "johnwparent")

    license("MIT", checked_by="johnwparent")

    version("0.0.33", sha256="de320e50587ceb5286125ed4abfdf802a2a7de00c8ce5b042b63e015574b4f76")
    version("0.0.24", sha256="f2cab5431fadf94abf87fd0c89d9f59046e49fe5de34afea8f89bc8390253746")

    depends_on("py-setuptools", type="build")

    depends_on("py-numpy@1.24.4:")
    depends_on("py-typing-extensions@4.9:")
    depends_on("py-stringzilla@3.10.4:")
    depends_on("py-simsimd@5.9.2:")
