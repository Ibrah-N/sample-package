from setuptools import setup, find_packages


# package long description
with open("README.md", 'r', encoding='utf-8') as f:
    description = f.read()


# packge info
AUTHER_NAME = "Ibrah-N"
PACKAGE_NAME = "samplepkg"
AUTHER_EMAIL = "ibrahnfreenlancer@gmail.com"
REPO_NAME = "sample-package"


# package setup
setup(
    name=PACKAGE_NAME, 
    description="It is sample practice package",
    long_description=description, 
    author=AUTHER_NAME, 
    author_email=AUTHER_EMAIL, 
    url=f"https://github/{AUTHER_NAME}/{REPO_NAME}", 
    project_urls = {"Bug Tracker"  : f"https://github/{AUTHER_NAME}/{REPO_NAME}/issues"},
    package_dir={"" : "src"}, 
    packages=find_packages(where="scr")
    # install_requires=[]
    )