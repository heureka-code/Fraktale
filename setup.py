import setuptools
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="Fraktale",
    version="1.0.0",
    author="heureka-code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    description="Darstellung und Berechnung von Juliamengen und der Mandelbrotmenge",
    install_requires=["pillow", "numpy"],
    packages=setuptools.find_packages()
    )
