from setuptools import setup, find_packages
setup(
    name = "ICTCLASTokenizer",
    version = "0.1",
    packages = find_packages(),
    scripts = [],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires = ['docutils>=0.3'],

    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['__init__.py', 'tokenizer.py', '*.so','Data/*.*'],
        # And include any *.msg files found in the 'hello' package, too:
        #'Data': ['*.*'],
    },

    # metadata for upload to PyPI
    author = "Sun Mingming",
    author_email = "sunmingming@gmail.com",
    description = "This is an python wrapper of ICTCLAS for NLTK",
    license = "BSD",
    keywords = "ICTCLAS python NLTK",
    url = "http://example.com/HelloWorld/",   # project home page, if any

    # could also include long_description, download_url, classifiers, etc.
)