#!/usr/bin/python3
#5/06/2023
# Learning fstrings.

def main():

    class Comedian:
        def __init__(self, first_name, last_name, age):
            self.first_name = first_name
            self.last_name = last_name
            self.age = age

        def __str__(self):
            return f"{self.first_name} {self.last_name} is {self.age}."

        def __repr__(self):
            return f"{self.first_name} {self.last_name} is {self.age}. Surprise!"

    new_comedian = Comedian("Eric", "Idle", "74")
    f"{new_comedian}"


if __name__ == "__main__":main()
