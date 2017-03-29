# coding: utf-8

import os


class Command(object):

    def __init__(self, _description):
        self._description = _description

    def description(self):
        return self._description

    def execute(self):
        pass

    def unexecute(self):
        pass


class CreateCommand(Command):

    def __init__(self, path, contents):
        Command.__init__(self, 'Create file: {}'.format(path))
        self.path = path
        self.contents = contents

    def execute(self):
        with open(self.path, 'w') as f:
            f.write(self.contents)

    def unexecute(self):
        os.remove(self.path)


class DeleteCommand(Command):

    def __init__(self, path):
        Command.__init__(self, 'Delete file: {}'.format(path))
        self.path = path
        self.contents = None

    def execute(self):
        try:
            with open(self.path, "r") as f:
                self.contents = f.read()

        except IOError:
            pass
        os.remove(self.path)


    def unexecute(self):
        if self.contents is not None:
            with open(self.path, 'w') as f:
                f.write(self.contents)


class CompositeCommand(Command):

    def __init__(self):
        Command.__init__(self, None)
        self.commands = []

    def description(self):
        return '\n'.join(cmd.description() for cmd in self.commands)

    def append_command(self, cmd):
        self.commands.append(cmd)

    def execute(self):
        for cmd in self.commands:
            cmd.execute()

    def unexecute(self):
        for cmd in reversed(self.commands):
            cmd.unexecute()
