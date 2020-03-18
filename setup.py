import setuptools
from .readme import long_description


setuptools.setup(
    name="dj-fine-search",
    version="0.0.3",
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