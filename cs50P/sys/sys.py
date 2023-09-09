'''cs50p 9/06/2023 commandline arguements with the sys module
    argv - agruement vector (the words typed at the prompt)
    Another reason not to use windows to write python code
    on a windows machine sys module doesnt have access to the
    argv variable vailable in the module
    
    I worte 
    '''
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguements")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguements")

for arg in sys.argv[1:-1]:
    print("Hello, my name is", arg)
