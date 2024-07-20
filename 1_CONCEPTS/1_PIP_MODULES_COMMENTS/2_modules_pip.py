""" 
# MODULES: A module is a file containing code written by somebody else (usually) which can be imported and used in our programs. 
# PIP:  Pip is the package manager for python. You can use pip to install a module on your system. 
"""
# Ex: To install pyjoke module,Open terminal and type:
# pip install pyjokes

import pyjokes

# Fetching a random joke from the 'pyjokes' module and printing it.
jokes = pyjokes.get_joke()
print (jokes)