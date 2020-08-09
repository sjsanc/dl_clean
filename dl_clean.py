import time
import glob
import os
import sys

# set quite mode
quiet = False;
if len(sys.argv) > 2 and sys.argv[2] == "-q":
    quiet = True


def move(path):

    # get contents of download dr
    downloads = glob.glob(path);
    size = len(downloads)
    if size == 0: 
        print("Nothing to move")
    else: 
        for fullpath in downloads:
            name = os.path.basename(fullpath) # filename
            filename, ext = os.path.splitext(fullpath) # extension
            if ext in [".jpg",".png",".svg"]: 
                os.rename(fullpath, os.environ["HOME"] + "/img/" + name)
                if quiet == False:
                    os.system("notify-send " + name)
            elif ext in [".pdf"]:
                os.rename(fullpath, os.environ["HOME"] + "/pdf/" + name)
                if quiet == False: 
                    os.system("notify-send " + name)

def run():
    while True:
        time.sleep(5)
        move(sys.argv[1])

if __name__ == "__main__":
    run()