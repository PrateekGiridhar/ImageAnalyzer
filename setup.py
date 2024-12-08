from setuptools import setup, find_packages

setup(
    name="stegsolve_clone",
    version="0.1.0",
    description="A Python-based steganography tool inspired by Stegsolve.",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Pillow",  # For image processing
        "PyYAML",  # For configuration handling
    ],
    entry_points={
        'console_scripts': [
            'stegsolve=stegsolve.main:main',
        ],
    },
)