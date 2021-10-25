import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.LLAW33012021S2FLAC3',
      version='1.0.1',
      description=('Fencey is an application to help users through a fencing issue to either create a form 2 or form 3. If their issue is too complex they are referred to Flinders Legal Clinic.'),
      long_description='# docassemble.LLAW33012021S2FLAC3\r\n\r\nThis application was made by Flinders University in collaboration with Flinders Legal Centre. This application is made for clients who having a fencing issue to provide guidance through their issues. Fency was specifically made for issues regarding the need to replace a fence due to damage or if they have been served with a notice of intention from their neighbour. This application will create a Form 2 or Form 3 depending on the users situation or if the situation is more complex will refer the user to book a consult with Flinders Legal Centre.\r\nThis application does not constitute legal advice nor replaces it.\r\n\r\n## Author\r\n\r\nAnnarose De Ionno, deio0004@flinders.edu.au\r\nJosephine Males, male0056@flinders.edu.au\r\nRumbi Sekete, seke0005@flinders.edu.au\r\nNikki Esmaeili, nikki.esmaeili@flinders.edu.au\r\nChloe Tunstill, tuns0011@flinders.edu.au\r\nKatie Henthorn, hent0023@flinders.edu.au\r\n\r\n',
      long_description_content_type='text/markdown',
      author='Annarose De Ionno',
      author_email='deio0004@flinders.edu.au',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/LLAW33012021S2FLAC3/', package='docassemble.LLAW33012021S2FLAC3'),
     )

