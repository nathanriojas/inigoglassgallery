import os

def main():

	for files in os.listdir("/home/nathan/inigoglassgallery/nonfunctional"): 
		if str(files) == "Convert.py":
			continue
		os.system("convert " + str(files) + " -quality 80 " + "converted_" + str(files))

main()