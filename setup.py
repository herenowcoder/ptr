from setuptools import setup

setup(name='ptr',
      version='0.1.0',
      description='Python google TRanslator script',
      author='Wojciech Kaczmarek',
      author_email='wojtekk@kofeina.net',
      url='http//:github.com/herenowcoder/ptr',

      scripts=['scripts/ptr'],

      install_requires=['selenium'],
)
