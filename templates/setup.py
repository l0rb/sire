import os

from setuptools import setup


def read(fname):
    """
    Helper to read README
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read().strip()


setup(
    name="{name}",
    version="0.0.1",  # bump2version will edit this automatically!
    description="",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="http://github.com/interrogator/{name}",
    author="Danny McDonald",
    include_package_data=True,
    zip_safe=False,
    packages=["{name}"],
    scripts=[],
    author_email="mcddjx@gmail.com",
    license="MIT",
    keywords=[],
    install_requires=[],
    dependency_links=[],
)
