"""This module goes over some common cmd methods that can be overridden though not all of them"""

import cmd
from typing import Any


class Illustrate(cmd.Cmd):
    """Illustrate the base class method use"""

    def cmdloop(self, intro: Any | None = None):
        print("cmdloop ", intro)
        return super().cmdloop(intro)

    def preloop(self):
        print("preloop()")
        return super().preloop()

    def postloop(self):
        print("postloop()")

    def parseline(self, line):
        print("parseline =>", line)
        ret = cmd.Cmd.parseline(self, line)
        print(ret)
        return ret

    def onecmd(self, s):
        print("onecmd", s)
        return cmd.Cmd.onecmd(self, s)

    def emptyline(self):
        print("Emptyline()")
        return cmd.Cmd.emptyline(self)

    def default(self, line):
        print("default", line)
        return cmd.Cmd.default(self, line)

    def precmd(self, line):
        print("precmd ", line)
        return cmd.Cmd.precmd(self, line)

    def postcmd(self, stop, line):
        print("postcmd ", stop, line)
        return cmd.Cmd.postcmd(self, stop, line)

    def do_greet(self, line):
        """Command to greet [person]
        """
        print("hello,", line)

    def do_EOF(self):
        """End application"""
        return True


if __name__ == "__main__":
    Illustrate().cmdloop("Illustrating the methods of cmd.Cmd")
