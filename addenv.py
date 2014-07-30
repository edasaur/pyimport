from subprocess import Popen, PIPE
import sys

envname = sys.argv[-1]

# try: 
#Determine if the virtualenv has been created before
createNew = True
p = Popen("source $(which virtualenvwrapper.sh) && lsvirtualenv", shell=True, stdout=PIPE)
for env in str(p.stdout.read()).split('\n'):
	if env == str(envname):
		createNew = False
		break
	else:
		pass

#create a new virtual environment if it has not been created before
if createNew:
	print "Creating new virtual environment"
	p = Popen("source $(which virtualenvwrapper.sh) && mkvirtualenv "+str(envname), shell=True, stdout=PIPE)
	print str(p.stdout.read())
	for package in sys.argv[1:-1]:
		p = Popen("source $(which virtualenvwrapper.sh) && workon "+str(envname)+"; pip install "+str(package), shell = True, stdout = PIPE)
		print p.stdout.read()

# except Exception, e:
# 	raise e



# if __name__ == "__main__":
# 	filename = sys.argv[-1]