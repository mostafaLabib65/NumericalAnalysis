# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/mario_hunter/testPyQT/form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QDockWidget, QVBoxLayout, QPushButton

from controllers.methodFactory import MethodFactory
from models.fixedpointplot import FixedPointPlot
from views.Observer import Observer

ys = [1, .81, .43, .25, .04, 0, .04, .25, .43, .81, 1]
xs = [-1, -.9, -.656, -.5, -.2, 0, .2, .5, .656, .9, 1]
gx = [0.81, .656, .43, .1853, 0.03433, 0]
x = [.9, 0.81, .656, .43, .1853, 0.03433]


class MainWindow(QMainWindow, Observer):
    def __init__(self, app):
        QMainWindow.__init__(self)
        self.app = app

    def setupUi(self):
        uic.loadUi("mainwindow.ui", self)
        self.fig = FixedPointPlot(xs, ys, gx, x, parent=None, app=self.app)
        # self.plotLayout.addWidget(self.fig,0,0)
        # self.plotLayout.insertWidget(0, self.fig)
        self.animatebtn.clicked.connect(self.animate_btn_clicked)
        self.solveBtn.clicked.connect(self.solve_btn_clicked)
        self.show()

    def animate_btn_clicked(self):
        self.fig.animate()

    def solve_btn_clicked(self):
        method = MethodFactory.acquire_method(self.methodsCombo.currentText(), self, self.equationInput.text(),
                                              parent=self.dockWidget, app=self.app)
        method.execute()

    def notify(self, result):
        self.update_ui(result)

    def update_ui(self, result):
        self.setStatusTip(result.status)
        self.solutionBrowser.setText(result.solution)
        self.messageLabel.setText(result.message)
        self.plotLayout.removeWidget(self.fig)
        self.fig = result.figure
        self.plotLayout.insertWidget(0, self.fig)
        self.animatebtn.setEnabled(True)

        self.update()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(app)
    window.setupUi()
    sys.exit(app.exec_())
