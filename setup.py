from setuptools import setup, find_packages

setup(
    name="iqoptionapi",
    version="0.2.0",
    description="Wrapper Python para IQ Option API",
    author="",
    author_email="",
    url="https://github.com/itmanagersupport/iqoptionapi_",
    packages=find_packages(),
    install_requires=["pylint", "requests", "websocket-client"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
)
