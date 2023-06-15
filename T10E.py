import sys

# Accessing Command Line Arguments

arguments = sys.argv
print("Command line arguments:", arguments)

# Modifying Module Search Path

sys.path.append("/path/to/custom/module")
import custom_module

# Retrieving System-Specific Information

print("Python version:", sys.version)
print("Operating system:", sys.platform)
print("Platform:", sys.platform)