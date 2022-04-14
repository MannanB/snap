from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="snap",  # Required
    version="1.0.0",  # Required
    long_description=long_description,  # Optional
    long_description_content_type="text/markdown",  # Optional (see note above)
    url="https://github.com/MannanB/snap",  # Optional
    author="Mannan Bhardwaj",  # Optional
    author_email="mannanb728@gmail.com",  # Optional
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    package_dir={"snap": "snap"},
    packages="snap",
    python_requires=">=3.9",
    install_requires=["aiohttp", "requests"],  # Optional

    project_urls={  # Optional
        "Bug Reports": "https://github.com/MannanB/snap/issues",
        "Source": "https://github.com/MannanB/snap",
    },
)