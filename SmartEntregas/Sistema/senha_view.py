# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'senhaMIufTm.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, Qt
from PySide6.QtGui import QCursor, QFont
from PySide6.QtWidgets import (QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(363, 317)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_alterar_senha = QFrame(Dialog)
        self.frame_alterar_senha.setObjectName(u"frame_alterar_senha")
        self.frame_alterar_senha.setStyleSheet(u"QLabel{\n"
"border: 0px solid black;\n"
"border-radius: 2px;\n"
"font: 700 12pt \"HeIvetica\";\n"
"}\n"
"\n"
"QLineEdit{\n"
"min-height: 29px;\n"
"max-height: 29px;\n"
"font: 12pt \"HeIvetica\";\n"
"}")
        self.frame_alterar_senha.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_alterar_senha.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_alterar_senha)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_confirmar_senha = QLabel(self.frame_alterar_senha)
        self.label_confirmar_senha.setObjectName(u"label_confirmar_senha")

        self.gridLayout.addWidget(self.label_confirmar_senha, 5, 0, 1, 2)

        self.botao_mostrar_nova_senha = QPushButton(self.frame_alterar_senha)
        self.botao_mostrar_nova_senha.setObjectName(u"botao_mostrar_nova_senha")
        self.botao_mostrar_nova_senha.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_mostrar_nova_senha.setStyleSheet(u"    QPushButton {\n"
"        background-color: white;\n"
"        color: black;\n"
"        border: 0px solid rgb(84,84,84);\n"
"        border-radius: 2px; \n"
"		font: 12pt \"HeIvetica\";\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(230,230,230);\n"
"        color: black;\n"
"        border: 1px solid rgb(84,84,84);\n"
"        border-radius: 2px; \n"
"		font: 12pt \"HeIvetica\";\n"
"    }")

        self.gridLayout.addWidget(self.botao_mostrar_nova_senha, 4, 1, 1, 2)

        self.label_alterar_senha = QLabel(self.frame_alterar_senha)
        self.label_alterar_senha.setObjectName(u"label_alterar_senha")
        font = QFont()
        font.setFamilies([u"Helvetica"])
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        self.label_alterar_senha.setFont(font)
        self.label_alterar_senha.setStyleSheet(u"font: 700 18pt \"Helvetica\";\n"
"border: 0px solid black;\n"
"border-radius: 2px;")
        self.label_alterar_senha.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_alterar_senha, 0, 0, 1, 3)

        self.lineEdit_senha_atual = QLineEdit(self.frame_alterar_senha)
        self.lineEdit_senha_atual.setObjectName(u"lineEdit_senha_atual")
        self.lineEdit_senha_atual.setStyleSheet(u"")

        self.gridLayout.addWidget(self.lineEdit_senha_atual, 2, 0, 1, 1)

        self.lineEdit_confirmar_senha = QLineEdit(self.frame_alterar_senha)
        self.lineEdit_confirmar_senha.setObjectName(u"lineEdit_confirmar_senha")

        self.gridLayout.addWidget(self.lineEdit_confirmar_senha, 6, 0, 1, 1)

        self.label_senha_atual = QLabel(self.frame_alterar_senha)
        self.label_senha_atual.setObjectName(u"label_senha_atual")

        self.gridLayout.addWidget(self.label_senha_atual, 1, 0, 1, 1)

        self.frame_botoes_alterar_senha = QFrame(self.frame_alterar_senha)
        self.frame_botoes_alterar_senha.setObjectName(u"frame_botoes_alterar_senha")
        self.frame_botoes_alterar_senha.setStyleSheet(u"    QPushButton {\n"
"        background-color: rgb(230,230,230);\n"
"        color: black;\n"
"        border: 1px solid rgb(84,84,84);\n"
"        border-radius: 2px; \n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(84,84,84);\n"
"        color: white;\n"
"        border: 1px solid black; \n"
"        border-radius: 2px; \n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"QFrame{\n"
"    border: 0px solid black;\n"
"    border-radius: 2px;\n"
"}")
        self.frame_botoes_alterar_senha.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_botoes_alterar_senha.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_botoes_alterar_senha)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.botao_salvar_nova_senha = QPushButton(self.frame_botoes_alterar_senha)
        self.botao_salvar_nova_senha.setObjectName(u"botao_salvar_nova_senha")
        self.botao_salvar_nova_senha.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_21.addWidget(self.botao_salvar_nova_senha)

        self.botao_cancelar_alterar_senha = QPushButton(self.frame_botoes_alterar_senha)
        self.botao_cancelar_alterar_senha.setObjectName(u"botao_cancelar_alterar_senha")
        self.botao_cancelar_alterar_senha.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_21.addWidget(self.botao_cancelar_alterar_senha)


        self.gridLayout.addWidget(self.frame_botoes_alterar_senha, 8, 0, 1, 3)

        self.label_correspondem = QLabel(self.frame_alterar_senha)
        self.label_correspondem.setObjectName(u"label_correspondem")
        self.label_correspondem.setStyleSheet(u"QLabel{\n"
"border: 0px solid black;\n"
"border-radius: 2px;\n"
"font: 8pt \"HeIvetica\";\n"
"}")

        self.gridLayout.addWidget(self.label_correspondem, 7, 0, 1, 1)

        self.botao_mostrar_senha_atual = QPushButton(self.frame_alterar_senha)
        self.botao_mostrar_senha_atual.setObjectName(u"botao_mostrar_senha_atual")
        self.botao_mostrar_senha_atual.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_mostrar_senha_atual.setStyleSheet(u"    QPushButton {\n"
"        background-color: white;\n"
"        color: black;\n"
"        border: 0px solid rgb(84,84,84);\n"
"        border-radius: 2px; \n"
"		font: 12pt \"HeIvetica\";\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(230,230,230);\n"
"        color: black;\n"
"        border: 1px solid rgb(84,84,84);\n"
"        border-radius: 2px; \n"
"		font: 12pt \"HeIvetica\";\n"
"    }")

        self.gridLayout.addWidget(self.botao_mostrar_senha_atual, 2, 1, 1, 2)

        self.label_nova_senha = QLabel(self.frame_alterar_senha)
        self.label_nova_senha.setObjectName(u"label_nova_senha")

        self.gridLayout.addWidget(self.label_nova_senha, 3, 0, 1, 1)

        self.lineEdit_nova_senha = QLineEdit(self.frame_alterar_senha)
        self.lineEdit_nova_senha.setObjectName(u"lineEdit_nova_senha")

        self.gridLayout.addWidget(self.lineEdit_nova_senha, 4, 0, 1, 1)

        self.botao_mostrar_confirmar_senha = QPushButton(self.frame_alterar_senha)
        self.botao_mostrar_confirmar_senha.setObjectName(u"botao_mostrar_confirmar_senha")
        self.botao_mostrar_confirmar_senha.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_mostrar_confirmar_senha.setStyleSheet(u"    QPushButton {\n"
"        background-color: white;\n"
"        color: black;\n"
"        border: 0px solid rgb(84,84,84);\n"
"        border-radius: 2px; \n"
"		font: 12pt \"HeIvetica\";\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(230,230,230);\n"
"        color: black;\n"
"        border: 1px solid rgb(84,84,84);\n"
"        border-radius: 2px; \n"
"		font: 12pt \"HeIvetica\";\n"
"    }")

        self.gridLayout.addWidget(self.botao_mostrar_confirmar_senha, 6, 1, 1, 2)


        self.verticalLayout.addWidget(self.frame_alterar_senha)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_confirmar_senha.setText(QCoreApplication.translate("Dialog", u"Confirmar senha", None))
        self.botao_mostrar_nova_senha.setText(QCoreApplication.translate("Dialog", u"Mostrar", None))
        self.label_alterar_senha.setText(QCoreApplication.translate("Dialog", u"Alterar Senha", None))
        self.label_senha_atual.setText(QCoreApplication.translate("Dialog", u"Senha atual", None))
        self.botao_salvar_nova_senha.setText(QCoreApplication.translate("Dialog", u"Salvar", None))
        self.botao_cancelar_alterar_senha.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.label_correspondem.setText("")
        self.botao_mostrar_senha_atual.setText(QCoreApplication.translate("Dialog", u"Mostrar", None))
        self.label_nova_senha.setText(QCoreApplication.translate("Dialog", u"Nova senha", None))
        self.botao_mostrar_confirmar_senha.setText(QCoreApplication.translate("Dialog", u"Mostrar", None))
    # retranslateUi

