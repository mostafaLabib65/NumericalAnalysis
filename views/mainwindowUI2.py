# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/mario_hunter/testPyQT/form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QDockWidget, QVBoxLayout, QPushButton
from qtpy import QtGui, QtCore

from controllers.rootsMethodFactory import RootsMethodFactory
from controllers.gaussGordanFactory import GaussGordan
from models.fixedpointplot import FixedPointPlot
from views.Observer import Observer
from controllers.interpolation import InterPolationFactory
from views.FileParameters import FileParameters as fp
ys = [1, .81, .43, .25, .04, 0, .04, .25, .43, .81, 1]
xs = [-1, -.9, -.656, -.5, -.2, 0, .2, .5, .656, .9, 1]
gx = [0.81, .656, .43, .1853, 0.03433, 0]
x = [.9, 0.81, .656, .43, .1853, 0.03433]

class MainWindow(QMainWindow, Observer):
    stepSolveFlag = 0
    choosedFileFlag = 0
    gaussGordanFlag = 0
    interpolationFlag = 0
    parameters = fp(method="", equation="",start="", End= "",tolerance="", maxItr="")
    result = []
    index = -1
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
        self.show()

    def animate_btn_clicked(self):
        self.fig.animate()


    def checkError(self):
        if(self.equationInput.text() == ""):
            return 1
        elif((self.methodsCombo.currentText() == "Bisection" or self.methodsCombo.currentText() == "False-Position" or self.methodsCombo.currentText() == "Secant")
        and (self.start_2.text() == "" or self.end_2.text() == "")):
            return 2
        elif((self.methodsCombo.currentText() == "Newton" or self.methodsCombo.currentText() == "Fixed Point" or self.methodsCombo.currentText() == "Bierge Vieta") and
         self.end_2.text() == ""):
            return 3
        else:
            return 4



    def solve_btn_clicked(self):
        if(self.choosedFileFlag == 0):
            self.next.setDisabled(True)
            global stepSolveFlag
            stepSolveFlag = 0
            status = self.checkError()
            if(status == 1):
                self.messageLabel.setText("Enter the equation first asshole")
            elif(status == 2):
                self.messageLabel.setText("Required input is missed asshole")
            elif(status == 3):
                self.messageLabel.setText("Required input is missed asshole")
            elif(status == 4):
                method = RootsMethodFactory.acquire_method(self.methodsCombo.currentText(), self, self.equationInput.text(),
                                                           self.end_2.text(), self.start_2.text(), self.tolerance.text(), self.maxIter.text(), parent=self.dockWidget, app=self.app)
                method.execute()
        else:
            self.choosedFileFlag == 0
            self.next.setDisabled(True)
            stepSolveFlag = 0
            method = RootsMethodFactory.acquire_method(self.parameters.method, self, self.parameters.equation,
                                                       self.parameters.start, self.parameters.End, self.parameters.tolerance, self.parameters.maxItr, parent=self.dockWidget,
                                                       app=self.app)
            method.execute()

    def step_btn_clicked(self):
        self.index = -1
        if(self.choosedFileFlag == 0):
            status = self.checkError()
            global stepSolveFlag
            stepSolveFlag = 1
            if (status == 1):
                self.messageLabel.setText("Enter the equation first asshole")
            elif (status == 2):
                self.messageLabel.setText("Required input is missed asshole")
            elif (status == 3):
                self.messageLabel.setText("Required input is missed asshole")
            elif (status == 4):
                method = RootsMethodFactory.acquire_method(self.methodsCombo.currentText(), self, self.equationInput.text(),
                                                           self.end_2.text(), self.start_2.text(), self.tolerance.text(),
                                                           self.maxIter.text(), parent=self.dockWidget, app=self.app)
                self.next.setEnabled(True)
                method.execute()
        else:
            self.choosedFileFlag = 0
            stepSolveFlag = 1
            method = RootsMethodFactory.acquire_method(self.parameters.method, self, self.parameters.equation,
                                                       self.parameters.start, self.parameters.End, self.parameters.tolerance,
                                                       self.parameters.maxItr, parent=self.dockWidget,
                                                       app=self.app)
            self.next.setEnabled(True)
            method.execute()

    def notify(self, result):
        if(self.stepSolveFlag == 0):
            self.update_ui(result)
        else:
            self.result = result
            self.update_step_plot(result)
            self.update_step_ui()

    def notifyFileParameters(self,parameters):
        if(self.gaussGordanFlag == 0 and self.interpolationFlag == 0):
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
        elif(self.gaussGordanFlag == 1):
            self.parameters = parameters
            self.gaussInput.append(parameters.equation)
        elif(self.interpolationFlag == 1):
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
        self.setStatusTip(result.status)
        if(self.gaussGordanFlag == 0 and self.interpolationFlag == 0):
            self.solutionBrowser.setText(str(result.solution) + "\n" + str(result.iterations))
            self.plotLayout.removeWidget(self.fig)
            self.fig = result.figure
            self.plotLayout.insertWidget(0, self.fig)
        elif(self.gaussGordanFlag == 1):
            self.gaussSolution.setText(str(result.solution))
        elif(self.interpolationFlag == 1):
            self.outPut.setText(str(result.solution))
        if(self.methodsCombo.currentText() != "Bierge Vieta"):
            self.animatebtn.setEnabled(True)
        self.messageLabel.setText(result.message)
        self.update()

    def update_step_ui(self):
        if(self.index == -1):
            self.messageLabel.setText(self.result.message)
            self.setStatusTip(self.result.status)
            self.solutionBrowser.append("iterations = " + str(self.result.iterations))
            self.messageLabel.setText(self.result.message)
            self.index += 1
        elif(self.index == 0):
            self.solutionBrowser.setText(str(self.result.data[0]))
            self.index += 1
        else:
            if (self.index != len(self.result.data)):
                self.solutionBrowser.append("\n" + str(self.result.data[self.index]))
                self.index += 1


    def update_step_plot(self, result):
        self.plotLayout.removeWidget(self.fig)
        self.fig = result.figure
        self.plotLayout.insertWidget(0, self.fig)
        self.animatebtn.setEnabled(True)
        self.update()

    def on_methodsCombo_changed(self):
        if (self.methodsCombo.currentText() == "Bisection" or self.methodsCombo.currentText() == "False-Position"):
            self.interval.setText("interval")
            self.start_2.setEnabled(True)
            self.start_2.show()
            self.From_2.setText("From")
            self.To_2.setText("To")
            self.To_2.show()
            self.itr.setText("Max iterations")

        elif (self.methodsCombo.currentText() == "Newton" or self.methodsCombo.currentText() == "Fixed Point" or self.methodsCombo.currentText() == "Bierge Vieta"):
            self.interval.setText("Point")
            self.From_2.setText("X")
            self.start_2.hide()
            self.To_2.hide()
            self.itr.setText("Max iterations")
            self.start_2.setDisabled(True)

        elif (self.methodsCombo.currentText() == "Secant"):
            self.interval.setText("Points")
            self.start_2.setEnabled(True)
            self.start_2.show()
            self.From_2.setText("X1")
            self.To_2.setText("X2")
            self.itr.setText("Max iterations")
            self.To_2.show()
        elif(self.methodsCombo.currentText() == "General algorithm"):
            self.interval.setText("interval")
            self.start_2.setEnabled(True)
            self.start_2.show()
            self.From_2.setText("From")
            self.To_2.setText("To")
            self.itr.setText("Number of roots")
            self.To_2.show()

    def on_modesCombo_changed(self):
        if(self.modes.currentText() == "Roots"):
            self.gaussGordanFlag = 0
            self.interpolationFlag = 0
            self.dockWidgetContents.setVisible(True)
            self.GaussWidget.setHidden(True)
            self.interpolationWidget.setHidden(True)
            self.RootsWidget.setVisible(True)
        elif(self.modes.currentText() == "Gauss jourdan"):
            self.gaussGordanFlag = 1
            self.interpolationFlag = 0
            self.dockWidgetContents.setHidden(True)
            self.RootsWidget.setHidden(True)
            self.interpolationWidget.setHidden(True)
            self.GaussWidget.setVisible(True)
        elif(self.modes.currentText() == "Interpolation"):
            self.gaussGordanFlag = 0
            self.interpolationFlag = 1
            self.dockWidgetContents.setHidden(True)
            self.GaussWidget.setHidden(True)
            self.RootsWidget.setHidden(True)
            self.interpolationWidget.setVisible(True)

    def gauss_Btn_Clicked(self):
        if (self.choosedFileFlag == 0):
            method = GaussGordan.acquire_method(self,self.gaussInput.toPlainText())
            method.execute()
        else:
            self.choosedFileFlag == 0
            method = GaussGordan.acquire_method(self, self.parameters.equation)
            method.execute()
    def interpolation_Btn_Clicked(self):
        if (self.choosedFileFlag == 0):
            method = InterPolationFactory.acquire_method(self.methodsCombo.currentText(),self,self.pointsEditor.text(),
                                                         self.xInput.text(),self.yInput.text(), self.pointsText.text())
            method.execute()
        else:
            self.choosedFileFlag == 0
            method = GaussGordan.acquire_method(self.parameters.method, self,self.parameters.equation,self.parameters.start,
                                                self.parameters.End,self.parameters.tolerance)
            method.execute()

    def readFromFile(self):
        global choosedFileFlag
        choosedFileFlag = 1
        filename = QtWidgets.QFileDialog.getOpenFileName(parent=self, caption='Open file')
        if(self.gaussGordanFlag != 1 and self.interpolationFlag != 1):
            reading = RootsMethodFactory.readFromFile(filename[0], self)
        elif(self.gaussGordanFlag == 1):
            reading = GaussGordan.readFromFile(filename[0], self)
        elif(self.interpolationFlag == 1):
            reading = InterPolationFactory.readFromFile(filename[0], self)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
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
