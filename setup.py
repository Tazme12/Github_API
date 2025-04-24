from setuptools import setup, find_packages
setup(
    name="GitHub_API", version="1.0.0", packages=find_packages (), install_requires=[
        "requests"
    ],
    entry_points={
    "console_scripts": [
    "GitHub_API=GitHub_API.backend:main"
    ]
    },
    author="Cameron Thornton",
    author_email="camthornton.07@gmail.com",
    description="A API that uses github to view user data.", long_description=open ("README.md", encoding="utf-8") .read (),
    long_description_content_type="text/markdown", url= "https://github.com/Tazme12/Github_API",
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)