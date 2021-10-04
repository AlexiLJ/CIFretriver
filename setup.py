from setuptools import setup, find_packages
import pathlib

this_directory = pathlib.Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(

    name='test_user_auth',  # Required
    version='1.0.5',  # Required
    description='User authentication service',  # Optional
    long_description=long_description,
    long_description_content_type='text/markdown', # Optional
    url='https://github.com/AlexiLJ/CIFretriver',  # Optional
    author='O.L.',  
    author_email='leiko.oleksandr@gmail.com',  # Optional
    classifiers=[  # Optional

        'License :: OSI Approved :: MIT License',
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'. See instead 'python_requires' below.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
    # Required
    packages=find_packages(include=['utilities', 'test']),
    python_requires='>=3.6',
    py_modules=["main"],
    install_requires=['pandas','pymatgen', 'pytest'],  # Optional
    entry_points={  # Optional
        'console_scripts': ['cifr=main:app']
        }
)