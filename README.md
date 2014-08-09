pyimport
========

Module to allow you to automatically import modules

PyImports creates .env files which are hidden from normal view. They should work in much the same way as .git files in which when an environment is loaded up, pyimport first checks to see if a .env file exists in the directory. If there is none specified, pyimport will create a virtual environment that contains all of the imported python modules installed.

Normal syntax of pyImport:

pyImport addEnv [name]
	creates a virtual environment called name

pyImport removeEnv[name]
	removes a virtual environment called name