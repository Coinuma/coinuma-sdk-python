from setuptools import setup, find_packages

NAME = "coinuma-sdk"
VERSION = "0.2.0"
DESCRIPTION = "A python SDK for the Coinuma Exchange API"
URL = "http://coinuma.com"
URL_DOWNLOAD = "https://github.com/Coinuma/coinuma-sdk-python.git"
REQUIRES = ["requests >= 2.21.0", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author_email="info@coinuma.com",
    url=URL,
    download_url=URL_DOWNLOAD,
    keywords=["Coinuma", "Coinuma API", "Coinuma Exchange", "Coinuma Exchange API SDK"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={
        'coinuma_sdk': ['py.typed']
    },
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
      ]
)
