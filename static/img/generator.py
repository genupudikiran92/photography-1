from os import listdir
from os.path import isfile, join

import sys

mypath = sys.argv[1]

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for file in sorted(onlyfiles):
	file = '/img/' + mypath + '/' + file
	print("{{< photo full=\"" + file + "\" thumb=\"" + file + "\" alt=\"\" phototitle=\"\" description=\"\">}}")
	print()
