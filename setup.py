from distutils.core import setup
import py2exe, sys, os
		
opts = {
	"py2exe": {
		"excludes": ["_ssl", "_tkinter", "_sqlite3", "scipy", "lxml",
					 "boto", "statsmodels", "pytables", "cython"],
		"dll_excludes": ["w9xpopen.exe"],
		"dist_dir": "dist",
		"compressed": True,
		"optimize": 2,
		"bundle_files": 1,
	}
}
win = [
	{
	"script": "MainWindow.py",
	"icon_resources": [(0, "resources\mainwindow-icon.ico")],
	"dest_base": "biak",
	}
]

setup(windows=win,
	  data_files=[("", ["settings.ini"])],
	  options=opts,
	  zipfile=None,
	  )