from distutils.core import setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="django_auth_ldap",
    version="1.2.0",
    description="",
    author="Peter Sagerson",
    maintainer="AGoodId",
    maintainer_email="teknik@agoodid.se",
    url="https://github.com/agoodid/django_auth_ldap",
    license="Custom",
    packages=[
        "django_auth_ldap",
    ],
    long_description=read("README.markdown"),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: Custom",
    ],
)
