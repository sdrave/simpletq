from setuptools import setup, find_packages

setup(
    name='simpletq',
    version='0.1.dev2',
    description='A very simple task queue',
    #long_description=long_description,
    url='https://github.com/sdrave/simpletq',
    author='Stephan Rave',
    author_email='mail@stephanrave.de',
    license='BSD License',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Other Audience',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering',
        'Topic :: System :: Distributed Computing',
        'Topic :: Utilities',
    ],
    keywords='task queue job management',
    scripts=['stq.py']
)
