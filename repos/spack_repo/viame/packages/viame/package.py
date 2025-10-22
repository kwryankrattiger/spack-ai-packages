# Copyright Kitware Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (BSD-3-Clause)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import (
    depends_on,
    maintainers,
    version,
    variant
)


class Viame(CMakePackage, CudaPackage):
    """Video and Image Analytics for Multiple Environments."""

    homepage = "http://www.viametoolkit.org/"
    url = "https://github.com/viame/VIAME"

    maintainers("kwryankrattiger", "johnwparent")

    license("BSD-3-Clause", checked_by="kwryankrattiger")

    version("1.2.3", md5="0123456789abcdef0123456789abcdef")

    variant(
        "opencv",
        default=True,
        description="Enable OpenCV processes (video readers/simple GUIs)",
    )
    variant(
        "torch",
        default=True,
        description="Enable PyTorch processes (video readers/image filters)",
    )
    variant("python", default=True, description="Enable Python processes")
    variant(
        "tensorflow",
        default=False,
        description="Enable Tensorflow object detectors plugin",
    )
    variant(
        "examples",
        default=True,
        description="Install examples and pre-trained models",
    )

    depends_on("opencv", when="+opencv")
    depends_on("py-pytorch", when="+torch")
    depends_on("py-tensorflow", when="+tensorflow")

    depends_on("python@3.6:", when="+python")
    depends_on("py-pip", when="+python")
    depends_on("py-numpy", when="+python")

    depends_on("cuda@11:12", when="+cuda")
    depends_on("cudnn@9", when="+cuda")

    def cmake_args(self):
        args = [
            # Use Spack installed dependencies
            self.define("VIAME_BUILD_DEPENDENCIES", False),
            # CUDA Acceleration
            self.define_from_variant("VIAME_ENABLE_CUDA", "cuda"),
            self.define_from_variant("VIAME_ENABLE_CUDNN", "cuda"),
            # OpenCV
            self.define_from_variant("VIAME_ENABLE_OPENCV", "opencv"),
            # Python
            self.define_from_variant("VIAME_ENABLE_PYTHON", "python"),
            # PyTorch
            self.define_from_variant("VIAME_ENABLE_PYTORCH", "torch"),
            # Tensorflow
            self.define_from_variant("VIAME_ENABLE_TENSORFLOW", "tensorflow"),
            # Extras
            self.define_from_variant("VIAME_INSTALL_EXAMPLES", "examples"),
            self.define_from_variant("VIAME_DOWNLOAD_MODELS", "examples"),
            self.define("VIAME_ENALBE_DOCS", False),
            # TODO: Add dependencies for additional tools
            self.define("VIAME_ENALBE_VXL", False),
            self.define("VIAME_ENALBE_DIVE", False),
            self.define("VIAME_ENALBE_VIVIA", False),
            self.define("VIAME_ENALBE_DARKNET", False),
            self.define("VIAME_ENALBE_TENSORRT", False),
            self.define("VIAME_ENALBE_BURNOUT", False),
            self.define("VIAME_ENALBE_SMQTK", False),
            self.define("VIAME_ENALBE_KWANT", False),
            self.define("VIAME_ENALBE_LEARN", False),
            self.define("VIAME_ENALBE_SCALLOP_TK", False),
            self.define("VIAME_ENALBE_SEAL", False),
            self.define("VIAME_ENALBE_ITK", False),
            self.define("VIAME_ENALBE_UW_CLASSIFIER", False),
            self.define("VIAME_ENALBE_MATLAB", False),
            self.define("VIAME_ENALBE_LANL", False),
        ]
        return args
