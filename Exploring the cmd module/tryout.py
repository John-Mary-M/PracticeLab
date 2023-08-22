#!/usr/bin/env python3
"""This module is a definition of a Library app"""

import cmd

class Libapp(cmd.Cmd):
    """Creates command to use to enter, display and delete books"""
    prompt = ">>>"
    bookList = []
    
    def do_addBook(self, book):
        """Adds books to list"""
        book_title = input("Enter Book Title: ")
        book_auth = input("Enter Author: ")
        Libapp.bookList.append(book_title + ", " + book_auth)
        
    
    
    def do_displayBook(self, arg):
        """Displays books in list"""
        print("loading books . . . !")
        number = 1
        for book in Libapp.bookList:
            print(number, book)
            number += 1
            # print()
        
    def do_EOF(self, arg):
        print()
        return True
        
if __name__=='__main__':
    Libapp().cmdloop()
        
    