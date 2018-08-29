# Runs all the other scripts, in order

print("RUNNING SCRIPTS...")
execfile("01_configure.py")
execfile("02_download.py")
execfile("03_extract.py")
execfile("04_load.py")
# execfile("05_explore.py")
execfile("06_merge.py")
execfile("07_shuffle.py")
execfile("08_save.py")
# execfile("09_check_dups.py")
execfile("10_classify.py")
