import time
import glob
import os
import sys
import configparser

# import config.ini file
config = configparser.ConfigParser()
config.read("dl_clean.conf")

#if -q flag specified, set quite mode
quiet = False
if "-q" in sys.argv:
    quiet = True
    print ("dl_clean started in quiet mode")

# if debug flag, output information about unmoved files
debug = False
if "-debug" in sys.argv:
    debug = True
    print ("dl_clean started in debug mode")

filetypes = list(config["ext"]) # get filetypes defined in config.ini

def move(path):
    # takes the watched directory as first argument
    watched = glob.glob(path) # get contents of watched dir
    if len(watched) == 0:
        pass # pass on empty dir
    else: 
        for file in watched: 
            filename = os.path.basename(file) # file.txt
            name, extension = os.path.splitext(file) # (file, .txt)

            if extension in filetypes: # check for existing rule in config
                os.rename(file, os.environ["HOME"] + config["ext"][extension] + filename)
                if quiet == False: # -q flag
                    os.system("notify-send " + config["ext"][extension] + filename) 
            else: 
                if debug == True:
                    print ("Missing rules for this extensions: " + extension)
            

def run():
    while True:
        time.sleep(3)
        move(sys.argv[1])

if __name__ == "__main__":
    run()