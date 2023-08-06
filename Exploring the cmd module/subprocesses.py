"""In this modue i go over the accesing shell commands through cmd module:
Subprocesses
"""

import cmd
import subprocess


class ShellEnabled(cmd.Cmd):
    """Subprocesses"""
    last_output = ""

    def do_shell(self, line):
        """Run a shell command"""

        print("running shell command:", line)

        sub_cmd = subprocess.Popen(line, shell=True, stdout=subprocess.PIPE)
        output = sub_cmd.communicate()[0]
        print(output)
        self.last_output = output

    def do_echo(self, line):
        """Print the input, replacing "$out" with
        the output of the last shell command.
        """
        # Obviously not robust
        print(line.replace("$out", self.last_output))

    def do_EOF(self):
        """End application"""
        return True
if __name__ == '__main__':
    ShellEnabled().cmdloop()
    