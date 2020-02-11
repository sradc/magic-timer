import setuptools

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

with open("VERSION", "r") as fh:
    VERSION = fh.read()

setuptools.setup(
    name="magic-timer",
    version=VERSION,
    author="Sidney Radcliffe",
    author_email="sidneyradcliffe@gmail.com",
    description="Conveniently get a rough idea of how long things take.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/sradc/magic-timer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)

