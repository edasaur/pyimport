from subprocess import PIPE, Popen
import sys

virtualEnvNames = sys.argv[1:]



for env in virtualEnvNames:
	p = Popen("source $(which virtualenvwrapper.sh) && rmvirtualenv" + str(env), stdout=PIPE, shell=True)
	print p.stdout.read()