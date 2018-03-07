import os

def main():

	for files in os.listdir("/home/nathan/inigoglassgallery/nonfunctional"): 
		if str(files) == "Convert.py":
			continue
		size = (os.stat(files).st_size)/1000
		if size > 600:
			os.system("convert " + str(files) + " -resize 12% " + "resize55_" + str(files))
		elif size > 100:
			os.system("convert " + str(files) + " -resize 27% " + "resize55_" + str(files))
		else: 
			os.system("convert " + str(files) + " -resize 37% " + "resize55_" + str(files))

main()