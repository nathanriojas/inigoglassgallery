import os

def main():
	
	for files in os.listdir("/home/nathan/inigoglassgallery/pendants"): 
		if str(files) == "Convert.py":
			continue
		os.system("convert " + str(files) + " -quality 80 " + str(files))

main()