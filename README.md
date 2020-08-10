## dl_clean.py || Download Cleaner

A script that listens to changes to a directory then sorts incoming files as they arrive.

Current usage is to remove the need to manually pick locations for my browser downloads, a task I largely despise.

Triggers a notification which can be turned off with the flag **-q**

Example:

> python dl_clean.py "path/to/listen/\*" -q

Changelog:
v0.1 - Just moves image files & pdfs
v0.0.2 - Moves files according to rules set in dl_clean.conf. Also has a debug & quiet mode.
v0.0.3 -

Todo:

1. Improve CLI usability with argparse & man page
2. ~~Daemonise properly rather than setting to timeout~~
3. Search function for looking for .conf, currently has to be in run directory
4. Log output flag, i.e. --verbose
5. More flexible config for locations. Currently home dir is assumed as output location
