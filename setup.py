from setuptools import setup, find_packages

long_description = """
lxd_container_api is a package to install in a lxd container 
to privide a unified API for starting, stopping, etc applications
in the container.
"""

setup(
    name='lxd_container_api',
    version='0.2',
    description='lxd_container_api',
    long_description=long_description,
    url='',
    author='Marco Duiker',
    author_email='md@md-kwadraat.nl',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='',
    entry_points={
            'console_scripts': [
                'lxd_container_api = lxd_container_api.wrapper:main',
            ]
    },
    packages=find_packages(exclude=[])
)
