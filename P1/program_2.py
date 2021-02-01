import os
 

def find_files(suffix, path): 
	files = []
	if os.path.isdir(path):
		all_files = os.listdir(path)

		directories = []
		for each_file in all_files:
			new_path = path + '/' + each_file   
			if os.path.isdir(new_path):
				directories.append(new_path)

			elif os.path.isfile(new_path) and suffix == '':
				files.append(new_path)

			elif os.path.isfile(new_path) and suffix in new_path:
				files.append(new_path)

		for each_directory in directories: 
			files += find_files(suffix, each_directory)
  
	if suffix == '' or os.path.isfile(path + '/' + suffix) or len(files) > 0:
		files.append(path)
	
	return files


def test():
    # Test Cases 
    # should return 17
    print ("Pass" if (17 == len(find_files('', './testdir'))) else "Fail")
 
    # should return 5
    print ("Pass" if (5 == len(find_files('a.c', './testdir'))) else "Fail")

    # should return 0
    print ("Pass" if (0 == len(find_files('a.c', './testdir/subdir3'))) else "Fail")

    # should return 2
    print ("Pass" if (2 == len(find_files('b.c', './testdir/subdir3/subsubdir1'))) else "Fail")
 
    # should return 3
    print ("Pass" if (3 == len(find_files('b.c', './testdir/subdir3'))) else "Fail")

    # should return 4
    print ("Pass" if (4 == len(find_files('b.c', './testdir'))) else "Fail")
      
    
test()