import sys
from setuptools import setup, find_packages
from setuptools._distutils.util import get_platform
from wheel.macosx_libfile import calculate_macosx_platform_tag

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("pyheif/data/version.txt") as f:
    version = f.read().strip()

pyversion = "".join([x for x in sys.version[:4] if x != "."]) # this will fail for Python x.100 or higher


def get_libheif_version():
    try:
        import pyheif
        return pyheif.libheif_version()
    except ImportError:
        pass


setup(
    name="pyheif-iplweb",
    version=version +  ".dev" + get_libheif_version().replace(".", ""),
    packages=["pyheif"],
    package_data={
        "pyheif": [
            "data/*",
            # Include the pre-build .so file with the proper name:
            f"../_libheif_cffi.cpython-{pyversion}-{sys.platform}.so",
        ]
    },
    install_requires=["cffi>=1.0.0"],
    setup_requires=["cffi>=1.0.0", "wheel"],
    # cffi_modules=["libheif/libheif_build.py:ffibuilder"],
    author="Anthony Paes",
    author_email="ant32bit-carsales@users.noreply.github.com",
    description="Python 3.6+ interface to libheif library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires="~=" + sys.version[:4], # this will fail on python x.100 or higher
    options={
        "bdist_wheel": {
            # "plat_name": get_platname(),
            "python_tag": "cp" + pyversion,
        },
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
    ],
    keywords="heif heic",
    url="https://github.com/carsales/pyheif",
)
