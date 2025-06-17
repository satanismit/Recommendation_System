from setuptools import setup, find_packages

setup(
    name="movie-recommendation",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "flask",
        "python-dotenv",
        "requests",
        "pandas",
        "numpy",
        "scikit-learn",
    ],
    author="Preet Rank",
    author_email="preetrank53@example.com",
    description="A movie recommendation system",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/satanismit/Recommendation_System.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
) 