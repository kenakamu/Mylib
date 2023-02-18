import setuptools

setuptools.setup(
    name="mylib",
    version="0.1.5",
    author="ken",
    author_email="kenakamu@microsoft.com",
    description="my library",
    long_description="long description",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6'
)