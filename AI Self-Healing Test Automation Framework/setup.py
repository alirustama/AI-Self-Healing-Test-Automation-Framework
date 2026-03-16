"""
Setup configuration for WhatsApp AI Automation Framework
Enables pip install -e . for development
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="whatsapp-ai-automation",
    version="1.0.0",
    author="Mohd Rustam Mansoori",
    author_email="aly.rustam.in@gmail.com",
    description="AI-powered WhatsApp Web automation framework with self-healing capabilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alirustama/whatsapp-ai-automation",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Topic :: Communications :: Chat",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest-cov>=4.0.0",
            "pytest-xdist>=3.0.0",
            "pytest-html>=3.2.0",
            "pylint>=2.15.0",
            "black>=23.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "whatsapp-automation=tests.test_send_messages:main",
        ],
    },
)
