from distutils.core import setup
import py2exe

setup(
    windows=['Calc.py', 'startup.py', 'malware1.py', 'malware2.py'],
    options={'py2exe': {'bundle_files': 1, 'compressed': True}},
    zipfile=None,
    py_modules=['watchdog', 'pytk',]
)
