import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="sari-field-definitions-generator", # Replace with your own username
    version="0.2.13",
    author="Florian Kräutli",
    author_email="florian.kraeutli@uzh.ch",
    description="A generator for Field Definitions for ResearchSpace and Metaphacts",
    include_package=True,
    install_requires=['pybars3','PyYAML'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/swiss-art-research-net/sari-field-definitions-generator.git",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    package_data={"": ["sariFieldDefinitionsGenerator/templates/*.handlebars"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)