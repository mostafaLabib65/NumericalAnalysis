# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/mario_hunter/testPyQT/form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QDockWidget, QVBoxLayout, QPushButton, QLabel, QAction
from qtpy import QtGui, QtCore
from controllers.rootsMethodFactory import RootsMethodFactory
from controllers.gaussGordanFactory import GaussGordan
from models.fixedpointplot import FixedPointPlot
from views.InputException import InputException
from views.InputValidation import InputValidation
from views.Observer import Observer
from controllers.interpolation import InterPolationFactory
from views.FileParameters import FileParameters as fp

ys = [1, .81, .43, .25, .04, 0, .04, .25, .43, .81, 1]
xs = [-1, -.9, -.656, -.5, -.2, 0, .2, .5, .656, .9, 1]
gx = [0.81, .656, .43, .1853, 0.03433, 0]
x = [.9, 0.81, .656, .43, .1853, 0.03433]
error_style = "QStatusBar{padding-left:8px;background:rgba(255,0,0,255);color:white;font-weight:bold;}"
info_style = "QStatusBar{padding-left:8px;background:rgba(192,192,192,0.3);color:white;font-weight:bold;}"
sucess = "QStatusBar{padding-left:8px;background:rgba(0,255,0,255);color:white;font-weight:bold;}"


class MainWindow(QMainWindow, Observer):
    stepSolveFlag = 0
    chosenFileFlag = 0
    gaussGordanFlag = 0
    interpolationFlag = 0
    result = []
    index = -1

    def __init__(self, app):
        QMainWindow.__init__(self)
        self.app = app
        self.parameters = fp(method=None, equation=None, start=None, End=None, tolerance=None, maxItr=None,
                             observer=self)

    def setupUi(self):
        uic.loadUi("mainwindow.ui", self)
        self.figure = FixedPointPlot(xs, ys, gx, x, parent=None, app=self.app)
        # self.plotLayout.addWidget(self.fig,0,0)
        # self.plotLayout.insertWidget(0, self.fig)
        self.animatebtn.clicked.connect(self.animate_btn_clicked)
        self.solveBtn.clicked.connect(self.solve_btn_clicked)
        self.methodsCombo.currentTextChanged.connect(self.on_methodsCombo_changed)
        self.modes.currentTextChanged.connect(self.on_modesCombo_changed)
        self.step.clicked.connect(self.step_btn_clicked)
        self.gaussSolve.clicked.connect(self.gauss_Btn_Clicked)
        self.GaussWidget.setHidden(not self.GaussWidget.isHidden())
        self.interpolationWidget.setHidden(not self.interpolationWidget.isHidden())
        self.next.clicked.connect(self.update_step_ui)
        self.chooseFile.clicked.connect(self.readFromFile)
        self.gaussChooseFile.clicked.connect(self.readFromFile)
        self.interSolve.clicked.connect(self.interpolation_Btn_Clicked)
        self.interChooseFile.clicked.connect(self.readFromFile)
        self.statusBar().show()
        self.populate_menu_bar()
        self.show()

    def populate_menu_bar(self):
        openFileAction = QAction("Open a file", self)
        openFileAction.setShortcut("Ctrl+O")
        openFileAction.setStatusTip('open a file to be loaded')
        openFileAction.triggered.connect(self.readFromFile)

        fileMenu = self.menuBar().addMenu("File")
        fileMenu.addAction(openFileAction)
        self.menuBar().show()

    def animate_btn_clicked(self):
        self.figure.animate()

    def check_error(self):
        InputValidation.validate(self.equationInput.text(), self.methodsCombo.currentText(), self.start_2.text(),
                                 self.end_2.text())

    def prepare_parameters(self):
        if self.chosenFileFlag == 0:
            # method, observer, eq_str, start_str, end_str, tolerance, maxItr, *args, **kwargs
            return {
                "method": self.methodsCombo.currentText(),
                "observer": self,
                "eq_str": self.equationInput.text(),
                "start_str": self.end_2.text(),
                "end_str": self.start_2.text(),
                "tolerance": self.tolerance.text(),
                "maxItr": self.maxIter.text(),
                "parent": self.dockWidget,
                "app": self.app
            }
        else:
            return self.parameters.paramters()

    def solve_btn_clicked(self):
        parameters = self.prepare_parameters()

        self.next.setDisabled(True)
        self.stepSolveFlag = 0

        try:
            self.check_error()
        except InputException as ex:
            self.statusBar().setStyleSheet(error_style)
            self.statusBar().clearMessage()
            self.statusBar().showMessage(ex.__str__())
            self.app.processEvents()
            return

        try:
            method = RootsMethodFactory.acquire_method(**parameters)
            method.execute()
        except Exception as ex:
            self.statusBar().setStyleSheet(error_style)
            self.statusBar().clearMessage()
            self.statusBar().showMessage(ex.__str__())
            self.app.processEvents()

    def step_btn_clicked(self):
        parameters = self.prepare_parameters()
        self.index = -1
        self.next.setDisabled(False)
        self.stepSolveFlag = 1

        try:
            self.check_error()
        except InputException as ex:
            self.statusBar().setStyleSheet(error_style)
            self.statusBar().clearMessage()
            self.statusBar().showMessage(ex.__str__())
            self.app.processEvents()
            return
        try:
            method = RootsMethodFactory.acquire_method(**parameters)
            self.next.setEnabled(True)
            method.execute()
        except Exception as ex:
            self.statusBar().setStyleSheet(error_style)
            self.statusBar().clearMessage()
            self.statusBar().showMessage(ex.__str__())
            self.app.processEvents()

    def notify(self, result):
        if self.stepSolveFlag == 0:
            self.update_ui(result)
        else:
            self.result = result
            self.update_step_plot(result)
            self.update_step_ui()

    def notifyFileParameters(self, parameters):
        if self.gaussGordanFlag == 0 and self.interpolationFlag == 0:
            self.parameters = parameters
            self.messageLabel.setText("File loaded")
            self.equationInput.setText(parameters.equation)
            index = self.methodsCombo.findText(parameters.method, QtCore.Qt.MatchFixedString)
            if index >= 0:
                self.methodsCombo.setCurrentIndex(index)
            self.end_2.setText(parameters.start)
            self.start_2.setText(parameters.End)
            self.tolerance.setText(parameters.tolerance)
            self.maxIter.setText(parameters.maxItr)
        elif self.gaussGordanFlag == 1:
            self.parameters = parameters
            self.gaussInput.append(parameters.equation)
        elif self.interpolationFlag == 1:
            self.parameters = parameters
            index = self.comboBox.findText(parameters.method, QtCore.Qt.MatchFixedString)
            if index >= 0:
                self.comboBox.setCurrentIndex(index)
            self.pointsEditor.setText(parameters.equation)
            self.xInput.setText(parameters.start)
            self.yInput.setText(parameters.End)
            self.pointsText.setText(parameters.tolerance)
        self.update()

    def update_ui(self, result):
        self.statusBar().setStyleSheet(sucess)
        self.statusBar().clearMessage()
        self.statusBar().showMessage(result.status)
        if self.gaussGordanFlag == 0 and self.interpolationFlag == 0:
            if result.iterations != None:
                self.solutionBrowser.setText(str(result.solution) + "\n" + str(result.iterations))
            else:
                self.solutionBrowser.setText(str(result.solution))
            self.plotLayout.removeWidget(self.figure)
            self.figure = result.figure
            self.plotLayout.insertWidget(0, self.figure)
        elif self.gaussGordanFlag == 1:
            self.gaussSolution.setText(str(result.solution))
        elif self.interpolationFlag == 1:
            self.outPut.setText(str(result.solution))
        if self.methodsCombo.currentText() != "Bierge Vieta":
            self.animatebtn.setEnabled(True)
        self.messageLabel.setText(result.message)
        self.update()

    def update_step_ui(self):
        if self.index == -1:
            self.messageLabel.setText(self.result.message)
            self.statusBar().setStyleSheet(sucess)
            self.statusBar().clearMessage()
            self.statusBar().showMessage(self.result.status)
            self.solutionBrowser.append("iterations = " + str(self.result.iterations))
            self.messageLabel.setText(self.result.message)
            self.index += 1
        elif self.index == 0:
            self.solutionBrowser.setText(str(self.result.data[0]))
            self.index += 1
        else:
            if self.index != len(self.result.data):
                self.solutionBrowser.append("\n" + str(self.result.data[self.index]))
                self.index += 1

    def update_step_plot(self, result):
        self.plotLayout.removeWidget(self.figure)
        self.figure = result.figure
        self.plotLayout.insertWidget(0, self.figure)
        self.animatebtn.setEnabled(True)
        self.update()

    def on_methodsCombo_changed(self):
        if self.methodsCombo.currentText() == "Bisection" or self.methodsCombo.currentText() == "False-Position":
            self.interval.setText("interval")
            self.start_2.setEnabled(True)
            self.start_2.show()
            self.From_2.setText("From")
            self.To_2.setText("To")
            self.To_2.show()
            self.itr.setText("Max iterations")

        elif (
                self.methodsCombo.currentText() == "Newton" or self.methodsCombo.currentText() == "Fixed Point" or self.methodsCombo.currentText() == "Bierge Vieta"):
            self.interval.setText("Point")
            self.From_2.setText("X")
            self.start_2.hide()
            self.To_2.hide()
            self.itr.setText("Max iterations")
            self.start_2.setDisabled(True)

        elif self.methodsCombo.currentText() == "Secant":
            self.interval.setText("Points")
            self.start_2.setEnabled(True)
            self.start_2.show()
            self.From_2.setText("X1")
            self.To_2.setText("X2")
            self.itr.setText("Max iterations")
            self.To_2.show()
        elif (self.methodsCombo.currentText() == "General algorithm"):
            self.interval.setText("interval")
            self.start_2.setEnabled(True)
            self.start_2.show()
            self.From_2.setText("From")
            self.To_2.setText("To")
            self.itr.setText("Number of roots")
            self.To_2.show()

    def on_modesCombo_changed(self):
        if (self.modes.currentText() == "Roots"):
            self.gaussGordanFlag = 0
            self.interpolationFlag = 0
            self.dockWidgetContents.setVisible(True)
            self.GaussWidget.setHidden(True)
            self.interpolationWidget.setHidden(True)
            self.RootsWidget.setVisible(True)
        elif (self.modes.currentText() == "Gauss jourdan"):
            self.gaussGordanFlag = 1
            self.interpolationFlag = 0
            self.dockWidgetContents.setHidden(True)
            self.RootsWidget.setHidden(True)
            self.interpolationWidget.setHidden(True)
            self.GaussWidget.setVisible(True)
        elif (self.modes.currentText() == "Interpolation"):
            self.gaussGordanFlag = 0
            self.interpolationFlag = 1
            self.dockWidgetContents.setHidden(True)
            self.GaussWidget.setHidden(True)
            self.RootsWidget.setHidden(True)
            self.interpolationWidget.setVisible(True)

    def gauss_Btn_Clicked(self):
        if self.chosenFileFlag == 0:
            method = GaussGordan.acquire_method(self, self.gaussInput.toPlainText())
            method.execute()
        else:
            self.chosenFileFlag == 0
            method = GaussGordan.acquire_method(self, self.parameters.equation)
            method.execute()

    def interpolation_Btn_Clicked(self):
        if self.chosenFileFlag == 0:
            method = InterPolationFactory.acquire_method(self.comboBox.currentText(), self,
                                                         self.pointsEditor.text(),
                                                         self.xInput.text(), self.yInput.text(), self.pointsText.text())
            method.execute()
        else:
            self.chosenFileFlag == 0
            method = GaussGordan.acquire_method(self.parameters.method, self, self.parameters.equation,
                                                self.parameters.start,
                                                self.parameters.End, self.parameters.tolerance)
            method.execute()

    def readFromFile(self):
        global chosenFileFlag
        chosenFileFlag = 1
        filename = QtWidgets.QFileDialog.getOpenFileName(parent=self, caption='Open file')
        if self.gaussGordanFlag != 1 and self.interpolationFlag != 1:
            reading = RootsMethodFactory.readFromFile(filename[0], self, widget=self.dockWidget, app=self.app)
        elif self.gaussGordanFlag == 1:
            reading = GaussGordan.readFromFile(filename[0], self, widget=self.dockWidget, app=self.app)
        elif self.interpolationFlag == 1:
            reading = InterPolationFactory.readFromFile(filename[0], self, widget=self.dockWidget, app=self.app)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Base, QtGui.QColor(15, 15, 15))
    palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)

    palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(142, 45, 197).lighter())
    palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
    app.setPalette(palette)
    window = MainWindow(app)
    window.setupUi()
    sys.exit(app.exec_())

    ''' def showRoots(self):
            self.chooseFile.show()
            self.methodsCombo.show()
            self.label_2.show()
            self.label.show()
            self.equationInput.show()
            self.interval.show()
            self.From.show()
            self.end.show()
            self.To.show()
            self.start.show()
            self.tol.show()
            self.tolerance.show()
            self.itr.show()
            self.maxIter.show()
            self.solveBtn.show()
            self.step.show()
            self.solutionBrowser.show()
            self.next.show()
        def hideRoots(self):
            self.chooseFile.hide()
            self.methodsCombo.hide()
            self.label_2.hide()
            self.label.hide()
            self.equationInput.hide()
            self.interval.hide()
            self.From.hide()
            self.end.hide()
            self.To.hide()
            self.start.hide()
            self.tol.hide()
            self.tolerance.hide()
            self.itr.hide()
            self.maxIter.hide()
            self.solveBtn.hide()
            self.step.hide()
            self.solutionBrowser.hide()
            self.next.hide()
            '''
