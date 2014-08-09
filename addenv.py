from subprocess import Popen, PIPE
import sys, glob, os

#Initial parsing of arguments
envName = sys.argv[-1]
paths = []
if len(sys.argv)==2:
	paths = ["./"]
else:
	for path in sys.argv[1:-1]:
		paths.append(str(path))

def parse(paths):
	"""Parses the paths list and places each into the proper format
	"""
	for path in paths:
		


parse(paths)

#Scan each directory for py files
for path in paths:
	if os.path.isdir(path):
		# Might be dangerous...
		paths.append()
	else:
		print list(glob.glob('*.py'))


#Determine if the virtualenv has been created before
createNew = True
p = Popen("source $(which virtualenvwrapper.sh) && lsvirtualenv", shell=True, stdout=PIPE)
for env in str(p.stdout.read()).split('\n'):
	if env == str(envName):
		createNew = False
		break
	else:
		pass

#create a new virtual environment
if createNew:
	print "Creating new virtual environment"
	p = Popen("source $(which virtualenvwrapper.sh) && mkvirtualenv "+str(envName), shell=True, stdout=PIPE)
	print str(p.stdout.read())
	#scan each directory



		# p = Popen("source $(which virtualenvwrapper.sh) && workon "+str(envName)+"; pip install "+str(package), shell = True, stdout = PIPE)




# if __name__ == "__main__":
# 	filename = sys.argv[-1]