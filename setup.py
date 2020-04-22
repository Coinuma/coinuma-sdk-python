from setuptools import setup, find_packages

NAME = "coinuma-sdk"
VERSION = "0.2.1"
DESCRIPTION = "A python SDK for the Coinuma Exchange API"
LONG_DESCRIPTION = """
# Welcome to the Coinuma API SDK
Through our cryptocurrency exchange we offer a wide selection of currencies for you to trade. For a complete API request and response reference please check out our [API documentation](https://coinuma.com/developers/docs). If you need additional help in using the API, please visit the [Coinuma website](https://coinuma.com) and reach our support center. 
#### Happy trading!
"""
URL = "https://coinuma.com"
URL_DOWNLOAD = "https://github.com/Coinuma/coinuma-sdk-python.git"
REQUIRES = ["requests >= 2.21.0", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content="text/markdown",
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
