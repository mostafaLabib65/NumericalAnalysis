from qtpy import QtCore


class RunCommands(QtCore.QThread):
    def __init__(self, parent, command, *args, **kwargs):
        QtCore.QThread.__init__(self, parent)
        self.command = command
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.command(*self.args)
