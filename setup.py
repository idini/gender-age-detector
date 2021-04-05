import setuptools

with open("README.md", "r") as fh:
   long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

   
setuptools.setup(
    name='GenderAgePoc',
    version='0.1Alpha',
    author="Maurizio Idini",
    author_email="maurizio.idini@gmail.com",
    description="Age Gender Recognition",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/idini/gender-age-detector",
    install_requires=required,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)