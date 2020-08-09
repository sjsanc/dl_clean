## dl_clean.py || Download Cleaner

A script that listens to changes to a directory then sorts incoming files as they arrive.

Current usage is to remove the need to manually pick locations for my browser downloads, a task I largely despise.

Triggers a notification which can be turned off with the flag **-q**

Example:

> python dl_clean.py "path/to/listen/\*"

Changelog:
v0.1 - Just moves image files & pdfs

Todo:
Make it installable? Idk this is a shitty WIP todo
Properly daemonize because timeout loops are bad for some reason
