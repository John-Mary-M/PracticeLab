'''cs50p 9/9/2023 Using thrid party Packages
cowsay pakage installed.'''
import sys
import cowsay

if len(sys.argv) == 2:
    cowsay.trex("Hello, " + sys.argv[1])