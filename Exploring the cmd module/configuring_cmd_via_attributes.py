"""In this module i illustrate some method overwriting"""
import cmd


class HelloWorld(cmd.Cmd):
    """Simple command processor example.
    This example class shows a command processor to let the user
    control the prompt for the interactive session.
    """

    prompt = ">>>> "
    intro = "Simple command processor example."
    doc_header = "doc_header"
    misc_header = "misc_header"
    undoc_header = "undoc_header"
    ruler = "-"

    def do_prompt(self, line):
        "Change the interactive prompt"
        self.prompt = line + ": "

    def do_EOF(self):
        """End application"""
        return True


if __name__ == "__main__":
    HelloWorld().cmdloop()
    