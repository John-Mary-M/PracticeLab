In this part of my learning i focus on and experiement with string functions
from the standard library and several string operationss.

assigningstr.c: I test how to initialize an array with a new string or replace
its contents totally, and how to concatenate a new string to it after
initialization.

char_ptr.c: the compiler reserves the memory of 11 bytes (10 for the hero's
name itself + 1 for an empty char) and fills it with the characters
'D', 'u', 'm', 'b', 'l', 'e' , 'd', 'o', 'r' , 'e' and '\0';
the compiler creates a variable named hero of type char *;
the compiler assigns the pointer to a newly reserved string to the hero variable