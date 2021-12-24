import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="byfax_sdk",
    version="1.1.0",
    author="ValConsultBy",
    author_email="contact@pamconsult.by",
    description="byFax Python SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/valconsultby/byfax-python",
    project_urls={
        "Bug Tracker": "https://github.com/valconsultby/byfax-python/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)