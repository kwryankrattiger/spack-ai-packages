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


class PyCmdQueue(PythonPackage):
    """A Python module for executing a DAG of bash jobs.
    """

    homepage = "https://gitlab.kitware.com/computer-vision/cmd_queue"

    git = "https://gitlab.kitware.com/computer-vision/cmd_queue"
    pypi = "cmd_queue/cmd_queue-0.1.20-py3-none-any.whl"

    maintainers("kwryankrattiger")

    license("APACHE-2.0")

    version(
        "0.1.20",
        sha256="52170bf8d081b8cbafdeede098e3b23d6610f816ed2d52b5819fd563cbbd2bd6",
        url="https://files.pythonhosted.org/packages/45/aa/a090657a9a6f609c8ca19650eb96e1492f1ac2399dfa3238d26330533b4d/cmd_queue-0.1.20-py3-none-any.whl",
        expand=False,
    )

    depends_on("py-setuptools@41.0.1:", type=("build"))
