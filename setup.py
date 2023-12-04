from setuptools import setup, find_packages

setup(
    name='image_based_robot_env',
    version='0.0.1',
    packages=find_packages(),  # Automatically discover and include all packages
    install_requires=['gym'],  # And any other dependencies required
)