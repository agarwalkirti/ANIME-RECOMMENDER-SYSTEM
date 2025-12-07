# to install all dependencies
# udemy\langchain\llmopsProjects\anime_recommender_system\setup.py

from setuptools import setup, find_packages

with open("requirements.txt", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="anime_recommender_system",
    version="0.1",
    author="Kirti",
    packages=find_packages(),   # Automatically finds all packages with __init__.py
    install_requires=requirements,
    include_package_data=True,  # Optional but recommended
)
