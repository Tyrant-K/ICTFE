from PyQt5 import QtCore, QtGui, QtWidgets
from ui_Widgets import uni_Widget


class ui_HexPanel(QtWidgets.QWidget):
    def __init__(self):
        super(ui_HexPanel, self).__init__()
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.HexSplitTips = uni_Widget.ICTFELabel(self)
        self.HexSplitTips.setObjectName("HexSplitTips")
        self.horizontalLayout.addWidget(self.HexSplitTips)
        self.HexSplitBox = uni_Widget.ICTFELineBox(self)
        self.HexSplitBox.setObjectName("HexSplitBox")
        self.horizontalLayout.addWidget(self.HexSplitBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.HexEncodeButton = uni_Widget.ICTFEButton(self)
        self.HexEncodeButton.setMinimumSize(QtCore.QSize(120, 45))
        self.HexEncodeButton.setMaximumSize(QtCore.QSize(120, 45))
        self.HexEncodeButton.setObjectName("HexEncodeButton")
        self.horizontalLayout.addWidget(self.HexEncodeButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.HexTextBox = uni_Widget.ICTFETextBox(self)
        self.HexTextBox.setObjectName("HexTextBox")
        self.verticalLayout.addWidget(self.HexTextBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.HexDecodeButton = uni_Widget.ICTFEButton(self)
        self.HexDecodeButton.setMinimumSize(QtCore.QSize(120, 45))
        self.HexDecodeButton.setMaximumSize(QtCore.QSize(120, 45))
        self.HexDecodeButton.setObjectName("HexDecodeButton")
        self.horizontalLayout_2.addWidget(self.HexDecodeButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.HexCipherBox = uni_Widget.ICTFETextBox(self)
        self.HexCipherBox.setObjectName("HexCipherBox")
        self.verticalLayout_2.addWidget(self.HexCipherBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.HexSplitTips.setText(_translate("self", "分隔符:"))
        self.HexEncodeButton.setText(_translate("self", "编码"))
        self.HexDecodeButton.setText(_translate("self", "解码"))