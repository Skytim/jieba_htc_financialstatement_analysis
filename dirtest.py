import os

for root, dirs, files in os.walk("htc_data"):
    for f in files:
    	if (f!=".DS_Store"):
    		print f
    		