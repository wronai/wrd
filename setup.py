"""
Setup script for WRD (WRonai Development)

This file is provided for backward compatibility with older Python packaging tools.
For new projects, it's recommended to use pyproject.toml with a modern build backend.
"""

import os
import re
from pathlib import Path

from setuptools import find_packages, setup

# Read the README.md file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

def get_version() -> str:
    """Extract version from pyproject.toml"""
    version_file = this_directory / "pyproject.toml"
    version_match = re.search(
        r'^version\s*=\s*["\']([^\"\']*)[\"\']',
        version_file.read_text(encoding="utf-8"),
        re.M,
    )
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string in pyproject.toml")

# Default dependencies
DEFAULT_DEPENDENCIES = [
    "typer[all]>=0.12.3,<1.0.0",
    "rich>=13.7.0,<14.0.0",
    "pyyaml>=6.0.1,<7.0.0",
    "jinja2>=3.1.2,<4.0.0",
    "python-dotenv>=1.0.0,<2.0.0",
    "click>=8.1.7,<9.0.0",
    "pydantic>=2.5.2,<3.0.0",
    "shellingham>=1.5.0,<2.0.0",
]

# Development dependencies
DEV_DEPENDENCIES = [
    "pytest>=7.4.0,<8.0.0",
    "pytest-cov>=4.1.0,<5.0.0",
    "black>=23.7.0,<24.0.0",
    "isort>=5.12.0,<6.0.0",
    "flake8>=6.1.0,<7.0.0",
    "mypy>=1.5.1,<2.0.0",
    "sphinx>=7.0.0,<8.0.0",
    "sphinx-rtd-theme>=1.2.0,<2.0.0",
    "twine>=4.0.0,<5.0.0",
]

# Get package data (non-Python files)
def get_package_data() -> dict[str, list[str]]:
    """Get package data files"""
    package_data = {
        "wrd": [
            "templates/**/*",
            "templates/**/.*",
            "configs/*.yaml",
            "configs/*.yml",
            "*.json",
            "*.md",
        ]
    }
    
    # Include all files in templates directory
    templates_dir = this_directory / "src" / "wrd" / "templates"
    if templates_dir.exists():
        for root, _, files in os.walk(templates_dir):
            if files:  # Only if there are files in the directory
                root_path = Path(root)
                rel_path = root_path.relative_to(this_directory / "src" / "wrd")
                package_data["wrd"].extend(
                    str(rel_path / "*") for _ in files
                )
    
    return package_data


setup(
    name="wrd",
    version=get_version(),
    author="WRonai Team",
    author_email="contact@wronai.com",
    description="WRD (WRonai Development) - A powerful workflow automation tool for developers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wronai/wrd",
    project_urls={
        "Documentation": "https://wronai.github.io/wrd",
        "Source": "https://github.com/wronai/wrd",
        "Tracker": "https://github.com/wronai/wrd/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src", exclude=["tests", "tests.*"]),
    include_package_data=True,
    package_data=get_package_data(),
    python_requires=">=3.8",
    install_requires=DEFAULT_DEPENDENCIES,
    extras_require={
        "dev": DEV_DEPENDENCIES,
    },
    entry_points={
        "console_scripts": [
            "wrd=wrd.cli:app",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Utilities",
    ],
    license="MIT",
    keywords="workflow automation development tools cli",
    zip_safe=False,
)    "data": [
            "pandas>=1.5.0",
            "numpy>=1.24.0",
            "matplotlib>=3.6.0",
        ],
        "web": [
            "fastapi>=0.95.0",
            "uvicorn>=0.20.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "wrd=wrd.__main__:main",
        ],
    },
    include_package_data=True,
    package_data={
        "wrd": ["templates/*", "configs/*"],
    },
)
