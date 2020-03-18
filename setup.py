import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dj-fine-search-bellomusodiq", # Replace with your own username
    version="0.0.1",
    author="Mayowa Bello",
    author_email="bmayowa25@gmail.com",
    description="A key word based queryset search for django",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bellomusodiq/dj-fine-search",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)