# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CryptoPanelUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1228, 718)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.CryptoLayout = QtWidgets.QSplitter(Form)
        self.CryptoLayout.setOrientation(QtCore.Qt.Horizontal)
        self.CryptoLayout.setObjectName("CryptoLayout")
        self.ToolsArea = QtWidgets.QScrollArea(self.CryptoLayout)
        self.ToolsArea.setWidgetResizable(True)
        self.ToolsArea.setObjectName("ToolsArea")
        self.ToolsAreaPanel = QtWidgets.QWidget()
        self.ToolsAreaPanel.setGeometry(QtCore.QRect(0, 0, 252, 698))
        self.ToolsAreaPanel.setObjectName("ToolsAreaPanel")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.ToolsAreaPanel)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.ToolsSearchBox = QtWidgets.QLineEdit(self.ToolsAreaPanel)
        self.ToolsSearchBox.setObjectName("ToolsSearchBox")
        self.verticalLayout_5.addWidget(self.ToolsSearchBox)
        self.ToolsList = QtWidgets.QListWidget(self.ToolsAreaPanel)
        self.ToolsList.setObjectName("ToolsList")
        self.verticalLayout_5.addWidget(self.ToolsList)
        self.ToolsArea.setWidget(self.ToolsAreaPanel)
        self.OperationLayout = QtWidgets.QSplitter(self.CryptoLayout)
        self.OperationLayout.setOrientation(QtCore.Qt.Horizontal)
        self.OperationLayout.setObjectName("OperationLayout")
        self.NodeBoxAndIOLayouts = QtWidgets.QSplitter(self.OperationLayout)
        self.NodeBoxAndIOLayouts.setOrientation(QtCore.Qt.Vertical)
        self.NodeBoxAndIOLayouts.setObjectName("NodeBoxAndIOLayouts")
        self.CryptoToolNodeEditor = QtWidgets.QWidget(self.NodeBoxAndIOLayouts)
        self.CryptoToolNodeEditor.setObjectName("CryptoToolNodeEditor")
        self.IOArea = QtWidgets.QScrollArea(self.NodeBoxAndIOLayouts)
        self.IOArea.setWidgetResizable(True)
        self.IOArea.setObjectName("IOArea")
        self.IOAreaPanel = QtWidgets.QWidget()
        self.IOAreaPanel.setGeometry(QtCore.QRect(0, 0, 698, 272))
        self.IOAreaPanel.setObjectName("IOAreaPanel")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.IOAreaPanel)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.IOLayout = QtWidgets.QSplitter(self.IOAreaPanel)
        self.IOLayout.setOrientation(QtCore.Qt.Horizontal)
        self.IOLayout.setObjectName("IOLayout")
        self.widget = QtWidgets.QWidget(self.IOLayout)
        self.widget.setObjectName("widget")
        self.InputPanelLayout = QtWidgets.QVBoxLayout(self.widget)
        self.InputPanelLayout.setContentsMargins(0, 0, 0, 0)
        self.InputPanelLayout.setObjectName("InputPanelLayout")
        self.InputTips = QtWidgets.QLabel(self.widget)
        self.InputTips.setObjectName("InputTips")
        self.InputPanelLayout.addWidget(self.InputTips)
        self.InputBoxLayout = QtWidgets.QHBoxLayout()
        self.InputBoxLayout.setObjectName("InputBoxLayout")
        self.InputBox = QtWidgets.QTextEdit(self.widget)
        self.InputBox.setObjectName("InputBox")
        self.InputBoxLayout.addWidget(self.InputBox)
        self.InputWorkButtonLayout = QtWidgets.QVBoxLayout()
        self.InputWorkButtonLayout.setObjectName("InputWorkButtonLayout")
        self.OpenFileButton = QtWidgets.QPushButton(self.widget)
        self.OpenFileButton.setObjectName("OpenFileButton")
        self.InputWorkButtonLayout.addWidget(self.OpenFileButton)
        self.EvalCheckBox = QtWidgets.QCheckBox(self.widget)
        self.EvalCheckBox.setObjectName("EvalCheckBox")
        self.InputWorkButtonLayout.addWidget(self.EvalCheckBox)
        self.BigCheckBox = QtWidgets.QCheckBox(self.widget)
        self.BigCheckBox.setObjectName("BigCheckBox")
        self.InputWorkButtonLayout.addWidget(self.BigCheckBox)
        self.InputBoxLayout.addLayout(self.InputWorkButtonLayout)
        self.InputPanelLayout.addLayout(self.InputBoxLayout)
        self.layoutWidget = QtWidgets.QWidget(self.IOLayout)
        self.layoutWidget.setObjectName("layoutWidget")
        self.OutputPanelLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.OutputPanelLayout.setContentsMargins(0, 0, 0, 0)
        self.OutputPanelLayout.setObjectName("OutputPanelLayout")
        self.OutputTips = QtWidgets.QLabel(self.layoutWidget)
        self.OutputTips.setObjectName("OutputTips")
        self.OutputPanelLayout.addWidget(self.OutputTips)
        self.OutputBoxLayout = QtWidgets.QHBoxLayout()
        self.OutputBoxLayout.setObjectName("OutputBoxLayout")
        self.OutputBox = QtWidgets.QTextEdit(self.layoutWidget)
        self.OutputBox.setObjectName("OutputBox")
        self.OutputBoxLayout.addWidget(self.OutputBox)
        self.SaveFileButton = QtWidgets.QPushButton(self.layoutWidget)
        self.SaveFileButton.setObjectName("SaveFileButton")
        self.OutputBoxLayout.addWidget(self.SaveFileButton)
        self.OutputPanelLayout.addLayout(self.OutputBoxLayout)
        self.horizontalLayout_3.addWidget(self.IOLayout)
        self.IOArea.setWidget(self.IOAreaPanel)
        self.FileAndOptionsLayout = QtWidgets.QSplitter(self.OperationLayout)
        self.FileAndOptionsLayout.setOrientation(QtCore.Qt.Vertical)
        self.FileAndOptionsLayout.setObjectName("FileAndOptionsLayout")
        self.OptionsArea = QtWidgets.QScrollArea(self.FileAndOptionsLayout)
        self.OptionsArea.setWidgetResizable(True)
        self.OptionsArea.setObjectName("OptionsArea")
        self.OptionsAreaPanel = QtWidgets.QWidget()
        self.OptionsAreaPanel.setGeometry(QtCore.QRect(0, 0, 252, 449))
        self.OptionsAreaPanel.setObjectName("OptionsAreaPanel")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.OptionsAreaPanel)
        self.verticalLayout.setObjectName("verticalLayout")
        self.OptionsTips = QtWidgets.QLabel(self.OptionsAreaPanel)
        self.OptionsTips.setObjectName("OptionsTips")
        self.verticalLayout.addWidget(self.OptionsTips)
        self.OptionsBox = QtWidgets.QListView(self.OptionsAreaPanel)
        self.OptionsBox.setObjectName("OptionsBox")
        self.verticalLayout.addWidget(self.OptionsBox)
        self.OptionsArea.setWidget(self.OptionsAreaPanel)
        self.FileTempStackArea = QtWidgets.QScrollArea(self.FileAndOptionsLayout)
        self.FileTempStackArea.setWidgetResizable(True)
        self.FileTempStackArea.setObjectName("FileTempStackArea")
        self.FileTempStackAreaPanel = QtWidgets.QWidget()
        self.FileTempStackAreaPanel.setGeometry(QtCore.QRect(0, 0, 252, 246))
        self.FileTempStackAreaPanel.setObjectName("FileTempStackAreaPanel")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.FileTempStackAreaPanel)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.FileTempStackTips = QtWidgets.QLabel(self.FileTempStackAreaPanel)
        self.FileTempStackTips.setObjectName("FileTempStackTips")
        self.verticalLayout_2.addWidget(self.FileTempStackTips)
        self.FileTempStack = QtWidgets.QListView(self.FileTempStackAreaPanel)
        self.FileTempStack.setObjectName("FileTempStack")
        self.verticalLayout_2.addWidget(self.FileTempStack)
        self.FileTempStackArea.setWidget(self.FileTempStackAreaPanel)
        self.verticalLayout_7.addWidget(self.CryptoLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.InputTips.setText(_translate("Form", "输入"))
        self.OpenFileButton.setText(_translate("Form", "打开..."))
        self.EvalCheckBox.setText(_translate("Form", "eval"))
        self.BigCheckBox.setText(_translate("Form", "大文件"))
        self.OutputTips.setText(_translate("Form", "输出"))
        self.SaveFileButton.setText(_translate("Form", "另存为.."))
        self.OptionsTips.setText(_translate("Form", "节点选项"))
        self.FileTempStackTips.setText(_translate("Form", "暂存池"))
