import os

def main():
	
	for files in os.listdir("/home/nathan/inigoglassgallery/pendants"): 
		if str(files) == "Convert.py":
			continue
		os.system("convert " + str(files) + " -resize 55% " + "resize55_" + str(files))

main()