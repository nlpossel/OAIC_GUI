from researchGUI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QFileDialog, QInputDialog, QAbstractItemView, QTableWidget, QTableWidgetItem
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys
from random import randint

##########NOTES############
# graph stuff too


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.addActor("temp 1")
    ui.addActor("temp 2")
    logs = "test and test and test and test and test and test"

    # Use this to get the list of actors and test script files used in
    # each test task.
    ui.tableWidget.itemClicked.connect(lambda: ui.getActors())
    ui.tableWidget.itemClicked.connect(lambda: ui.printout())
    ui.stopButton.clicked.connect(lambda: ui.updateStatus("Running"))
    ui.stopButton.clicked.connect(lambda: ui.addLogs(logs))

    ui.graphX = list(range(100))
    ui.graphY = [randint(0,100) for _ in range(100)]
    ui.addGraphData(ui.graphX, ui.graphY)

    timer = QtCore.QTimer()
    timer.setInterval(100)
    timer.timeout.connect(lambda: updatePlotData(ui))
    timer.start()
    
    sys.exit(app.exec_())

def updatePlotData(ui):
    index = ui.dropDown1.currentIndex()
    xData = ui.dropDown1.itemData(index, ui.graphRoleX)
    yData = ui.dropDown1.itemData(index, ui.graphRoleY)
    if xData is None:
        ui.graphX = list(range(100))
        ui.graphY = [randint(0,100) for _ in range(100)]
        ui.addGraphData(ui.graphX, ui.graphY)

    xData = xData[1:]
    xData.append(xData[-1] + 1)
    ui.dropDown1.setItemData(index, xData, ui.graphRoleX)

    yData = yData[1:]
    yData.append(randint(0,100))
    ui.dropDown1.setItemData(index, yData, ui.graphRoleY)

    ui.showGraph()


    

if __name__ == '__main__':
    main()