import setuptools
import os

version_file = os.path.join(os.path.dirname(__file__), 'house_price_predictor/VERSION')
with open(version_file) as f:
    _version = f.read().strip()

readme_file = os.path.join(os.path.dirname(__file__), 'README.md')
if os.path.exists(readme_file):
    with open(readme_file, "r", encoding="utf-8") as f:
        long_description = f.read()
else:
    long_description = ""

reqs_file = os.path.join(os.path.dirname(__file__), 'requirements.txt')
def list_reqs(fname=reqs_file):
    with open(fname) as f:
        return f.read().splitlines()
    
#package_dir = os.path.dirname(__file__)

setuptools.setup(
    name="house_price_predictor-skhetarpal",
    version=_version,
    author="Suraj Khetarpal",
    author_email="suraj.khetarpal@gmail.com",
    description="An example package to demonstrate ML deployment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/skhetarpal/ML_Deployment",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    #package_dir={"": package_dir},
    packages=setuptools.find_packages(exclude=('tests',)),
    python_requires=">=3.6",
    install_requires=list_reqs(),
    package_data={'house_price_predictor': ['VERSION']}
)