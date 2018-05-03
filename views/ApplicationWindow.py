import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QMenu, QWidget, QVBoxLayout
from qtpy import QtCore

from models.fixedpointplot import FixedPointPlot


class ApplicationWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("application main window")

        self.file_menu = QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.fileQuit,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)

        self.help_menu = QMenu('&Help', self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)

        self.help_menu.addAction('&About', self.about)

        self.main_widget = QWidget(self)

        l = QVBoxLayout(self.main_widget)
        ys = [1, .81, .43, .25, .04, 0, .04, .25, .43, .81, 1]
        xs = [-1, -.9, -.656, -.5, -.2, 0, .2, .5, .656, .9, 1]
        gx = [0.81, .656, .43, .1853, 0.03433, 0]
        x = [.9, 0.81, .656, .43, .1853, 0.03433]
        sc = FixedPointPlot(xs, ys, gx, x, parent=self.main_widget, width=5, height=4, dpi=100)
        l.addWidget(sc)

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        self.statusBar().showMessage("All hail matplotlib!", 2000)

    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()

    def about(self):
        QMessageBox.about(self, "About",
                          """embedding_in_qt5.py example
                          Copyright 2015 BoxControL
                          This program is a simple example of a Qt5 application embedding matplotlib
                          canvases. It is base on example from matplolib documentation, and initially was
                          developed from Florent Rougon and Darren Dale.
                          http://matplotlib.org/examples/user_interfaces/embedding_in_qt4.html
                          It may be used and modified with no restriction; raw copies as well as
                          modified versions may be distributed without limitation."""
                          )


if __name__ == '__main__':
    app = QApplication(sys.argv)

    aw = ApplicationWindow()
    aw.setWindowTitle("PyQt5 Matplot Example")
    aw.show()
    # sys.exit(qApp.exec_())
    app.exec_()
