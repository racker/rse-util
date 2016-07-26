from setuptools import setup, find_packages

setup(
    name = "rax",
    version = "0.2.0",
    description = "A small collection of libraries used by RSE.",
    url = "https://github.com/rackerlabs/rse/",
    maintainer = "ATL Devops",
    maintainer_email = "devops.atl@lists.rackspace.com",
    classifiers = ["Private :: Do Not Upload"],
    packages = find_packages(),
    install_requires = ["webob"]
)
