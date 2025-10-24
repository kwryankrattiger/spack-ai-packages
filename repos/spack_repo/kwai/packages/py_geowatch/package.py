# Copyright Kitware, Inc. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import (
    depends_on,
    license,
    conflicts,
    maintainers,
    version,
    variant
)


class PyGeowatch(PythonPackage):
    """GeoWATCH is a PyTorch tool for training image detection models."""

    homepage = "https://github.com/Kitware/geowatch"
    pypi = "geowatch/geowatch-1.1.0.tar.gz"

    maintainers("kwryankrattiger")

    license("Apache-2.0", checked_by="kwryankrattiger")

    version("0.19.0")

    depends_on("python@3.8:")

    # The following is translated directly from geowatch/rc/requirements/runtime.txt
    # TODO: cleanup the python version constraints
    depends_on("py-numpy@2.1.0:" , when="^python@3.13:")
    depends_on("py-numpy@1.26.0:", when="^python@3.12")
    depends_on("py-numpy@1.23.2:", when="^python@3.11")
    depends_on("py-numpy@1.21.6:", when="^python@:3.10")

    depends_on("py-scipy@1.14.1:", when="^python@3.13:")
    depends_on("py-scipy@1.11.2:", when="^python@3.12")
    depends_on("py-scipy@1.9.2:" , when="^python@3.11")
    depends_on("py-scipy@1.8.0:" , when="^python@:3.10")

    depends_on("py-shapely@2.0.6:", when="^python@3.13:")
    depends_on("py-shapely@2.0.2:", when="^python@3.12")
    depends_on("py-shapely@2.0.1:", when="^python@3.11")
    depends_on("py-shapely@2.0.1:", when="^python@:3.10")

    depends_on("py-rasterio@1.3.11:", when="^python@3.13:")
    depends_on("py-rasterio@1.3.9:", when="^python@3.12")
    depends_on("py-rasterio@1.3.5:", when="^python@3.11")
    depends_on("py-rasterio@1.3.5:", when="^python@:3.10")

    depends_on("py-pandas@2.2.3:", when="^python@3.13:")
    depends_on("py-pandas@2.1.1:", when="^python@3.12")
    depends_on("py-pandas@1.5.3:", when="^python@3.11")
    depends_on("py-pandas@1.5.3:", when="^python@:3.10")

    depends_on("py-scikit-learn@1.5.2:", when="^python@3.13:")
    depends_on("py-scikit-learn@1.3.1:", when="^python@3.12")
    depends_on("py-scikit-learn@1.1.3:", when="^python@3.11")
    depends_on("py-scikit-learn@1.1.0:", when="^python@:3.10")

    depends_on("py-scikit-image@0.25.1:", when="^python@3.13:")
    depends_on("py-scikit-image@0.22.0:", when="^python@3.12")
    depends_on("py-scikit-image@0.20.0:", when="^python@3.11")
    depends_on("py-scikit-image@0.19.0:", when="^python@:3.10")

    depends_on("jq@1.8:")

    depends_on("jsonschema@4.19.2:")

    depends_on("py-pyproj@3.7.0:", when="^python@3.13:")
    depends_on("py-pyproj@3.6.1:", when="^python@3.12")
    depends_on("py-pyproj@3.4.1:3.4", when="^python@3.11")
    depends_on("py-pyproj@3.3.1:3.4", when="^python@:3.10")

    depends_on("py-fiona@1.10.0:", when="^python@3.13:")
    depends_on("py-fiona@1.9.5:", when="^python@3.12")
    depends_on("py-fiona@1.8.22:1.8", when="^python@3.11")
    depends_on("py-fiona@1.8.22:1.8", when="^python@:3.10")

    depends_on("py-matplotlib@3.9.2:", when="^python@3.13:")
    depends_on("py-matplotlib@3.8.2:", when="^python@:3.12")

    depends_on("py-pillow@11.3.0:", when="^python@3.13:")
    depends_on("py-pillow@10.2.0:", when="^python@:3.12")

    depends_on("psutil@5.9.6:")

    depends_on("py-rtree@1.2.0:")

    depends_on("sqlalchemy@1.4.50:")

    depends_on("py-xxhash@3.4.1:")

    # xdev availpkg numexpr
    depends_on("py-numexpr@2.10.2:", when="^python@3.13:")
    depends_on("py-numexpr@2.8.7:", when="^python@3.12")
    depends_on("py-numexpr@2.8.4:", when="^python@3.11")
    depends_on("py-numexpr@2.8.1:", when="^python@:3.10")

    # Numeric
    depends_on("py-xarray@2023.10.0:")

    depends_on("py-einops@0.8.0:", when="python@3.13:")
    depends_on("py-einops@0.6.0:", when="python@:3.12")

    depends_on("py-dask+array@2025.2.0:", when="^python@3.13:")
    depends_on("py-dask+array@2023.5.0:", when="^python@:3.12")

    # Utilities
    depends_on("py-rich@12.5.1:")
    depends_on("py-textual@0.1.18:")
    depends_on("py-text_unidecode@1.3:")
    depends_on("py-configargparse@1.7.1:")
    depends_on("py-parse@1.19.0:")
    depends_on("py-affine@2.3.0:")
    depends_on("py-xmltodict@0.12.0:")
    depends_on("py-Pygments@2.12.0:")
    depends_on("py-requests@2.27.1:")
    depends_on("py-fasteners@0.17.3:")

    depends_on("py-blake3@1.0.1:", when="^python@3.12:")
    depends_on("py-blake3@0.3.1:", when="^python@3.11")
    depends_on("py-blake3@0.2.1:", when="^python@:3.10")

    depends_on("py-more_itertools@8.12.0:")

    depends_on("py-pint@0.24.4:", when="^python@3.13:")
    depends_on("py-pint@0.23:", when="^python@:3.12")

    depends_on("py-lxml@5.3.0:", when="^python@3.11:")
    depends_on("py-lxml@4.6.3:", when="^python@:3.10")

    depends_on("py-pystac_client@0.5.1:")

    depends_on("py-pygtrie@2.5.0:")

    depends_on("py-networkx@3.0.0:", when="^python@3.13:")
    depends_on("py-networkx@2.8.0:", when="^python@:3.12")

    depends_on("py-python_dateutil@2.8.2:")
    depends_on("py-pytimeparse@1.1.8:")

    # Parsing
    depends_on("py-lark@1.1.7:")

    depends_on("py-tifffile@2022.8.12:", when="^python@3.12:")
    depends_on("py-tifffile@2021.4.8:", when="^python@3.12:")

    # Plotting
    depends_on("py-seaborn@0.13.0:")

    depends_on("py-geopandas@0.14.4:1.0.0", when="^python@3.13:")
    depends_on("py-geopandas@0.10.2:1.0.0", when="^python@:3.12")

    depends_on("py-geojson@3.1.0:", when="^python@3.12:")
    depends_on("py-geojson@3.0.1:", when="^python@:3.11")

    # Machine learning

    depends_on("py-torch@2.6.0:", when="^python@3.13:")
    depends_on("py-torch@2.2.0:", when="^python@3.12")
    depends_on("py-torch@2.0.0:", when="^python@3.11")
    depends_on("py-torch@1.12.0:", when="^python@:3.10")

    depends_on("py-torchvision@0.21.0:", when="^python@3.13:")
    depends_on("py-torchvision@0.17.0:", when="^python@3.12")
    depends_on("py-torchvision@0.15.1:", when="^python@3.11")
    depends_on("py-torchvision@0.13.0:", when="^python@:3.10")

    depends_on("py-torchmetrics@0.11.0:")

    depends_on("py-omegaconf@2.3:")
    depends_on("py-hydra-core@1.3.2:")

    depends_on("py-jsonargparse@4.19.0: +signatures")
    depends_on("py-pytorch_lightning@2.0.8:")
    conflicts("py-pytorch_lightning@2.3,2.4.0")

    depends_on("py-monai@1.3.2:", when="^python@3.13:")
    depends_on("py-monai@0.8.0:", when="^python@3.11:3.12")
    depends_on("py-monai@0.6.0:", when="^python@:3.10")

    depends_on("py-timm@0.6.13:0.9.0", when="^python@3.11:")
    depends_on("py-timm@0.4.12:0.9.0", when="^python@:3.10")

    depends_on("py-kornia@0.6.8:")
    depends_on("py-segmentation-models-pytorch@0.2.0:")

    depends_on("py-ujson@5.6.0:", when="^python@3.11:")
    depends_on("py-ujson@5.2.0:", when="^python@:3.10")

    depends_on("py-py-cpuinfo@9:")

    depends_on("py-ruamel.yaml@0.17.22:0.17.32")

    depends_on("py-lazy_loader@0.4:")

    depends_on("py-colormath@3.0.0:")

    depends_on("py-imagesize@1.4.1:")

    depends_on("py-absl_py@1.4.0:")

    depends_on("py-pyyaml@6.0.2:")
    depends_on("py-tqdm@4.64.1:")

    depends_on("py-fsspec@2023.6.0:")
    depends_on("py-s3fs@2023.6.0:")

    depends_on("py-transformers@4.37.2:")
    depends_on("py-ubelt@1.3.6:")

    # Missing in spack
    # vvvvvvvvvvvvvvvv
    #   portion>=2.4.1

    #   ijson>=3.2.1 ; python_version < '4.0'  and python_version >= '3.13'    # Python 3.13+
    #   ijson>=3.2.1 ; python_version < '3.13' and python_version >= '3.12'    # Python 3.12
    #   ijson>=3.2.1 ; python_version < '3.12' and python_version >= '3.11'    # Python 3.11
    #   ijson>=3.2.1 ; python_version < '3.11' and python_version >= '3.10'    # Python 3.10

    #   cmd_queue >= 0.1.20
    #   pytorch_msssim==0.1.5


    #   torch_optimizer>=0.1.0
    #   torch_liberator>=0.2.1
    #   rgd_imagery_client>=0.2.7
    #   rgd_client>=0.2.7
    #   utm>=0.7.0
    #   # Plotting
    #   kwplot>=0.4.14
    #   # GIS
    #   # Note: kwgis contains tools that have historically lived in geowatch 
    #   # We are gradually transitioning this codebase to use those instead of
    #   # internal variants to maintain a more modular software stack. 
    #   kwgis>=0.1.1

    #   lark_cython >= 0.0.16

    #   # Imaging
    depends_on("py-distinctipy@1.2.1:")
    depends_on("py-kwimage@0.11.2:")
    depends_on("py-kwimage_ext@0.2.1:")
    depends_on("py-kwcoco@0.8.5:")
    #   kwcoco_dataloader>=0.1.1
    #   delayed_image>=0.4.5

    #   # Try 1.3.1?
    #   albumentations==1.0.0  # pinned for invariants model

    #   ndsampler>=0.8.0
    depends_on("pogiter@2.0.0:")
    #   fire>=0.4.0
    #   tempenv>=0.2.0
    #   scriptconfig>=0.8.2
    #   girder_client>=3.1.15
    #  kwutil>=0.3.4
    #  simple_dvc>=0.2.1
    depends_on("py-kwarray@0.6.19:")
    #  # xdev availpkg mgrs
    #  mgrs>=1.4.6     ; python_version < '4.0'  and python_version >= '3.12'    # Python 3.12+
    #  mgrs>=1.4.6     ; python_version < '3.12' and python_version >= '3.11'    # Python 3.11
    #  mgrs>=1.4.3     ; python_version < '3.11' and python_version >= '3.10'    # Python 3.10
