"""This module is where the app will run"""
import features
import cmd

def main():
    pass

if __name__:="__main__":
    base_instance = features.Base()
    base_instance.do_load_data()
    base_instance.cmdloop()
    
    
    