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


class PyKwgis(PythonPackage):
    """GIS tools for geowatch"""

    homepage = "https://gitlab.kitware.com/computer-vision/kwimage"
    git = "https://gitlab.kitware.com/computer-vision/kwgis"
    pypi = "kwgis/kwgis-0.1.2.tar.gz"

    maintainers("kwryankrattiger")

    license("Apache-2.0", checked_by="kwryankrattiger")

    version("0.1.2", md5="e01ac5acd033ecc056a0ea0179635db1")

    depends_on("py-setuptools@41.0.1:", type=("build"))

    depends_on("py-numpy@1.19.3:")
    depends_on("py-scipy@1.8.0:")
    depends_on("py-shapely@2.0.1:")
    depends_on("py-rasterio@1.3.4:")
    depends_on("py-pandas@1.4.2:")
    depends_on("py-scikit-learn@1.0.2:")
    depends_on("py-scikit-image@0.17.2:")

    depends_on("jq@1.2.1:")

    depends_on("py-pyproj@3.6.1:", when="python@3.12:")
    depends_on("py-pyproj@3.4.1:3.5.0", when="python@:3.11")
    depends_on("py-fiona@1.9.5:", when="python@3.12:")
    depends_on("py-fiona@1.8.22:1.9.0", when="python@:3.11")

    depends_on("py-matplotlib@3.6.2:")
    depends_on("py-pillow@10.0.0:")
    depends_on("py-rtree@0.9.7:")
    depends_on("py-mgrs@1.4.3:")

    # Numeric
    depends_on("py-kwarray@0.6.19:")
    depends_on("py-einops@0.6.0:")

    # Utilities
    depends_on("py-rich@12.3.0:")
    depends_on("py-parse@1.19.0:")
    depends_on("py-affine@2.3.0:")
    depends_on("py-ubelt@1.3.6:")
    depends_on("py-xmltodict@0.12.0:")
    depends_on("py-requests@2.27.1:")
    depends_on("py-xarray@0.17.0:")
    depends_on("py-pint@0.18:")
    depends_on("py-pygtrie@2.5.0:")
    depends_on("py-girder-client@3.1.15:")
    depends_on("py-lxml@4.2.4:")
    depends_on("py-pystac-client@0.5.1:")
    depends_on("py-scriptconfig@0.7.10:")
    depends_on("py-networkx@2.8:")
    depends_on("py-python-dateutil@2.8.2:")
    depends_on("py-pytimeparse@1.1.8:")
    depends_on("py-progiter@1.1.0:")

    # Imaging
    depends_on("py-distinctipy@1.2.1:")
    depends_on("py-kwimage@0.10.0:")
    depends_on("py-delayed-image@0.3.1:")
    depends_on("py-tifffile@2021.4.8:")

    # Plotting
    depends_on("py-kwplot@0.4.14:")
    depends_on("py-seaborn@0.11.1:")

    # GIS
    # TODO: Figure out geopandas dependency issue
    # constraint fails to concretize with restricted range
    # depends_on("py-geopandas@0.10.2:0.14.3")
    depends_on("py-geopandas")
    depends_on("py-utm@0.7.0:")
    depends_on("py-geojson@3.1.0:")

    # Misc
    depends_on("py-ruamel-yaml@0.17.22:0.17.32")
    depends_on("py-lazy-loader@0.3:")
    depends_on("py-kwutil@0.2.5:")
    depends_on("py-suntime@1.3.2:")
    depends_on("py-pytz@2024.1:")
