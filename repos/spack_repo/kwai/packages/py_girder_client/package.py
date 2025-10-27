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


class PyGirderClient(PythonPackage):
    """Girder client library.
    """

    homepage = "http://girder.readthedocs.org/en/latest/python-client.html"
    pypi = "girder-client/girder_client-3.2.11.tar.gz"

    maintainers("kwryankrattiger")

    license("Apache-2.0", checked_by="kwryankrattiger")

    version("3.2.11", md5="df13840cae1f7d4b876c89214a32847f")

    depends_on("py-setuptools", type=("build"))
    depends_on("py-setuptools-scm", type=("build"))
    depends_on("py-click@6.7:")
    depends_on("py-diskcache")
    depends_on("py-requests@2.4.2:")
    depends_on("py-requests-toolbelt")
