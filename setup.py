import setuptools

setuptools.setup(
        name='acdx',
        version='0.0.1',
        url='https://docs.acdx.io/',
        license='GNU General Public License',
        author='Pasha Petukhov',
        author_email='support@acdx.io',
        description='ACDX python library',
        packages=setuptools.find_packages(),
        long_description=open('README.md').read(),
        zip_safe=False,
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Operating System :: OS Independent",
        ],
    )
