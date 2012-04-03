from distutils.core import setup

setup(
  name = "rax",
  version = "0.2",
  packages = ["rax", "rax.http", "rax.fastcache"],
  requires = ["webob"]
)
