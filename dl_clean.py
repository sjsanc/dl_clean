import time
import glob
import os
import sys
import configparser

# import config.ini file
config = configparser.ConfigParser()
config.read("config.ini")

# rule = config["ext"]
# for value in rule: 
#     print (value)

# if -q flag specified, set quite mode
quiet = False;
if len(sys.argv) > 2 and sys.argv[2] == "-q":
    quiet = True

debug = True #

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
                    os.system("notify-send" + name) 
            else: 
                if debug == True:
                    print ("Missing rules for this extensions: " + extension)
            

def run():
    while True:
        time.sleep(3)
        move(sys.argv[1])

if __name__ == "__main__":
    run()