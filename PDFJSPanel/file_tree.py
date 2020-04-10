import sys
from PyQt5.QtWidgets import *
from PyQt5 import Qt, QtGui, QtCore
from PDFJSPanel.fileopen import ui_PDFFileWindow
from PyQt5 import QtWidgets
import threading
import os


def file_name(path):
    return os.listdir(path)


class Tree(QMainWindow, ui_PDFFileWindow):
    FileDetectedSignal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(Tree, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("File_Tree")
        self.tree = QTreeWidget()
        font = QtGui.QFont()
        font.setFamily('文泉驿等宽微米黑')
        font.setPixelSize(20)
        path = './Resources/PDFJS/web'
        self.tree.setFont(font)
        self.tree.setStyleSheet("QTreeView::item:hover{background-color:rgb(60,150,225)}"
                                "QTreeView::item:selected{background-color:rgb(80,130,255)}"
                                "QTreeView{background-color: rgb(40, 40, 40)}")
        self.tree.setColumnCount(1)
        self.tree.setColumnWidth(0, 50)
        self.tree.setHeaderLabels(["书籍列表"])
        self.tree.setIconSize(Qt.QSize(25, 25))
        self.tree.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tree.doubleClicked.connect(lambda x: self.EmitFilePath(self.tree.itemFromIndex(x)))
        self.actionfileopen.triggered.connect(self.Open_Folder)

        dirs = file_name(path)

        fileInfo = Qt.QFileInfo(path)
        fileIcon = Qt.QFileIconProvider()
        icon = QtGui.QIcon(fileIcon.icon(fileInfo))
        root = FileTreeItem(self.tree)
        root.setText(0, path.split('/')[-1])
        root.setIcon(0, QtGui.QIcon(icon))
        self.CreateTree(dirs, root, path)
        self.setCentralWidget(self.tree)
        QApplication.processEvents()

    def Open_Folder(self):
        path = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")
        if path == '':
            return
        self.tree = QTreeWidget()
        font = QtGui.QFont()
        font.setFamily('文泉驿等宽微米黑')
        font.setPixelSize(20)
        self.tree.setFont(font)
        self.tree.setStyleSheet("QTreeView::item:hover{background-color:rgb(60,150,225)}"
                                "QTreeView::item:selected{background-color:rgb(80,130,255)}"
                                "QTreeView{background-color: rgb(40, 40, 40)}")
        self.tree.setColumnCount(1)
        self.tree.setColumnWidth(0, 50)
        self.tree.setHeaderLabels(["书籍列表"])
        self.tree.setIconSize(Qt.QSize(25, 25))
        self.tree.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tree.doubleClicked.connect(lambda x: self.EmitFilePath(self.tree.itemFromIndex(x)))
        self.actionfileopen.triggered.connect(self.Open_Folder)

        dirs = file_name(path)

        fileInfo = Qt.QFileInfo(path)
        fileIcon = Qt.QFileIconProvider()
        icon = QtGui.QIcon(fileIcon.icon(fileInfo))
        root = FileTreeItem(self.tree)
        root.setText(0, path.split('/')[-1])
        root.setIcon(0, QtGui.QIcon(icon))
        self.CreateTree(dirs, root, path)
        self.setCentralWidget(self.tree)
        QApplication.processEvents()

    def CreateTree(self, dirs, root, path):
        for i in dirs:
            path_new = path + '/' + i
            if os.path.isdir(path_new):
                fileInfo = Qt.QFileInfo(path_new)
                fileIcon = Qt.QFileIconProvider()
                icon = QtGui.QIcon(fileIcon.icon(fileInfo))
                child = FileTreeItem(root)
                child.setText(0, i)
                child.setIcon(0, QtGui.QIcon(icon))
                dirs_new = file_name(path_new)
                self.CreateTree(dirs_new, child, path_new)
            else:
                fileInfo = Qt.QFileInfo(path_new)
                fileIcon = Qt.QFileIconProvider()
                icon = QtGui.QIcon(fileIcon.icon(fileInfo))
                child = FileTreeItem(root)
                child.setText(0, i)
                child.setIcon(0, QtGui.QIcon(icon))
                child.setFilePath(path_new)

    def EmitFilePath(self, item):
        self.FileDetectedSignal.emit(item.FilePath)


class FileTreeItem(QtWidgets.QTreeWidgetItem):
    FilePath = ''

    def __init__(self, parent=None):
        super(FileTreeItem, self).__init__(parent)

    def setFilePath(self, path):
        self.FilePath = path