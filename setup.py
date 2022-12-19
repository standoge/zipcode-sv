from setuptools import setup

readme = open("./README.md", "r")

setup(
    name="zipcode-sv",
    package=["zipcode-sv"],
    version="1.1.1",
    description="Package to get El Salvador zipcodes scrapping it",
    long_description=readme.read(),
    long_description_content_type="text/markdown",
    author="standoge",
    url="https://github.com/standoge/zipcode-sv",
    install_requires=["requests", "beautifulsoup4"],
    keywords=["scrapping", "requests", "beautifulsoup4", "El Salvador"],
    classifiers=[],
    license="GPL3",
    include_package_data=True,
)