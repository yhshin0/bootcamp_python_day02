import setuptools

'''
with open("README.md", "r") as fh:
    long_description = fh.read()
'''

setuptools.setup(
    name="ai42",
    version="1.0.0",
    author="yshin",
    author_email="yshin@student.42seoul.kr",
    description="ai42",
    long_description="",
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
