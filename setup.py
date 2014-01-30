from distutils.core import setup
import py2exe
import matplotlib

setup(console=['MainWindow.py'],
	  data_files=matplotlib.get_py2exe_datafiles(),
	  )