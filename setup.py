from setuptools import setup

setup(name='footgoal',
      version='0.2',
      description='Predict football results',
      url='https://github.com/AGHPythonCourse2017/zad3-lysy352',
      author='Dawid Siwko',
      author_email='dawid.siwko@gmail.com',
      license='MIT',
      packages=['footgoal'],
      entry_points={
          'console_scripts': [
              'footgoal = footgoal.main:main'
          ]
      },
      install_requires=[
          'numpy',
          'scipy',
          'scikit-learn',
      ],
      zip_safe=False)
