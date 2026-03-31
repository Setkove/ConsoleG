from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='ConsoleG',
  version='0.1.0',
  author='Setkove',
  author_email='biarslan551@gmail.com',
  description='This Graphics Library',
  long_description=readme(),
  long_description_content_type='The Graphics Library it allows you to create and draw graphics, as well as graphics functions that allow you to create many things',
  url='home_link',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='tkinter',
  project_urls={
        "Homepage": "https://github.com/Setkove/ConsoleG",
        "Repository": "https://github.com/Setkove/ConsoleG",
        "Issues": "https://github.com/Setkove/ConsoleG/issues",
  },
  python_requires='>=3.7'
)