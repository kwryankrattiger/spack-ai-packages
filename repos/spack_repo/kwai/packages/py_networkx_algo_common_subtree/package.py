# Copyright Kitware, Inc. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNetworkxAlgoCommonSubtree(PythonPackage):
    """Networkx algorithms for maximum common ordered subtree minors 
    (or embedding) and maximum common subtree isomorphism. 
    Contains pure python and cython optimized versions."""

    homepage = "https://github.com/Erotemic/networkx_algo_common_subtree"
    pypi = "networkx_algo_common_subtree/networkx_algo_common_subtree-0.2.2.tar.gz"


    maintainers("kwryankrattiger", "johnwparent")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("Apache-2.0", checked_by="johnwparent")

    version("0.2.2", sha256="d5ed0eb21c7c59f25cf0f7a34e8aab6599afb4d8d31be8e2cbbeec10e5ed11b8")

    depends_on("py-setuptools", type="build")
    depends_on("py-networkx@2.7:")