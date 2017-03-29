# coding: utf-8

class SlickButton(object):

    def __init__(self, command):
        self.command = command

    def on_button_pushed(self):
        self.command.execute()


class BeepCommand(object):

    def execute():
        print('Beep!')


class SendMailCommand(object):

    def execute():
        print('Send mail!')


if __name__ == '__main__':
    cmd = BeepCommand()
    btn = SlickButton(cmd)

    cmd2 = SendMailCommand()
    btn2 = SlickButton(cmd2)
