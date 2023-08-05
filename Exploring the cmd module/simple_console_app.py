import cmd

class HelloWorld(cmd.Cmd):
    """Simple command processor"""
    FRIENDS = ['Alice', 'Adam', 'Barbara', 'Bob']

    # define the first command
    def do_greet(self, person):
        """greet [person]
        Greet the named person"""

        greeting = "Hello"
        if person and person in self.FRIENDS:
            greeting = "Hi, %s!" % person
        elif person:
            print("Hello, " + person)
            return

        print(greeting)

    # format live help
    def help_greet(self):
        print("\n".join([
            'greet [person]',
            'Greet the named person',
        ]))

    # built-in auto completion
    def complete_greet(self, text, line, begidx, endidx):
        if not text:
            completions = self.FRIENDS[:]
        else:
            completions = [f for f in self.FRIENDS if f.startswith(text)]
        return completions

    # define method to exit the application when done
    def do_EOF(self, line):
        return True


# run application only if called by name
if __name__ == "__main__":
    HelloWorld().cmdloop()