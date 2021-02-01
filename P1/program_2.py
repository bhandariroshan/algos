import os
 

def find_files(directory):
	if os.path.isdir(directory):
		files = [directory]
	else:
		files = []
		return files

	all_files = os.listdir(directory)

	for each_file in all_files:
		path = directory + '/' + each_file 

		if os.path.isdir(path):
			files += find_files(path)

		elif os.path.isfile(path):
			files.append(path)
	 
	return files


def test():
    # Test Cases

    # returns 17
    print ("Pass" if (17 == len(find_files('./testdir'))) else "Fail")

    # returns 4
    print ("Pass" if (4 == len(find_files('./testdir/subdir3'))) else "Fail")

    # returns 3
    print ("Pass" if (3 == len(find_files('./testdir/subdir3/subsubdir1'))) else "Fail")

    # returns 0
    print ("Pass" if (0 == len(find_files('./testdir/subdir3/subsubdir1/b.c'))) else "Fail")
      
    
test()