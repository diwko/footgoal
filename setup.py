from setuptools import setup

setup(name='footgoal',
      version='0.2',
      description='Predict football results',
      url='https://github.com/diwko/footgoal',
      author='Dawid Siwko',
      author_email='dawidsiwko@gmail.com',
      license='MIT',
      packages=['footgoal'],
      include_package_data=True,
      package_data={'footgoal': ['data/classifier_model']},
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
