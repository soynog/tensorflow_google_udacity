# Runs all the other scripts, in order

print("RUNNING SCRIPTS...")
execfile("01_configure.py")
execfile("02_download.py")
execfile("03_extract.py")
execfile("04_load.py")
execfile("05_explore.py")
