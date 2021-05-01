import pathlib
import os
import sys

def deletee():
	for root,dirs,files in os.walk(os.getcwd()):
		if files=='':
			remove.files('')
		print(root,files)
		print(len(dirs),len(files))
	ch=int(input('1.files\n2.folders\n'))
	if ch==1:
		name=input('name of the file\t')
		os.remove(name)
	if ch==2:
		name=input('name the folder\t')
		os.rmdir(name)
	return create_file()

def make_dir(name):
	os.mkdir(name)
	return create_file()
def create_file():
	name=input('if you want into another directory then write in format dir/file_name.(file extension) or just write file_name.(file extension)')
	with open(name,'a') as files:
		files.close()
def main():
	name=input('name the folder: ')
	if os.path.exists(name):
		print('Folder with this name is also excist,please write another name')
		return main()
	else: make_dir(name)
def rename_all():
	for root,dirs,files in os.walk(os.getcwd()):
		print(root,files)
	name=input('name\t')
	rename=input('new name\t')
	os.rename(name,rename)
if __name__ == '__main__':
	rename_all()