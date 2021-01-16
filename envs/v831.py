
from setuptools import Extension
from .utils import get_srcs

ext_so = "./ext_modules/libmaix/components/libmaix/lib/arch/v831"

# _maix_module = Extension('_maix', include_dirs=['ext_modules/_maix/include'], sources=get_srcs('ext_modules/_maix'), libraries=['jpeg'])
_maix_module = Extension('_maix', include_dirs=['ext_modules/_maix/include', 'ext_modules/libmaix/components/libmaix/include'], 
                        sources=get_srcs('ext_modules/_maix'), 
                        libraries=[
                            "jpeg", "dl", "rt", "log", "ion", "pthread", "cdc_base",
                            "MemAdapter", "media_utils", "mpp_vi", "mpp_isp", "ISP",
                            "mpp_mini", 
                            "maix_utils", "maix_cam", "maix_disp", "maix_image", "maix_nn",
                        ],
                        library_dirs=[ "/lib",  "/usr/lib", ext_so, ],
                        # extra_link_args  = [ "-Wl,-z,origin", "-Wl,-rpath='$ORIGIN/maix'" ]
                        extra_link_args  = [ "-Wl,-rpath=/usr/lib/python3.8/site-packages/maix" ]
                    )
_maix_nn_module = Extension('_maix_nn', include_dirs=['ext_modules/_maix_nn/include', 'ext_modules/libmaix/components/libmaix/include'], 
                        sources=get_srcs('ext_modules/_maix_nn/src'), 
                        libraries=[
                                    "maix_utils", "maix_nn",
                        ],
                        library_dirs=[ "/lib",  "/usr/lib", ext_so, ],
                        # extra_link_args  = [ "-Wl,-z,origin", "-Wl,-rpath='$ORIGIN/maix'" ]
                        extra_link_args  = [ "-Wl,-rpath=/usr/lib/python3.8/site-packages/maix" ]
                    )

_maix_data_files = [
    ('/maix', get_srcs(ext_so, ['so'])),
]
