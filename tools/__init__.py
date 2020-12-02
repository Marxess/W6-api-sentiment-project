#whenever modules are added, this will get executed because getdata is at another level vs. configuration
#we will avoid errors with this process
import sys, os

module_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(module_path)
