"""This module implements a simple Console application using the cmd module"""
import cmd

class HelloWorld(cmd.Cmd):
        """Simple command processor"""
        
        # define the first command
        def do_greet(self, person):
                """greet [person]
                Greet the named person"""
                if person:
                        print ("Hello", person)
                else:
                        print ("hi")
                
        # format live help
        def help_greet(self):
                print("\n".join([
                        'greet [person]',
                        'Greet the named person',
                ]))
                
        # build in auto completion
        def complete_greet(self, text, line, begidx, endix):
                # list of options for auto-complete
                options = ['Alice', 'Bob', 'Charlie']
                # return all options if no text in entered
                if not text:
                        completions = options
                # otherwise, return options that start with the entered text
                else:
                        completions = [c for c in options if c.startswith(text)]
                return completions
        # define method to exit the app
        def do_EOF(self, line):
                return True
        
        # override the default complete method to enable auto-completion
        def complete(self, text, state):
                # split the line to get the command being entered
                line = self.line_buffer
                stripped_line = line.strip()
                command = stripped_line.split(' ')[0] if stripped_line else ''
                
                # call the appropriate complete_* method based on the command
                if command == 'greet':
                        return self.complete_greet(text, line, 0, len(line))
                # fallback to the default behavior
                return super().complete(text, state)

       		
# run application only if called by name
if __name__ == "__main__":
        HelloWorld().cmdloop()