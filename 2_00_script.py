# Master Script for Assignment 2

print("RUNNING SCRIPTS FOR ASSIGNMENT 2...")
execfile("2_01_configure.py")
execfile("2_02_load.py")
execfile("2_03_reformat.py")
# execfile("2_04_build_graph_gd.py") # normal gradient descent
execfile("2_04_build_graph_nnrelu.py") # stochastic gradient descent
# execfile("2_05_compute_gd.py")
execfile("2_05_compute_sgd.py")
