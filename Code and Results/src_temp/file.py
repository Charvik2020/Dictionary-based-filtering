import sys
import glob,os
import re, math


def get_filepaths(directory):
    file_paths = []  # List which will store all of the full filepaths.

    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.

full_file_paths = get_filepaths("original_Images")
file = open("lst.txt","w")

for f in full_file_paths:
	if (f.endswith(".tif") or f.endswith(".TIF")):
		try:
			file.write(f+"\n")
			
		except:
			print('Something went wrong')
			sys.exit(0)
			
file.close()

