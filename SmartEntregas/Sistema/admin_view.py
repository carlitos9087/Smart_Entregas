# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'telasNOzHYN.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication,
    QMetaObject, QRect,
    QSize, Qt)
from PySide6.QtGui import (QCursor,
    QFont)
from PySide6.QtWidgets import ( QComboBox, QFrame, QGraphicsView,
    QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(804, 655)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setPointSize(12)
        self.centralwidget.setFont(font)
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_telas = QFrame(self.centralwidget)
        self.frame_telas.setObjectName(u"frame_telas")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_telas.sizePolicy().hasHeightForWidth())
        self.frame_telas.setSizePolicy(sizePolicy)
        self.frame_telas.setStyleSheet(u"font: 12pt \"HeIvetica\";")
        self.frame_telas.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_telas.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_telas)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_menu = QFrame(self.frame_telas)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setStyleSheet(u"QFrame{\n"
"border: 0px;\n"
"}\n"
"    QPushButton {\n"
"        background-color: rgb(230,230,230); /* Cor de fundo */\n"
"        color: black; /* Cor do texto */\n"
"        border: 1px solid rgb(84,84,84);/* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(84,84,84); /* Cor de fundo */\n"
"        color: white; /* Cor do texto */\n"
"        border: 1px solid black; /* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }")
        self.frame_menu.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_menu)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)

        self.botao_home = QPushButton(self.frame_menu)
        self.botao_home.setObjectName(u"botao_home")
        self.botao_home.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.botao_home)

        self.botao_configurar_conta = QPushButton(self.frame_menu)
        self.botao_configurar_conta.setObjectName(u"botao_configurar_conta")
        self.botao_configurar_conta.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.botao_configurar_conta)

        self.botao_sair = QPushButton(self.frame_menu)
        self.botao_sair.setObjectName(u"botao_sair")
        self.botao_sair.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.botao_sair, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.frame_menu)

        self.stackedWidget = QStackedWidget(self.frame_telas)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pag_conteudo = QWidget()
        self.pag_conteudo.setObjectName(u"pag_conteudo")
        self.verticalLayout_11 = QVBoxLayout(self.pag_conteudo)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.tabWidget_telas = QTabWidget(self.pag_conteudo)
        self.tabWidget_telas.setObjectName(u"tabWidget_telas")
        self.tabWidget_telas.setCursor(QCursor(Qt.ArrowCursor))
        self.tab_cadastro_pacotes = QWidget()
        self.tab_cadastro_pacotes.setObjectName(u"tab_cadastro_pacotes")
        self.horizontalLayout_19 = QHBoxLayout(self.tab_cadastro_pacotes)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.frame_cadastro_pacotes = QFrame(self.tab_cadastro_pacotes)
        self.frame_cadastro_pacotes.setObjectName(u"frame_cadastro_pacotes")
        self.frame_cadastro_pacotes.setStyleSheet(u"QLabel{\n"
"border: 1px solid black;\n"
"border-radius: 2px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 1px solid black;\n"
"border-radius: 2px;\n"
"}")
        self.frame_cadastro_pacotes.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_cadastro_pacotes.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_cadastro_pacotes)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_descricao = QLineEdit(self.frame_cadastro_pacotes)
        self.lineEdit_descricao.setObjectName(u"lineEdit_descricao")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_descricao.sizePolicy().hasHeightForWidth())
        self.lineEdit_descricao.setSizePolicy(sizePolicy1)
        self.lineEdit_descricao.setStyleSheet(u"    min-height: 29px;\n"
"    max-height: 29px;")

        self.gridLayout.addWidget(self.lineEdit_descricao, 2, 1, 1, 3)

        self.label_peso = QLabel(self.frame_cadastro_pacotes)
        self.label_peso.setObjectName(u"label_peso")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_peso.sizePolicy().hasHeightForWidth())
        self.label_peso.setSizePolicy(sizePolicy2)
        self.label_peso.setStyleSheet(u"min-height: 29px;\n"
"max-height: 29px;\n"
"font: 700 12pt \"HeIvetica\";")

        self.gridLayout.addWidget(self.label_peso, 5, 2, 1, 1)

        self.botao_realizar_cadastro = QPushButton(self.frame_cadastro_pacotes)
        self.botao_realizar_cadastro.setObjectName(u"botao_realizar_cadastro")
        self.botao_realizar_cadastro.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_realizar_cadastro.setStyleSheet(u"    QPushButton {\n"
"        background-color: rgb(230,230,230); /* Cor de fundo */\n"
"        color: black; /* Cor do texto */\n"
"        border: 1px solid rgb(84,84,84);/* Borda */\n"
"        border-radius: 10px; /* Cantos arredondados */\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(84,84,84); /* Cor de fundo */\n"
"        color: white; /* Cor do texto */\n"
"        border: 1px solid black; /* Borda */\n"
"        border-radius: 10px; /* Cantos arredondados */\n"
"    }\n"
"min-height: 29px;\n"
"max-height: 29px;\n"
"font: 700 12pt \"HeIvetica\";")

        self.gridLayout.addWidget(self.botao_realizar_cadastro, 5, 4, 1, 1)

        self.lineEdit_id_morador = QLineEdit(self.frame_cadastro_pacotes)
        self.lineEdit_id_morador.setObjectName(u"lineEdit_id_morador")
        sizePolicy1.setHeightForWidth(self.lineEdit_id_morador.sizePolicy().hasHeightForWidth())
        self.lineEdit_id_morador.setSizePolicy(sizePolicy1)
        self.lineEdit_id_morador.setStyleSheet(u"    min-height: 29px;\n"
"    max-height: 29px;")

        self.gridLayout.addWidget(self.lineEdit_id_morador, 3, 1, 1, 3)

        self.label_resultado_cadastro = QLabel(self.frame_cadastro_pacotes)
        self.label_resultado_cadastro.setObjectName(u"label_resultado_cadastro")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_resultado_cadastro.sizePolicy().hasHeightForWidth())
        self.label_resultado_cadastro.setSizePolicy(sizePolicy3)
        self.label_resultado_cadastro.setStyleSheet(u"    min-height: 102px;\n"
"   ")

        self.gridLayout.addWidget(self.label_resultado_cadastro, 2, 4, 3, 1)

        self.label_descricao = QLabel(self.frame_cadastro_pacotes)
        self.label_descricao.setObjectName(u"label_descricao")
        sizePolicy2.setHeightForWidth(self.label_descricao.sizePolicy().hasHeightForWidth())
        self.label_descricao.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setFamilies([u"HeIvetica"])
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        self.label_descricao.setFont(font1)
        self.label_descricao.setStyleSheet(u"min-height: 29px;\n"
"max-height: 29px;\n"
"font: 700 12pt \"HeIvetica\";\n"
"\n"
"")

        self.gridLayout.addWidget(self.label_descricao, 2, 0, 1, 1)

        self.lineEdit_volume = QLineEdit(self.frame_cadastro_pacotes)
        self.lineEdit_volume.setObjectName(u"lineEdit_volume")
        sizePolicy1.setHeightForWidth(self.lineEdit_volume.sizePolicy().hasHeightForWidth())
        self.lineEdit_volume.setSizePolicy(sizePolicy1)
        self.lineEdit_volume.setStyleSheet(u"    min-height: 29px;\n"
"    max-height: 29px;")

        self.gridLayout.addWidget(self.lineEdit_volume, 5, 1, 1, 1)

        self.label_status = QLabel(self.frame_cadastro_pacotes)
        self.label_status.setObjectName(u"label_status")
        sizePolicy2.setHeightForWidth(self.label_status.sizePolicy().hasHeightForWidth())
        self.label_status.setSizePolicy(sizePolicy2)
        self.label_status.setStyleSheet(u"min-height: 29px;\n"
"max-height: 29px;\n"
"font: 700 12pt \"HeIvetica\";")

        self.gridLayout.addWidget(self.label_status, 4, 0, 1, 1)

        self.lineEdit_peso = QLineEdit(self.frame_cadastro_pacotes)
        self.lineEdit_peso.setObjectName(u"lineEdit_peso")
        sizePolicy1.setHeightForWidth(self.lineEdit_peso.sizePolicy().hasHeightForWidth())
        self.lineEdit_peso.setSizePolicy(sizePolicy1)
        self.lineEdit_peso.setStyleSheet(u"    min-height: 29px;\n"
"    max-height: 29px;")

        self.gridLayout.addWidget(self.lineEdit_peso, 5, 3, 1, 1)

        self.lineEdit_status = QLineEdit(self.frame_cadastro_pacotes)
        self.lineEdit_status.setObjectName(u"lineEdit_status")
        sizePolicy1.setHeightForWidth(self.lineEdit_status.sizePolicy().hasHeightForWidth())
        self.lineEdit_status.setSizePolicy(sizePolicy1)
        self.lineEdit_status.setStyleSheet(u"    min-height: 29px;\n"
"    max-height: 29px;")

        self.gridLayout.addWidget(self.lineEdit_status, 4, 1, 1, 3)

        self.label_cadastro_pacotes = QLabel(self.frame_cadastro_pacotes)
        self.label_cadastro_pacotes.setObjectName(u"label_cadastro_pacotes")
        sizePolicy2.setHeightForWidth(self.label_cadastro_pacotes.sizePolicy().hasHeightForWidth())
        self.label_cadastro_pacotes.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamilies([u"Helvetica"])
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setItalic(False)
        self.label_cadastro_pacotes.setFont(font2)
        self.label_cadastro_pacotes.setStyleSheet(u"font: 700 18pt \"Helvetica\";\n"
"border: 0px solid black;\n"
"border-radius: 2px;\n"
"\n"
"\n"
"\n"
"")
        self.label_cadastro_pacotes.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_cadastro_pacotes, 1, 0, 1, 5)

        self.label_volume = QLabel(self.frame_cadastro_pacotes)
        self.label_volume.setObjectName(u"label_volume")
        sizePolicy2.setHeightForWidth(self.label_volume.sizePolicy().hasHeightForWidth())
        self.label_volume.setSizePolicy(sizePolicy2)
        self.label_volume.setStyleSheet(u"min-height: 29px;\n"
"max-height: 29px;\n"
"font: 700 12pt \"HeIvetica\";")

        self.gridLayout.addWidget(self.label_volume, 5, 0, 1, 1)

        self.label_id_morador = QLabel(self.frame_cadastro_pacotes)
        self.label_id_morador.setObjectName(u"label_id_morador")
        sizePolicy2.setHeightForWidth(self.label_id_morador.sizePolicy().hasHeightForWidth())
        self.label_id_morador.setSizePolicy(sizePolicy2)
        self.label_id_morador.setStyleSheet(u"min-height: 29px;\n"
"max-height: 29px;\n"
"font: 700 12pt \"HeIvetica\";")

        self.gridLayout.addWidget(self.label_id_morador, 3, 0, 1, 1)

        self.verticalSpacer_topo_pacote = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.gridLayout.addItem(self.verticalSpacer_topo_pacote, 0, 0, 1, 5)

        self.verticalSpacer_embaixo_pacote = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.gridLayout.addItem(self.verticalSpacer_embaixo_pacote, 6, 0, 1, 5)


        self.horizontalLayout_19.addWidget(self.frame_cadastro_pacotes)

        self.tabWidget_telas.addTab(self.tab_cadastro_pacotes, "")
        self.tab_criacao_remessa = QWidget()
        self.tab_criacao_remessa.setObjectName(u"tab_criacao_remessa")
        self.horizontalLayout_8 = QHBoxLayout(self.tab_criacao_remessa)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.scrollArea = QScrollArea(self.tab_criacao_remessa)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 752, 659))
        self.verticalLayout_10 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_criacao_remessas = QLabel(self.scrollAreaWidgetContents)
        self.label_criacao_remessas.setObjectName(u"label_criacao_remessas")
        self.label_criacao_remessas.setStyleSheet(u"font: 700 18pt \"HeIvetica\";\n"
"border: 0px solid black;\n"
"border-radius: 2px;\n"
"background-color: rgb(255, 255, 255);")
        self.label_criacao_remessas.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_criacao_remessas)

        self.frame_tabelas_mapa = QFrame(self.scrollAreaWidgetContents)
        self.frame_tabelas_mapa.setObjectName(u"frame_tabelas_mapa")
        sizePolicy2.setHeightForWidth(self.frame_tabelas_mapa.sizePolicy().hasHeightForWidth())
        self.frame_tabelas_mapa.setSizePolicy(sizePolicy2)
        self.frame_tabelas_mapa.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_tabelas_mapa.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_tabelas_mapa)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.tableWidget_morador = QTableWidget(self.frame_tabelas_mapa)
        if (self.tableWidget_morador.columnCount() < 4):
            self.tableWidget_morador.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_morador.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_morador.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_morador.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_morador.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_morador.setObjectName(u"tableWidget_morador")
        self.tableWidget_morador.setStyleSheet(u"QTableWidget {\n"
"    border: 1px solid black;\n"
"    border-radius: 2px;\n"
"}")

        self.horizontalLayout_10.addWidget(self.tableWidget_morador)

        self.tableWidget_pacote = QTableWidget(self.frame_tabelas_mapa)
        if (self.tableWidget_pacote.columnCount() < 6):
            self.tableWidget_pacote.setColumnCount(6)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_pacote.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_pacote.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_pacote.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_pacote.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_pacote.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_pacote.setHorizontalHeaderItem(5, __qtablewidgetitem9)
        self.tableWidget_pacote.setObjectName(u"tableWidget_pacote")
        self.tableWidget_pacote.setStyleSheet(u"QTableWidget {\n"
"    border: 1px solid black;\n"
"    border-radius: 2px;\n"
"}\n"
"")

        self.horizontalLayout_10.addWidget(self.tableWidget_pacote)

        self.frame_mapa_remessa = QFrame(self.frame_tabelas_mapa)
        self.frame_mapa_remessa.setObjectName(u"frame_mapa_remessa")
        self.frame_mapa_remessa.setStyleSheet(u"QFrame {\n"
"    border: 1px solid black;\n"
"    border-radius: 2px;\n"
"}")
        self.frame_mapa_remessa.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_mapa_remessa.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_mapa_remessa)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_mapa_remessa = QLabel(self.frame_mapa_remessa)
        self.label_mapa_remessa.setObjectName(u"label_mapa_remessa")
        self.label_mapa_remessa.setStyleSheet(u"border: 0px solid black;\n"
"font: 700 12pt \"HeIvetica\";")

        self.verticalLayout_9.addWidget(self.label_mapa_remessa)

        self.graphicsView_remessa = QGraphicsView(self.frame_mapa_remessa)
        self.graphicsView_remessa.setObjectName(u"graphicsView_remessa")

        self.verticalLayout_9.addWidget(self.graphicsView_remessa)


        self.horizontalLayout_10.addWidget(self.frame_mapa_remessa)


        self.verticalLayout_10.addWidget(self.frame_tabelas_mapa)

        self.frame_remessa_json = QFrame(self.scrollAreaWidgetContents)
        self.frame_remessa_json.setObjectName(u"frame_remessa_json")
        self.frame_remessa_json.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_remessa_json.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_remessa_json)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_dados_remessa = QFrame(self.frame_remessa_json)
        self.frame_dados_remessa.setObjectName(u"frame_dados_remessa")
        self.frame_dados_remessa.setStyleSheet(u"QFrame {\n"
"    border: 1px solid black;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"\n"
"QLabel{\n"
"border: 1px solid black;\n"
"border-radius: 2px;\n"
"font: 700 12pt \"HeIvetica\";\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 1px solid black;\n"
"border-radius: 2px;\n"
"}\n"
"\n"
"\n"
"")
        self.frame_dados_remessa.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_dados_remessa.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_dados_remessa)
        self.gridLayout_3.setObjectName(u"gridLayout_3")



        self.label_id_pacote_1 = QLabel(self.frame_dados_remessa)
        self.label_id_pacote_1.setObjectName(u"label_id_pacote_1")
        self.label_id_pacote_1.setStyleSheet(u"min-width: 95px;")

        self.gridLayout_3.addWidget(self.label_id_pacote_1, 2, 0, 1, 1)

        self.label_endereco_1 = QLabel(self.frame_dados_remessa)
        self.label_endereco_1.setObjectName(u"label_endereco_1")
        self.label_endereco_1.setStyleSheet(u"min-width: 95px;")

        self.gridLayout_3.addWidget(self.label_endereco_1, 3, 0, 1, 1)


        self.label_compartimento_1 = QLabel(self.frame_dados_remessa)
        self.label_compartimento_1.setObjectName(u"label_compartimento_1")
        self.label_compartimento_1.setStyleSheet(u"min-width: 198px;")

        self.gridLayout_3.addWidget(self.label_compartimento_1, 1, 0, 1, 2)

        self.lineEdit_id_pacote_1 = QLineEdit(self.frame_dados_remessa)
        self.lineEdit_id_pacote_1.setObjectName(u"lineEdit_id_pacote_1")
        self.lineEdit_id_pacote_1.setStyleSheet(u"min-width: 95px;")

        self.gridLayout_3.addWidget(self.lineEdit_id_pacote_1, 2, 1, 1, 1)

        self.label_texto_endereco_1 = QLabel(self.frame_dados_remessa)
        self.label_texto_endereco_1.setObjectName(u"label_texto_endereco_1")
        self.label_texto_endereco_1.setStyleSheet(u"font: 12pt \"HeIvetica\";\n"
"min-width: 95px;")

        self.gridLayout_3.addWidget(self.label_texto_endereco_1, 3, 1, 1, 1)


        self.label_endereco_2 = QLabel(self.frame_dados_remessa)
        self.label_endereco_2.setObjectName(u"label_endereco_2")
        self.label_endereco_2.setStyleSheet(u"min-width: 95px;")

        self.gridLayout_3.addWidget(self.label_endereco_2, 3, 2, 1, 1)

        self.label_id_pacote_2 = QLabel(self.frame_dados_remessa)
        self.label_id_pacote_2.setObjectName(u"label_id_pacote_2")
        self.label_id_pacote_2.setStyleSheet(u"min-width: 95px;")

        self.gridLayout_3.addWidget(self.label_id_pacote_2, 2, 2, 1, 1)

        self.label_compartimento_2 = QLabel(self.frame_dados_remessa)
        self.label_compartimento_2.setObjectName(u"label_compartimento_2")
        self.label_compartimento_2.setStyleSheet(u"min-width: 198px;")

        self.gridLayout_3.addWidget(self.label_compartimento_2, 1, 2, 1, 3)

        self.lineEdit_id_pacote_2 = QLineEdit(self.frame_dados_remessa)
        self.lineEdit_id_pacote_2.setObjectName(u"lineEdit_id_pacote_2")
        self.lineEdit_id_pacote_2.setStyleSheet(u"min-width: 95px;")

        self.gridLayout_3.addWidget(self.lineEdit_id_pacote_2, 2, 3, 1, 2)

        self.label_texto_endereco_2 = QLabel(self.frame_dados_remessa)
        self.label_texto_endereco_2.setObjectName(u"label_texto_endereco_2")
        self.label_texto_endereco_2.setStyleSheet(u"font: 12pt \"HeIvetica\";\n"
"min-width: 95px;")

        self.gridLayout_3.addWidget(self.label_texto_endereco_2, 3, 3, 1, 2)



        self.horizontalLayout_9.addWidget(self.frame_dados_remessa)

        self.frame_iniciar_remessa = QFrame(self.frame_remessa_json)
        self.frame_iniciar_remessa.setObjectName(u"frame_iniciar_remessa")
        sizePolicy.setHeightForWidth(self.frame_iniciar_remessa.sizePolicy().hasHeightForWidth())
        self.frame_iniciar_remessa.setSizePolicy(sizePolicy)
        self.frame_iniciar_remessa.setStyleSheet(u"QFrame {\n"
                                            "    border: 1px solid black;\n"
                                            "    border-radius: 2px;\n"
                                            "}")
        self.frame_iniciar_remessa.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_iniciar_remessa.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_iniciar_remessa)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")

        self.QlineEdit_Id_Remessa = QLineEdit(self.frame_iniciar_remessa)
        self.QlineEdit_Id_Remessa.setObjectName(u"QlineEdit_Id_Remessa")
        self.QlineEdit_Id_Remessa.setStyleSheet(u"border: 0px solid black;\n"
                                                 "font: 700 12pt \"HeIvetica\";\n")

        self.botao_iniciar_remessa = QPushButton(self.frame_iniciar_remessa)
        self.botao_iniciar_remessa.setObjectName(u"botao_iniciar_remessa")
        self.botao_iniciar_remessa.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_8.addWidget(self.botao_iniciar_remessa)

        self.verticalLayout_8.addWidget(self.QlineEdit_Id_Remessa)

        self.horizontalLayout_9.addWidget(self.frame_iniciar_remessa)

        self.botao_json_remessa = QPushButton(self.frame_dados_remessa)
        self.botao_json_remessa.setObjectName(u"botao_json_remessa")
        self.botao_json_remessa.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_json_remessa.setStyleSheet(u"    QPushButton {\n"
"        background-color: rgb(230,230,230); /* Cor de fundo */\n"
"        color: black; /* Cor do texto */\n"
"        border: 1px solid rgb(84,84,84);/* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(84,84,84); /* Cor de fundo */\n"
"        color: white; /* Cor do texto */\n"
"        border: 1px solid black; /* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"")

        self.gridLayout_3.addWidget(self.botao_json_remessa, 0, 5, 2, 1)


        self.verticalLayout_10.addWidget(self.frame_remessa_json)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_8.addWidget(self.scrollArea)

        self.tabWidget_telas.addTab(self.tab_criacao_remessa, "")


        self.tab_listas = QWidget()
        self.tab_listas.setObjectName(u"tab_listas")
        self.gridLayout_5 = QGridLayout(self.tab_listas)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tabWidget_listas = QTabWidget(self.tab_listas)
        self.tabWidget_listas.setObjectName(u"tabWidget_listas")
        self.tabWidget_listas.setCursor(QCursor(Qt.ArrowCursor))
        self.tab_pacotes = QWidget()
        self.tab_pacotes.setObjectName(u"tab_pacotes")
        self.gridLayout_8 = QGridLayout(self.tab_pacotes)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.frame_alteracoes_pacote = QFrame(self.tab_pacotes)
        self.frame_alteracoes_pacote.setObjectName(u"frame_alteracoes_pacote")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_alteracoes_pacote.sizePolicy().hasHeightForWidth())
        self.frame_alteracoes_pacote.setSizePolicy(sizePolicy6)
        self.frame_alteracoes_pacote.setStyleSheet(u"QLabel{\n"
"border: 1px solid black;\n"
"border-radius: 2px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 1px solid black;\n"
"border-radius: 2px;\n"
"}\n"
"QFrame{\n"
"    border: 0px solid black;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"font: 12pt \"HeIvetica\";")
        self.frame_alteracoes_pacote.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_alteracoes_pacote.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_alteracoes_pacote)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_volume_alterar = QLabel(self.frame_alteracoes_pacote)
        self.label_volume_alterar.setObjectName(u"label_volume_alterar")
        sizePolicy2.setHeightForWidth(self.label_volume_alterar.sizePolicy().hasHeightForWidth())
        self.label_volume_alterar.setSizePolicy(sizePolicy2)
        self.label_volume_alterar.setStyleSheet(u"font: 700 12pt \"HeIvetica\";")

        self.gridLayout_4.addWidget(self.label_volume_alterar, 6, 0, 1, 1)

        self.lineEdit_id_morador_alterar = QLineEdit(self.frame_alteracoes_pacote)
        self.lineEdit_id_morador_alterar.setObjectName(u"lineEdit_id_morador_alterar")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.lineEdit_id_morador_alterar.sizePolicy().hasHeightForWidth())
        self.lineEdit_id_morador_alterar.setSizePolicy(sizePolicy7)
        self.lineEdit_id_morador_alterar.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.lineEdit_id_morador_alterar, 4, 1, 1, 1)

        self.label_id_morador_alterar = QLabel(self.frame_alteracoes_pacote)
        self.label_id_morador_alterar.setObjectName(u"label_id_morador_alterar")
        sizePolicy2.setHeightForWidth(self.label_id_morador_alterar.sizePolicy().hasHeightForWidth())
        self.label_id_morador_alterar.setSizePolicy(sizePolicy2)
        self.label_id_morador_alterar.setStyleSheet(u"font: 700 12pt \"HeIvetica\";")

        self.gridLayout_4.addWidget(self.label_id_morador_alterar, 4, 0, 1, 1)

        self.lineEdit_status_alterar = QLineEdit(self.frame_alteracoes_pacote)
        self.lineEdit_status_alterar.setObjectName(u"lineEdit_status_alterar")
        sizePolicy7.setHeightForWidth(self.lineEdit_status_alterar.sizePolicy().hasHeightForWidth())
        self.lineEdit_status_alterar.setSizePolicy(sizePolicy7)
        self.lineEdit_status_alterar.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.lineEdit_status_alterar, 5, 1, 1, 1)

        self.lineEdit_volume_alterar = QLineEdit(self.frame_alteracoes_pacote)
        self.lineEdit_volume_alterar.setObjectName(u"lineEdit_volume_alterar")
        sizePolicy7.setHeightForWidth(self.lineEdit_volume_alterar.sizePolicy().hasHeightForWidth())
        self.lineEdit_volume_alterar.setSizePolicy(sizePolicy7)
        self.lineEdit_volume_alterar.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.lineEdit_volume_alterar, 6, 1, 1, 1)

        self.label_alterar_pacote = QLabel(self.frame_alteracoes_pacote)
        self.label_alterar_pacote.setObjectName(u"label_alterar_pacote")
        self.label_alterar_pacote.setStyleSheet(u"font: 700 14pt \"HeIvetica\";\n"
"border: 0px solid black;\n"
"border-radius: 2px;")

        self.gridLayout_4.addWidget(self.label_alterar_pacote, 0, 0, 1, 2)

        self.label_status_alterar = QLabel(self.frame_alteracoes_pacote)
        self.label_status_alterar.setObjectName(u"label_status_alterar")
        sizePolicy2.setHeightForWidth(self.label_status_alterar.sizePolicy().hasHeightForWidth())
        self.label_status_alterar.setSizePolicy(sizePolicy2)
        self.label_status_alterar.setStyleSheet(u"font: 700 12pt \"HeIvetica\";")

        self.gridLayout_4.addWidget(self.label_status_alterar, 5, 0, 1, 1)

        self.frame_botoes_alterar_pacote = QFrame(self.frame_alteracoes_pacote)
        self.frame_botoes_alterar_pacote.setObjectName(u"frame_botoes_alterar_pacote")
        sizePolicy.setHeightForWidth(self.frame_botoes_alterar_pacote.sizePolicy().hasHeightForWidth())
        self.frame_botoes_alterar_pacote.setSizePolicy(sizePolicy)
        self.frame_botoes_alterar_pacote.setStyleSheet(u"    QPushButton {\n"
"        background-color: rgb(230,230,230); /* Cor de fundo */\n"
"        color: black; /* Cor do texto */\n"
"        border: 1px solid rgb(84,84,84);/* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(84,84,84); /* Cor de fundo */\n"
"        color: white; /* Cor do texto */\n"
"        border: 1px solid black; /* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"QFrame{\n"
"    border: 0px solid black;\n"
"    border-radius: 2px;\n"
"}")
        self.frame_botoes_alterar_pacote.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_botoes_alterar_pacote.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_botoes_alterar_pacote)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.botao_salvar_alterar_pacote = QPushButton(self.frame_botoes_alterar_pacote)
        self.botao_salvar_alterar_pacote.setObjectName(u"botao_salvar_alterar_pacote")
        self.botao_salvar_alterar_pacote.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_12.addWidget(self.botao_salvar_alterar_pacote)

        self.botao_cancelar_alterar_pacote = QPushButton(self.frame_botoes_alterar_pacote)
        self.botao_cancelar_alterar_pacote.setObjectName(u"botao_cancelar_alterar_pacote")
        self.botao_cancelar_alterar_pacote.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_12.addWidget(self.botao_cancelar_alterar_pacote)


        self.gridLayout_4.addWidget(self.frame_botoes_alterar_pacote, 8, 0, 1, 2)

        self.label_peso_alterar = QLabel(self.frame_alteracoes_pacote)
        self.label_peso_alterar.setObjectName(u"label_peso_alterar")
        sizePolicy7.setHeightForWidth(self.label_peso_alterar.sizePolicy().hasHeightForWidth())
        self.label_peso_alterar.setSizePolicy(sizePolicy7)
        self.label_peso_alterar.setStyleSheet(u"font: 700 12pt \"HeIvetica\";")

        self.gridLayout_4.addWidget(self.label_peso_alterar, 7, 0, 1, 1)

        self.lineEdit_peso_alterar = QLineEdit(self.frame_alteracoes_pacote)
        self.lineEdit_peso_alterar.setObjectName(u"lineEdit_peso_alterar")
        sizePolicy7.setHeightForWidth(self.lineEdit_peso_alterar.sizePolicy().hasHeightForWidth())
        self.lineEdit_peso_alterar.setSizePolicy(sizePolicy7)
        self.lineEdit_peso_alterar.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.lineEdit_peso_alterar, 7, 1, 1, 1)

        self.linha_alterar_pacote = QFrame(self.frame_alteracoes_pacote)
        self.linha_alterar_pacote.setObjectName(u"linha_alterar_pacote")
        self.linha_alterar_pacote.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(0, 0, 0);\n"
"    max-height: 1px;\n"
"    min-height: 1px;\n"
"}\n"
"")
        self.linha_alterar_pacote.setFrameShape(QFrame.Shape.HLine)
        self.linha_alterar_pacote.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_4.addWidget(self.linha_alterar_pacote, 1, 0, 1, 2)

        self.lineEdit_descricao_alterar = QLineEdit(self.frame_alteracoes_pacote)
        self.lineEdit_descricao_alterar.setObjectName(u"lineEdit_descricao_alterar")
        sizePolicy7.setHeightForWidth(self.lineEdit_descricao_alterar.sizePolicy().hasHeightForWidth())
        self.lineEdit_descricao_alterar.setSizePolicy(sizePolicy7)
        self.lineEdit_descricao_alterar.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.lineEdit_descricao_alterar, 3, 1, 1, 1)

        self.label_descricao_alterar = QLabel(self.frame_alteracoes_pacote)
        self.label_descricao_alterar.setObjectName(u"label_descricao_alterar")
        sizePolicy2.setHeightForWidth(self.label_descricao_alterar.sizePolicy().hasHeightForWidth())
        self.label_descricao_alterar.setSizePolicy(sizePolicy2)
        self.label_descricao_alterar.setFont(font1)
        self.label_descricao_alterar.setStyleSheet(u"font: 700 12pt \"HeIvetica\";\n"
"\n"
"")

        self.gridLayout_4.addWidget(self.label_descricao_alterar, 3, 0, 1, 1)

        self.label_id_pacote_alterar_2 = QLabel(self.frame_alteracoes_pacote)
        self.label_id_pacote_alterar_2.setObjectName(u"label_id_pacote_alterar_2")
        self.label_id_pacote_alterar_2.setStyleSheet(u"font: 700 12pt \"HeIvetica\";")

        self.gridLayout_4.addWidget(self.label_id_pacote_alterar_2, 2, 0, 1, 1)

        self.label_id_pacote_num = QLabel(self.frame_alteracoes_pacote)
        self.label_id_pacote_num.setObjectName(u"label_id_pacote_num")
        self.label_id_pacote_num.setStyleSheet(u"QLabel{\n"
"border: 1px solid black;\n"
"border-radius: 2px;\n"
"	border-top-color: rgb(255, 255, 255);\n"
"	border-right-color: rgb(255, 255, 255);\n"
"	border-bottom-color: rgb(0, 0, 0);\n"
"	border-left-color: rgb(255, 255, 255);\n"
"}\n"
"font: 12pt \"HeIvetica\";")

        self.gridLayout_4.addWidget(self.label_id_pacote_num, 2, 1, 1, 1)


        self.gridLayout_8.addWidget(self.frame_alteracoes_pacote, 1, 3, 1, 1)

        self.tableWidget_lista_pacotes = QTableWidget(self.tab_pacotes)
        if (self.tableWidget_lista_pacotes.columnCount() < 6):
            self.tableWidget_lista_pacotes.setColumnCount(6)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_lista_pacotes.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_lista_pacotes.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_lista_pacotes.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_lista_pacotes.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_lista_pacotes.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_lista_pacotes.setHorizontalHeaderItem(5, __qtablewidgetitem15)
        self.tableWidget_lista_pacotes.setObjectName(u"tableWidget_lista_pacotes")
        sizePolicy6.setHeightForWidth(self.tableWidget_lista_pacotes.sizePolicy().hasHeightForWidth())
        self.tableWidget_lista_pacotes.setSizePolicy(sizePolicy6)
        self.tableWidget_lista_pacotes.setStyleSheet(u"QTableWidget {\n"
"    border: 1px solid black;\n"
"    border-radius: 2px;\n"
"}")

        self.gridLayout_8.addWidget(self.tableWidget_lista_pacotes, 0, 1, 2, 1)

        self.frame_filtro_pacotes = QFrame(self.tab_pacotes)
        self.frame_filtro_pacotes.setObjectName(u"frame_filtro_pacotes")
        sizePolicy6.setHeightForWidth(self.frame_filtro_pacotes.sizePolicy().hasHeightForWidth())
        self.frame_filtro_pacotes.setSizePolicy(sizePolicy6)
        self.frame_filtro_pacotes.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid black;\n"
"border-radius: 2px;\n"
"}\n"
"QFrame{\n"
"    border: 0px solid black;\n"
"    border-radius: 2px;\n"
"}\n"
"font: 12pt \"HeIvetica\";\n"
"")
        self.frame_filtro_pacotes.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_filtro_pacotes.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_filtro_pacotes)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_topo_filtro = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_topo_filtro)

        self.label_filtro = QLabel(self.frame_filtro_pacotes)
        self.label_filtro.setObjectName(u"label_filtro")
        font3 = QFont()
        font3.setFamilies([u"HeIvetica"])
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        font3.setKerning(True)
        self.label_filtro.setFont(font3)
        self.label_filtro.setStyleSheet(u"font: 700 14pt \"HeIvetica\";\n"
"border: 0px solid black;\n"
"border-radius: 2px;")

        self.verticalLayout_5.addWidget(self.label_filtro)

        self.linha_filtro = QFrame(self.frame_filtro_pacotes)
        self.linha_filtro.setObjectName(u"linha_filtro")
        self.linha_filtro.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(0, 0, 0);\n"
"    max-height: 1px;\n"
"    min-height: 1px;\n"
"}\n"
"")
        self.linha_filtro.setFrameShape(QFrame.Shape.HLine)
        self.linha_filtro.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_5.addWidget(self.linha_filtro)

        self.comboBox_filtro_pacotes = QComboBox(self.frame_filtro_pacotes)
        self.comboBox_filtro_pacotes.addItem("")
        self.comboBox_filtro_pacotes.addItem("")
        self.comboBox_filtro_pacotes.addItem("")
        self.comboBox_filtro_pacotes.addItem("")
        self.comboBox_filtro_pacotes.addItem("")
        self.comboBox_filtro_pacotes.addItem("")
        self.comboBox_filtro_pacotes.setObjectName(u"comboBox_filtro_pacotes")
        sizePolicy7.setHeightForWidth(self.comboBox_filtro_pacotes.sizePolicy().hasHeightForWidth())
        self.comboBox_filtro_pacotes.setSizePolicy(sizePolicy7)
        self.comboBox_filtro_pacotes.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_filtro_pacotes.setStyleSheet(u"    QComboBox {\n"
"        background-color: rgb(230,230,230); /* Cor de fundo */\n"
"        color: black; /* Cor do texto */\n"
"        border: 1px solid rgb(84,84,84);/* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"    QComboBox:pressed {\n"
"        background-color: rgb(84,84,84); /* Cor de fundo */\n"
"        color: white; /* Cor do texto */\n"
"        border: 1px solid black; /* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }")

        self.verticalLayout_5.addWidget(self.comboBox_filtro_pacotes)

        self.lineEdit_filtro_pacotes = QLineEdit(self.frame_filtro_pacotes)
        self.lineEdit_filtro_pacotes.setObjectName(u"lineEdit_filtro_pacotes")
        sizePolicy7.setHeightForWidth(self.lineEdit_filtro_pacotes.sizePolicy().hasHeightForWidth())
        self.lineEdit_filtro_pacotes.setSizePolicy(sizePolicy7)

        self.verticalLayout_5.addWidget(self.lineEdit_filtro_pacotes)

        self.frame_botoes_filtro = QFrame(self.frame_filtro_pacotes)
        self.frame_botoes_filtro.setObjectName(u"frame_botoes_filtro")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.frame_botoes_filtro.sizePolicy().hasHeightForWidth())
        self.frame_botoes_filtro.setSizePolicy(sizePolicy8)
        self.frame_botoes_filtro.setStyleSheet(u"    QPushButton {\n"
"        background-color: rgb(230,230,230); /* Cor de fundo */\n"
"        color: black; /* Cor do texto */\n"
"        border: 1px solid rgb(84,84,84);/* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(84,84,84); /* Cor de fundo */\n"
"        color: white; /* Cor do texto */\n"
"        border: 1px solid black; /* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"QFrame{\n"
"    border: 0px solid black;\n"
"    border-radius: 2px;\n"
"}")
        self.frame_botoes_filtro.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_botoes_filtro.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_botoes_filtro)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.botao_aplicar_pacotes = QPushButton(self.frame_botoes_filtro)
        self.botao_aplicar_pacotes.setObjectName(u"botao_aplicar_pacotes")
        self.botao_aplicar_pacotes.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_11.addWidget(self.botao_aplicar_pacotes)

        self.botao_restaurar_filtro_pacotes = QPushButton(self.frame_botoes_filtro)
        self.botao_restaurar_filtro_pacotes.setObjectName(u"botao_restaurar_filtro_pacotes")
        self.botao_restaurar_filtro_pacotes.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_11.addWidget(self.botao_restaurar_filtro_pacotes)


        self.verticalLayout_5.addWidget(self.frame_botoes_filtro)

        self.verticalSpacer_embaixo_filtro = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_embaixo_filtro)


        self.gridLayout_8.addWidget(self.frame_filtro_pacotes, 0, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer, 0, 0, 2, 1)

        self.frame_botoes_pacote = QFrame(self.tab_pacotes)
        self.frame_botoes_pacote.setObjectName(u"frame_botoes_pacote")
        sizePolicy.setHeightForWidth(self.frame_botoes_pacote.sizePolicy().hasHeightForWidth())
        self.frame_botoes_pacote.setSizePolicy(sizePolicy)
        self.frame_botoes_pacote.setStyleSheet(u"QFrame{\n"
"    border: 1px solid black;\n"
"    border-radius: 2px;\n"
"}")
        self.frame_botoes_pacote.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_botoes_pacote.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_botoes_pacote)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.botao_filtro_pacote = QPushButton(self.frame_botoes_pacote)
        self.botao_filtro_pacote.setObjectName(u"botao_filtro_pacote")
        self.botao_filtro_pacote.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_filtro_pacote.setStyleSheet(u"    QPushButton {\n"
"        background-color: rgb(230,230,230); /* Cor de fundo */\n"
"        color: black; /* Cor do texto */\n"
"        border: 1px solid rgb(84,84,84);/* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(84,84,84); /* Cor de fundo */\n"
"        color: white; /* Cor do texto */\n"
"        border: 1px solid black; /* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }")

        self.verticalLayout_4.addWidget(self.botao_filtro_pacote)

        self.botao_alterar_pacote = QPushButton(self.frame_botoes_pacote)
        self.botao_alterar_pacote.setObjectName(u"botao_alterar_pacote")
        self.botao_alterar_pacote.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_alterar_pacote.setStyleSheet(u"    QPushButton {\n"
"        background-color: rgb(230,230,230); /* Cor de fundo */\n"
"        color: black; /* Cor do texto */\n"
"        border: 1px solid rgb(84,84,84);/* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(84,84,84); /* Cor de fundo */\n"
"        color: white; /* Cor do texto */\n"
"        border: 1px solid black; /* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }")

        self.verticalLayout_4.addWidget(self.botao_alterar_pacote)

        self.botao_excluir_pacote = QPushButton(self.frame_botoes_pacote)
        self.botao_excluir_pacote.setObjectName(u"botao_excluir_pacote")
        self.botao_excluir_pacote.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_excluir_pacote.setStyleSheet(u"    QPushButton {\n"
"        background-color: rgb(230,230,230); /* Cor de fundo */\n"
"        color: black; /* Cor do texto */\n"
"        border: 1px solid rgb(84,84,84);/* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(84,84,84); /* Cor de fundo */\n"
"        color: white; /* Cor do texto */\n"
"        border: 1px solid black; /* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }")

        self.verticalLayout_4.addWidget(self.botao_excluir_pacote)

        self.verticalSpacer_botoes = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_botoes)


        self.gridLayout_8.addWidget(self.frame_botoes_pacote, 0, 2, 2, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_2, 0, 4, 2, 1)

        self.tabWidget_listas.addTab(self.tab_pacotes, "")
        self.tab_remessas = QWidget()
        self.tab_remessas.setObjectName(u"tab_remessas")
        self.gridLayout_10 = QGridLayout(self.tab_remessas)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.tableWidget_lista_remessa = QTableWidget(self.tab_remessas)
        if (self.tableWidget_lista_remessa.columnCount() < 3):
            self.tableWidget_lista_remessa.setColumnCount(3)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_lista_remessa.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_lista_remessa.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_lista_remessa.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        self.tableWidget_lista_remessa.setObjectName(u"tableWidget_lista_remessa")
        sizePolicy6.setHeightForWidth(self.tableWidget_lista_remessa.sizePolicy().hasHeightForWidth())
        self.tableWidget_lista_remessa.setSizePolicy(sizePolicy6)
        self.tableWidget_lista_remessa.setStyleSheet(u"QTableWidget {\n"
"    border: 1px solid black;\n"
"    border-radius: 2px;\n"
"}")

        self.gridLayout_10.addWidget(self.tableWidget_lista_remessa, 0, 1, 2, 1)

        self.frame_botoes_remessa = QFrame(self.tab_remessas)
        self.frame_botoes_remessa.setObjectName(u"frame_botoes_remessa")
        sizePolicy.setHeightForWidth(self.frame_botoes_remessa.sizePolicy().hasHeightForWidth())
        self.frame_botoes_remessa.setSizePolicy(sizePolicy)
        self.frame_botoes_remessa.setStyleSheet(u"QFrame{\n"
"    border: 1px solid black;\n"
"    border-radius: 2px;\n"
"}")
        self.frame_botoes_remessa.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_botoes_remessa.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_botoes_remessa)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.botao_filtro_remessa = QPushButton(self.frame_botoes_remessa)
        self.botao_filtro_remessa.setObjectName(u"botao_filtro_remessa")
        self.botao_filtro_remessa.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_filtro_remessa.setStyleSheet(u"    QPushButton {\n"
"        background-color: rgb(230,230,230); /* Cor de fundo */\n"
"        color: black; /* Cor do texto */\n"
"        border: 1px solid rgb(84,84,84);/* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(84,84,84); /* Cor de fundo */\n"
"        color: white; /* Cor do texto */\n"
"        border: 1px solid black; /* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }")

        self.verticalLayout_13.addWidget(self.botao_filtro_remessa)

        self.botao_alterar_remessa = QPushButton(self.frame_botoes_remessa)
        self.botao_alterar_remessa.setObjectName(u"botao_alterar_remessa")
        self.botao_alterar_remessa.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_alterar_remessa.setStyleSheet(u"    QPushButton {\n"
"        background-color: rgb(230,230,230); /* Cor de fundo */\n"
"        color: black; /* Cor do texto */\n"
"        border: 1px solid rgb(84,84,84);/* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(84,84,84); /* Cor de fundo */\n"
"        color: white; /* Cor do texto */\n"
"        border: 1px solid black; /* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }")

        self.verticalLayout_13.addWidget(self.botao_alterar_remessa)

        self.botao_excluir_remessa = QPushButton(self.frame_botoes_remessa)
        self.botao_excluir_remessa.setObjectName(u"botao_excluir_remessa")
        self.botao_excluir_remessa.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_excluir_remessa.setStyleSheet(u"    QPushButton {\n"
"        background-color: rgb(230,230,230); /* Cor de fundo */\n"
"        color: black; /* Cor do texto */\n"
"        border: 1px solid rgb(84,84,84);/* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(84,84,84); /* Cor de fundo */\n"
"        color: white; /* Cor do texto */\n"
"        border: 1px solid black; /* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }")

        self.verticalLayout_13.addWidget(self.botao_excluir_remessa)

        self.verticalSpacer_botoes_remessa = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_botoes_remessa)


        self.gridLayout_10.addWidget(self.frame_botoes_remessa, 0, 2, 2, 1)

        self.frame_filtro_remessa = QFrame(self.tab_remessas)
        self.frame_filtro_remessa.setObjectName(u"frame_filtro_remessa")
        sizePolicy6.setHeightForWidth(self.frame_filtro_remessa.sizePolicy().hasHeightForWidth())
        self.frame_filtro_remessa.setSizePolicy(sizePolicy6)
        self.frame_filtro_remessa.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid black;\n"
"border-radius: 2px;\n"
"}\n"
"QFrame{\n"
"    border: 0px solid black;\n"
"    border-radius: 2px;\n"
"}\n"
"font: 12pt \"HeIvetica\";\n"
"")
        self.frame_filtro_remessa.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_filtro_remessa.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_filtro_remessa)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalSpacer_topo_filtro_remessa = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_topo_filtro_remessa)

        self.label_filtro_remessa = QLabel(self.frame_filtro_remessa)
        self.label_filtro_remessa.setObjectName(u"label_filtro_remessa")
        self.label_filtro_remessa.setFont(font3)
        self.label_filtro_remessa.setStyleSheet(u"font: 700 14pt \"HeIvetica\";\n"
"border: 0px solid black;\n"
"border-radius: 2px;")

        self.verticalLayout_12.addWidget(self.label_filtro_remessa)

        self.linha_filtro_remessa = QFrame(self.frame_filtro_remessa)
        self.linha_filtro_remessa.setObjectName(u"linha_filtro_remessa")
        self.linha_filtro_remessa.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(0, 0, 0);\n"
"    max-height: 1px;\n"
"    min-height: 1px;\n"
"}\n"
"")
        self.linha_filtro_remessa.setFrameShape(QFrame.Shape.HLine)
        self.linha_filtro_remessa.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_12.addWidget(self.linha_filtro_remessa)

        self.comboBox_filtro_remessa = QComboBox(self.frame_filtro_remessa)
        self.comboBox_filtro_remessa.addItem("")
        self.comboBox_filtro_remessa.addItem("")
        self.comboBox_filtro_remessa.addItem("")
        self.comboBox_filtro_remessa.setObjectName(u"comboBox_filtro_remessa")
        sizePolicy7.setHeightForWidth(self.comboBox_filtro_remessa.sizePolicy().hasHeightForWidth())
        self.comboBox_filtro_remessa.setSizePolicy(sizePolicy7)
        self.comboBox_filtro_remessa.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_filtro_remessa.setStyleSheet(u"    QComboBox {\n"
"        background-color: rgb(230,230,230); /* Cor de fundo */\n"
"        color: black; /* Cor do texto */\n"
"        border: 1px solid rgb(84,84,84);/* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"    QComboBox:pressed {\n"
"        background-color: rgb(84,84,84); /* Cor de fundo */\n"
"        color: white; /* Cor do texto */\n"
"        border: 1px solid black; /* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }")

        self.verticalLayout_12.addWidget(self.comboBox_filtro_remessa)

        self.lineEdit_filtro_remessa = QLineEdit(self.frame_filtro_remessa)
        self.lineEdit_filtro_remessa.setObjectName(u"lineEdit_filtro_remessa")
        sizePolicy7.setHeightForWidth(self.lineEdit_filtro_remessa.sizePolicy().hasHeightForWidth())
        self.lineEdit_filtro_remessa.setSizePolicy(sizePolicy7)

        self.verticalLayout_12.addWidget(self.lineEdit_filtro_remessa)

        self.frame_botoes_filtro_remessa = QFrame(self.frame_filtro_remessa)
        self.frame_botoes_filtro_remessa.setObjectName(u"frame_botoes_filtro_remessa")
        sizePolicy8.setHeightForWidth(self.frame_botoes_filtro_remessa.sizePolicy().hasHeightForWidth())
        self.frame_botoes_filtro_remessa.setSizePolicy(sizePolicy8)
        self.frame_botoes_filtro_remessa.setStyleSheet(u"    QPushButton {\n"
"        background-color: rgb(230,230,230); /* Cor de fundo */\n"
"        color: black; /* Cor do texto */\n"
"        border: 1px solid rgb(84,84,84);/* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(84,84,84); /* Cor de fundo */\n"
"        color: white; /* Cor do texto */\n"
"        border: 1px solid black; /* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"QFrame{\n"
"    border: 0px solid black;\n"
"    border-radius: 2px;\n"
"}")
        self.frame_botoes_filtro_remessa.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_botoes_filtro_remessa.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_botoes_filtro_remessa)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.botao_aplicar_remessa = QPushButton(self.frame_botoes_filtro_remessa)
        self.botao_aplicar_remessa.setObjectName(u"botao_aplicar_remessa")
        self.botao_aplicar_remessa.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_13.addWidget(self.botao_aplicar_remessa)

        self.botao_restaurar_filtro_remessa = QPushButton(self.frame_botoes_filtro_remessa)
        self.botao_restaurar_filtro_remessa.setObjectName(u"botao_restaurar_filtro_remessa")
        self.botao_restaurar_filtro_remessa.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_13.addWidget(self.botao_restaurar_filtro_remessa)


        self.verticalLayout_12.addWidget(self.frame_botoes_filtro_remessa)

        self.verticalSpacer_embaixo_filtro_remessa = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_embaixo_filtro_remessa)


        self.gridLayout_10.addWidget(self.frame_filtro_remessa, 0, 3, 1, 1)

        self.frame_alteracoes_remessa = QFrame(self.tab_remessas)
        self.frame_alteracoes_remessa.setObjectName(u"frame_alteracoes_remessa")
        sizePolicy6.setHeightForWidth(self.frame_alteracoes_remessa.sizePolicy().hasHeightForWidth())
        self.frame_alteracoes_remessa.setSizePolicy(sizePolicy6)
        self.frame_alteracoes_remessa.setStyleSheet(u"QLabel{\n"
"border: 1px solid black;\n"
"border-radius: 2px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 1px solid black;\n"
"border-radius: 2px;\n"
"}\n"
"QFrame{\n"
"    border: 0px solid black;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"font: 12pt \"HeIvetica\";")
        self.frame_alteracoes_remessa.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_alteracoes_remessa.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_alteracoes_remessa)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.linha_alterar_remessa = QFrame(self.frame_alteracoes_remessa)
        self.linha_alterar_remessa.setObjectName(u"linha_alterar_remessa")
        self.linha_alterar_remessa.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(0, 0, 0);\n"
"    max-height: 1px;\n"
"    min-height: 1px;\n"
"}\n"
"")
        self.linha_alterar_remessa.setFrameShape(QFrame.Shape.HLine)
        self.linha_alterar_remessa.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_9.addWidget(self.linha_alterar_remessa, 1, 0, 1, 2)

        self.label_alterar_remessa = QLabel(self.frame_alteracoes_remessa)
        self.label_alterar_remessa.setObjectName(u"label_alterar_remessa")
        self.label_alterar_remessa.setStyleSheet(u"font: 700 14pt \"HeIvetica\";\n"
"border: 0px solid black;\n"
"border-radius: 2px;")

        self.gridLayout_9.addWidget(self.label_alterar_remessa, 0, 0, 1, 2)

        self.label_id_pacote_1_alterar = QLabel(self.frame_alteracoes_remessa)
        self.label_id_pacote_1_alterar.setObjectName(u"label_id_pacote_1_alterar")
        sizePolicy2.setHeightForWidth(self.label_id_pacote_1_alterar.sizePolicy().hasHeightForWidth())
        self.label_id_pacote_1_alterar.setSizePolicy(sizePolicy2)
        self.label_id_pacote_1_alterar.setStyleSheet(u"font: 700 12pt \"HeIvetica\";")

        self.gridLayout_9.addWidget(self.label_id_pacote_1_alterar, 4, 0, 1, 1)

        self.frame_botoes_alterar_remessa = QFrame(self.frame_alteracoes_remessa)
        self.frame_botoes_alterar_remessa.setObjectName(u"frame_botoes_alterar_remessa")
        sizePolicy.setHeightForWidth(self.frame_botoes_alterar_remessa.sizePolicy().hasHeightForWidth())
        self.frame_botoes_alterar_remessa.setSizePolicy(sizePolicy)
        self.frame_botoes_alterar_remessa.setStyleSheet(u"    QPushButton {\n"
"        background-color: rgb(230,230,230); /* Cor de fundo */\n"
"        color: black; /* Cor do texto */\n"
"        border: 1px solid rgb(84,84,84);/* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(84,84,84); /* Cor de fundo */\n"
"        color: white; /* Cor do texto */\n"
"        border: 1px solid black; /* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"QFrame{\n"
"    border: 0px solid black;\n"
"    border-radius: 2px;\n"
"}")
        self.frame_botoes_alterar_remessa.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_botoes_alterar_remessa.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_botoes_alterar_remessa)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.botao_salvar_alterar_remessa = QPushButton(self.frame_botoes_alterar_remessa)
        self.botao_salvar_alterar_remessa.setObjectName(u"botao_salvar_alterar_remessa")
        self.botao_salvar_alterar_remessa.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_14.addWidget(self.botao_salvar_alterar_remessa)

        self.botao_cancelar_alterar_remessa = QPushButton(self.frame_botoes_alterar_remessa)
        self.botao_cancelar_alterar_remessa.setObjectName(u"botao_cancelar_alterar_remessa")
        self.botao_cancelar_alterar_remessa.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_14.addWidget(self.botao_cancelar_alterar_remessa)


        self.gridLayout_9.addWidget(self.frame_botoes_alterar_remessa, 6, 0, 1, 2)

        self.label_id_pacote_2_alterar = QLabel(self.frame_alteracoes_remessa)
        self.label_id_pacote_2_alterar.setObjectName(u"label_id_pacote_2_alterar")
        sizePolicy2.setHeightForWidth(self.label_id_pacote_2_alterar.sizePolicy().hasHeightForWidth())
        self.label_id_pacote_2_alterar.setSizePolicy(sizePolicy2)
        self.label_id_pacote_2_alterar.setStyleSheet(u"font: 700 12pt \"HeIvetica\";")

        self.gridLayout_9.addWidget(self.label_id_pacote_2_alterar, 5, 0, 1, 1)

        self.lineEdit_id_pacote_1_alterar = QLineEdit(self.frame_alteracoes_remessa)
        self.lineEdit_id_pacote_1_alterar.setObjectName(u"lineEdit_id_pacote_1_alterar")
        sizePolicy7.setHeightForWidth(self.lineEdit_id_pacote_1_alterar.sizePolicy().hasHeightForWidth())
        self.lineEdit_id_pacote_1_alterar.setSizePolicy(sizePolicy7)
        self.lineEdit_id_pacote_1_alterar.setStyleSheet(u"")

        self.gridLayout_9.addWidget(self.lineEdit_id_pacote_1_alterar, 4, 1, 1, 1)

        self.lineEdit_id_pacote_2_alterar = QLineEdit(self.frame_alteracoes_remessa)
        self.lineEdit_id_pacote_2_alterar.setObjectName(u"lineEdit_id_pacote_2_alterar")
        sizePolicy7.setHeightForWidth(self.lineEdit_id_pacote_2_alterar.sizePolicy().hasHeightForWidth())
        self.lineEdit_id_pacote_2_alterar.setSizePolicy(sizePolicy7)
        self.lineEdit_id_pacote_2_alterar.setStyleSheet(u"")

        self.gridLayout_9.addWidget(self.lineEdit_id_pacote_2_alterar, 5, 1, 1, 1)

        self.label_id_remessa_alterar = QLabel(self.frame_alteracoes_remessa)
        self.label_id_remessa_alterar.setObjectName(u"label_id_remessa_alterar")
        sizePolicy2.setHeightForWidth(self.label_id_remessa_alterar.sizePolicy().hasHeightForWidth())
        self.label_id_remessa_alterar.setSizePolicy(sizePolicy2)
        self.label_id_remessa_alterar.setFont(font1)
        self.label_id_remessa_alterar.setStyleSheet(u"font: 700 12pt \"HeIvetica\";\n"
"\n"
"")

        self.gridLayout_9.addWidget(self.label_id_remessa_alterar, 3, 0, 1, 1)

        self.label_id_remessa_alterar_num = QLabel(self.frame_alteracoes_remessa)
        self.label_id_remessa_alterar_num.setObjectName(u"label_id_remessa_alterar_num")
        self.label_id_remessa_alterar_num.setStyleSheet(u"QLabel{\n"
"border: 1px solid black;\n"
"border-radius: 2px;\n"
"	border-top-color: rgb(255, 255, 255);\n"
"	border-right-color: rgb(255, 255, 255);\n"
"	border-bottom-color: rgb(0, 0, 0);\n"
"	border-left-color: rgb(255, 255, 255);\n"
"}\n"
"font: 12pt \"HeIvetica\";")

        self.gridLayout_9.addWidget(self.label_id_remessa_alterar_num, 3, 1, 1, 1)


        self.gridLayout_10.addWidget(self.frame_alteracoes_remessa, 1, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 424, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_4, 0, 4, 2, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 424, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_3, 0, 0, 2, 1)

        self.tabWidget_listas.addTab(self.tab_remessas, "")
        self.tab_moradores = QWidget()
        self.tab_moradores.setObjectName(u"tab_moradores")
        self.gridLayout_12 = QGridLayout(self.tab_moradores)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.tableWidget_lista_moradores = QTableWidget(self.tab_moradores)
        if (self.tableWidget_lista_moradores.columnCount() < 4):
            self.tableWidget_lista_moradores.setColumnCount(4)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_lista_moradores.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_lista_moradores.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_lista_moradores.setHorizontalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_lista_moradores.setHorizontalHeaderItem(3, __qtablewidgetitem22)
        self.tableWidget_lista_moradores.setObjectName(u"tableWidget_lista_moradores")
        sizePolicy6.setHeightForWidth(self.tableWidget_lista_moradores.sizePolicy().hasHeightForWidth())
        self.tableWidget_lista_moradores.setSizePolicy(sizePolicy6)
        self.tableWidget_lista_moradores.setStyleSheet(u"QTableWidget {\n"
"    border: 1px solid black;\n"
"    border-radius: 2px;\n"
"}")

        self.gridLayout_12.addWidget(self.tableWidget_lista_moradores, 0, 1, 2, 1)

        self.frame_botoes_morador = QFrame(self.tab_moradores)
        self.frame_botoes_morador.setObjectName(u"frame_botoes_morador")
        sizePolicy.setHeightForWidth(self.frame_botoes_morador.sizePolicy().hasHeightForWidth())
        self.frame_botoes_morador.setSizePolicy(sizePolicy)
        self.frame_botoes_morador.setStyleSheet(u"QFrame{\n"
"    border: 1px solid black;\n"
"    border-radius: 2px;\n"
"}")
        self.frame_botoes_morador.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_botoes_morador.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_botoes_morador)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.botao_filtro_morador = QPushButton(self.frame_botoes_morador)
        self.botao_filtro_morador.setObjectName(u"botao_filtro_morador")
        self.botao_filtro_morador.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_filtro_morador.setStyleSheet(u"    QPushButton {\n"
"        background-color: rgb(230,230,230); /* Cor de fundo */\n"
"        color: black; /* Cor do texto */\n"
"        border: 1px solid rgb(84,84,84);/* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(84,84,84); /* Cor de fundo */\n"
"        color: white; /* Cor do texto */\n"
"        border: 1px solid black; /* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }")

        self.verticalLayout_15.addWidget(self.botao_filtro_morador)

        self.botao_alterar_morador = QPushButton(self.frame_botoes_morador)
        self.botao_alterar_morador.setObjectName(u"botao_alterar_morador")
        self.botao_alterar_morador.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_alterar_morador.setStyleSheet(u"    QPushButton {\n"
"        background-color: rgb(230,230,230); /* Cor de fundo */\n"
"        color: black; /* Cor do texto */\n"
"        border: 1px solid rgb(84,84,84);/* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(84,84,84); /* Cor de fundo */\n"
"        color: white; /* Cor do texto */\n"
"        border: 1px solid black; /* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }")

        self.verticalLayout_15.addWidget(self.botao_alterar_morador)

        self.botao_excluir_morador = QPushButton(self.frame_botoes_morador)
        self.botao_excluir_morador.setObjectName(u"botao_excluir_morador")
        self.botao_excluir_morador.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_excluir_morador.setStyleSheet(u"    QPushButton {\n"
"        background-color: rgb(230,230,230); /* Cor de fundo */\n"
"        color: black; /* Cor do texto */\n"
"        border: 1px solid rgb(84,84,84);/* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(84,84,84); /* Cor de fundo */\n"
"        color: white; /* Cor do texto */\n"
"        border: 1px solid black; /* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }")

        self.verticalLayout_15.addWidget(self.botao_excluir_morador)

        self.verticalSpacer_botoes_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_botoes_2)


        self.gridLayout_12.addWidget(self.frame_botoes_morador, 0, 2, 2, 1)

        self.frame_filtro_morador = QFrame(self.tab_moradores)
        self.frame_filtro_morador.setObjectName(u"frame_filtro_morador")
        sizePolicy6.setHeightForWidth(self.frame_filtro_morador.sizePolicy().hasHeightForWidth())
        self.frame_filtro_morador.setSizePolicy(sizePolicy6)
        self.frame_filtro_morador.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid black;\n"
"border-radius: 2px;\n"
"}\n"
"QFrame{\n"
"    border: 0px solid black;\n"
"    border-radius: 2px;\n"
"}\n"
"font: 12pt \"HeIvetica\";\n"
"")
        self.frame_filtro_morador.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_filtro_morador.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_filtro_morador)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalSpacer_topo_filtro_morador = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_topo_filtro_morador)

        self.label_filtro_morador = QLabel(self.frame_filtro_morador)
        self.label_filtro_morador.setObjectName(u"label_filtro_morador")
        self.label_filtro_morador.setFont(font3)
        self.label_filtro_morador.setStyleSheet(u"font: 700 14pt \"HeIvetica\";\n"
"border: 0px solid black;\n"
"border-radius: 2px;")

        self.verticalLayout_14.addWidget(self.label_filtro_morador)

        self.linha_filtro_morador = QFrame(self.frame_filtro_morador)
        self.linha_filtro_morador.setObjectName(u"linha_filtro_morador")
        self.linha_filtro_morador.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(0, 0, 0);\n"
"    max-height: 1px;\n"
"    min-height: 1px;\n"
"}\n"
"")
        self.linha_filtro_morador.setFrameShape(QFrame.Shape.HLine)
        self.linha_filtro_morador.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_14.addWidget(self.linha_filtro_morador)

        self.comboBox_filtro_morador = QComboBox(self.frame_filtro_morador)
        self.comboBox_filtro_morador.addItem("")
        self.comboBox_filtro_morador.addItem("")
        self.comboBox_filtro_morador.addItem("")
        self.comboBox_filtro_morador.addItem("")
        self.comboBox_filtro_morador.setObjectName(u"comboBox_filtro_morador")
        sizePolicy7.setHeightForWidth(self.comboBox_filtro_morador.sizePolicy().hasHeightForWidth())
        self.comboBox_filtro_morador.setSizePolicy(sizePolicy7)
        self.comboBox_filtro_morador.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_filtro_morador.setStyleSheet(u"    QComboBox {\n"
"        background-color: rgb(230,230,230); /* Cor de fundo */\n"
"        color: black; /* Cor do texto */\n"
"        border: 1px solid rgb(84,84,84);/* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"    QComboBox:pressed {\n"
"        background-color: rgb(84,84,84); /* Cor de fundo */\n"
"        color: white; /* Cor do texto */\n"
"        border: 1px solid black; /* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }")

        self.verticalLayout_14.addWidget(self.comboBox_filtro_morador)

        self.lineEdit_filtro_morador = QLineEdit(self.frame_filtro_morador)
        self.lineEdit_filtro_morador.setObjectName(u"lineEdit_filtro_morador")
        sizePolicy7.setHeightForWidth(self.lineEdit_filtro_morador.sizePolicy().hasHeightForWidth())
        self.lineEdit_filtro_morador.setSizePolicy(sizePolicy7)

        self.verticalLayout_14.addWidget(self.lineEdit_filtro_morador)

        self.frame_botoes_filtro_morador = QFrame(self.frame_filtro_morador)
        self.frame_botoes_filtro_morador.setObjectName(u"frame_botoes_filtro_morador")
        sizePolicy8.setHeightForWidth(self.frame_botoes_filtro_morador.sizePolicy().hasHeightForWidth())
        self.frame_botoes_filtro_morador.setSizePolicy(sizePolicy8)
        self.frame_botoes_filtro_morador.setStyleSheet(u"    QPushButton {\n"
"        background-color: rgb(230,230,230); /* Cor de fundo */\n"
"        color: black; /* Cor do texto */\n"
"        border: 1px solid rgb(84,84,84);/* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(84,84,84); /* Cor de fundo */\n"
"        color: white; /* Cor do texto */\n"
"        border: 1px solid black; /* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"QFrame{\n"
"    border: 0px solid black;\n"
"    border-radius: 2px;\n"
"}")
        self.frame_botoes_filtro_morador.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_botoes_filtro_morador.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_botoes_filtro_morador)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.botao_aplicar_morador = QPushButton(self.frame_botoes_filtro_morador)
        self.botao_aplicar_morador.setObjectName(u"botao_aplicar_morador")
        self.botao_aplicar_morador.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_15.addWidget(self.botao_aplicar_morador)

        self.botao_restaurar_filtro_morador = QPushButton(self.frame_botoes_filtro_morador)
        self.botao_restaurar_filtro_morador.setObjectName(u"botao_restaurar_filtro_morador")
        self.botao_restaurar_filtro_morador.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_15.addWidget(self.botao_restaurar_filtro_morador)


        self.verticalLayout_14.addWidget(self.frame_botoes_filtro_morador)

        self.verticalSpacer_embaixo_filtro_morador = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_embaixo_filtro_morador)


        self.gridLayout_12.addWidget(self.frame_filtro_morador, 0, 3, 1, 1)

        self.frame_alteracoes_morador = QFrame(self.tab_moradores)
        self.frame_alteracoes_morador.setObjectName(u"frame_alteracoes_morador")
        sizePolicy6.setHeightForWidth(self.frame_alteracoes_morador.sizePolicy().hasHeightForWidth())
        self.frame_alteracoes_morador.setSizePolicy(sizePolicy6)
        self.frame_alteracoes_morador.setStyleSheet(u"QLabel{\n"
"border: 1px solid black;\n"
"border-radius: 2px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 1px solid black;\n"
"border-radius: 2px;\n"
"}\n"
"QFrame{\n"
"    border: 0px solid black;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"font: 12pt \"HeIvetica\";")
        self.frame_alteracoes_morador.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_alteracoes_morador.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_alteracoes_morador)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_id_morador_num = QLabel(self.frame_alteracoes_morador)
        self.label_id_morador_num.setObjectName(u"label_id_morador_num")
        self.label_id_morador_num.setStyleSheet(u"QLabel{\n"
"border: 1px solid black;\n"
"border-radius: 2px;\n"
"	border-top-color: rgb(255, 255, 255);\n"
"	border-right-color: rgb(255, 255, 255);\n"
"	border-bottom-color: rgb(0, 0, 0);\n"
"	border-left-color: rgb(255, 255, 255);\n"
"}\n"
"font: 12pt \"HeIvetica\";")

        self.gridLayout_11.addWidget(self.label_id_morador_num, 2, 1, 1, 1)

        self.label_telefone_alterar = QLabel(self.frame_alteracoes_morador)
        self.label_telefone_alterar.setObjectName(u"label_telefone_alterar")
        sizePolicy2.setHeightForWidth(self.label_telefone_alterar.sizePolicy().hasHeightForWidth())
        self.label_telefone_alterar.setSizePolicy(sizePolicy2)
        self.label_telefone_alterar.setStyleSheet(u"font: 700 12pt \"HeIvetica\";")

        self.gridLayout_11.addWidget(self.label_telefone_alterar, 5, 0, 1, 1)

        self.lineEdit_nome_morador_alterar = QLineEdit(self.frame_alteracoes_morador)
        self.lineEdit_nome_morador_alterar.setObjectName(u"lineEdit_nome_morador_alterar")
        sizePolicy7.setHeightForWidth(self.lineEdit_nome_morador_alterar.sizePolicy().hasHeightForWidth())
        self.lineEdit_nome_morador_alterar.setSizePolicy(sizePolicy7)
        self.lineEdit_nome_morador_alterar.setStyleSheet(u"")

        self.gridLayout_11.addWidget(self.lineEdit_nome_morador_alterar, 3, 1, 1, 1)

        self.label_id_morador_alterar_2 = QLabel(self.frame_alteracoes_morador)
        self.label_id_morador_alterar_2.setObjectName(u"label_id_morador_alterar_2")
        self.label_id_morador_alterar_2.setStyleSheet(u"font: 700 12pt \"HeIvetica\";")

        self.gridLayout_11.addWidget(self.label_id_morador_alterar_2, 2, 0, 1, 1)

        self.lineEdit_endereco_alterar = QLineEdit(self.frame_alteracoes_morador)
        self.lineEdit_endereco_alterar.setObjectName(u"lineEdit_endereco_alterar")
        sizePolicy7.setHeightForWidth(self.lineEdit_endereco_alterar.sizePolicy().hasHeightForWidth())
        self.lineEdit_endereco_alterar.setSizePolicy(sizePolicy7)
        self.lineEdit_endereco_alterar.setStyleSheet(u"")

        self.gridLayout_11.addWidget(self.lineEdit_endereco_alterar, 4, 1, 1, 1)

        self.label_alterar_morador = QLabel(self.frame_alteracoes_morador)
        self.label_alterar_morador.setObjectName(u"label_alterar_morador")
        self.label_alterar_morador.setStyleSheet(u"font: 700 14pt \"HeIvetica\";\n"
"border: 0px solid black;\n"
"border-radius: 2px;")

        self.gridLayout_11.addWidget(self.label_alterar_morador, 0, 0, 1, 2)

        self.label_nome_morador_alterar = QLabel(self.frame_alteracoes_morador)
        self.label_nome_morador_alterar.setObjectName(u"label_nome_morador_alterar")
        sizePolicy2.setHeightForWidth(self.label_nome_morador_alterar.sizePolicy().hasHeightForWidth())
        self.label_nome_morador_alterar.setSizePolicy(sizePolicy2)
        self.label_nome_morador_alterar.setFont(font1)
        self.label_nome_morador_alterar.setStyleSheet(u"font: 700 12pt \"HeIvetica\";\n"
"\n"
"")

        self.gridLayout_11.addWidget(self.label_nome_morador_alterar, 3, 0, 1, 1)

        self.lineEdit_telefone_alterar = QLineEdit(self.frame_alteracoes_morador)
        self.lineEdit_telefone_alterar.setObjectName(u"lineEdit_telefone_alterar")
        sizePolicy7.setHeightForWidth(self.lineEdit_telefone_alterar.sizePolicy().hasHeightForWidth())
        self.lineEdit_telefone_alterar.setSizePolicy(sizePolicy7)
        self.lineEdit_telefone_alterar.setStyleSheet(u"")

        self.gridLayout_11.addWidget(self.lineEdit_telefone_alterar, 5, 1, 1, 1)

        self.label_endereco_alterar = QLabel(self.frame_alteracoes_morador)
        self.label_endereco_alterar.setObjectName(u"label_endereco_alterar")
        sizePolicy2.setHeightForWidth(self.label_endereco_alterar.sizePolicy().hasHeightForWidth())
        self.label_endereco_alterar.setSizePolicy(sizePolicy2)
        self.label_endereco_alterar.setStyleSheet(u"font: 700 12pt \"HeIvetica\";")

        self.gridLayout_11.addWidget(self.label_endereco_alterar, 4, 0, 1, 1)

        self.frame_botoes_alterar_morador = QFrame(self.frame_alteracoes_morador)
        self.frame_botoes_alterar_morador.setObjectName(u"frame_botoes_alterar_morador")
        sizePolicy.setHeightForWidth(self.frame_botoes_alterar_morador.sizePolicy().hasHeightForWidth())
        self.frame_botoes_alterar_morador.setSizePolicy(sizePolicy)
        self.frame_botoes_alterar_morador.setStyleSheet(u"    QPushButton {\n"
"        background-color: rgb(230,230,230); /* Cor de fundo */\n"
"        color: black; /* Cor do texto */\n"
"        border: 1px solid rgb(84,84,84);/* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(84,84,84); /* Cor de fundo */\n"
"        color: white; /* Cor do texto */\n"
"        border: 1px solid black; /* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"QFrame{\n"
"    border: 0px solid black;\n"
"    border-radius: 2px;\n"
"}")
        self.frame_botoes_alterar_morador.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_botoes_alterar_morador.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_botoes_alterar_morador)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.botao_salvar_alterar_morador = QPushButton(self.frame_botoes_alterar_morador)
        self.botao_salvar_alterar_morador.setObjectName(u"botao_salvar_alterar_morador")
        self.botao_salvar_alterar_morador.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_16.addWidget(self.botao_salvar_alterar_morador)

        self.botao_cancelar_alterar_morador = QPushButton(self.frame_botoes_alterar_morador)
        self.botao_cancelar_alterar_morador.setObjectName(u"botao_cancelar_alterar_morador")
        self.botao_cancelar_alterar_morador.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_16.addWidget(self.botao_cancelar_alterar_morador)


        self.gridLayout_11.addWidget(self.frame_botoes_alterar_morador, 6, 0, 1, 2)

        self.linha_alterar_morador = QFrame(self.frame_alteracoes_morador)
        self.linha_alterar_morador.setObjectName(u"linha_alterar_morador")
        self.linha_alterar_morador.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(0, 0, 0);\n"
"    max-height: 1px;\n"
"    min-height: 1px;\n"
"}\n"
"")
        self.linha_alterar_morador.setFrameShape(QFrame.Shape.HLine)
        self.linha_alterar_morador.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_11.addWidget(self.linha_alterar_morador, 1, 0, 1, 2)


        self.gridLayout_12.addWidget(self.frame_alteracoes_morador, 1, 3, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_6, 0, 0, 2, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_5, 0, 4, 2, 1)

        self.tabWidget_listas.addTab(self.tab_moradores, "")
        self.tab_administradores = QWidget()
        self.tab_administradores.setObjectName(u"tab_administradores")
        self.gridLayout_14 = QGridLayout(self.tab_administradores)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.tableWidget_lista_admin = QTableWidget(self.tab_administradores)
        if (self.tableWidget_lista_admin.columnCount() < 3):
            self.tableWidget_lista_admin.setColumnCount(3)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_lista_admin.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_lista_admin.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_lista_admin.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        self.tableWidget_lista_admin.setObjectName(u"tableWidget_lista_admin")
        sizePolicy6.setHeightForWidth(self.tableWidget_lista_admin.sizePolicy().hasHeightForWidth())
        self.tableWidget_lista_admin.setSizePolicy(sizePolicy6)
        self.tableWidget_lista_admin.setStyleSheet(u"QTableWidget {\n"
"    border: 1px solid black;\n"
"    border-radius: 2px;\n"
"}")

        self.gridLayout_14.addWidget(self.tableWidget_lista_admin, 0, 1, 2, 1)

        self.frame_botoes_admin = QFrame(self.tab_administradores)
        self.frame_botoes_admin.setObjectName(u"frame_botoes_admin")
        sizePolicy.setHeightForWidth(self.frame_botoes_admin.sizePolicy().hasHeightForWidth())
        self.frame_botoes_admin.setSizePolicy(sizePolicy)
        self.frame_botoes_admin.setStyleSheet(u"QFrame{\n"
"    border: 1px solid black;\n"
"    border-radius: 2px;\n"
"}")
        self.frame_botoes_admin.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_botoes_admin.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_botoes_admin)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.botao_filtro_admin = QPushButton(self.frame_botoes_admin)
        self.botao_filtro_admin.setObjectName(u"botao_filtro_admin")
        self.botao_filtro_admin.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_filtro_admin.setStyleSheet(u"    QPushButton {\n"
"        background-color: rgb(230,230,230); /* Cor de fundo */\n"
"        color: black; /* Cor do texto */\n"
"        border: 1px solid rgb(84,84,84);/* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(84,84,84); /* Cor de fundo */\n"
"        color: white; /* Cor do texto */\n"
"        border: 1px solid black; /* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }")

        self.verticalLayout_17.addWidget(self.botao_filtro_admin)

        self.botao_alterar_admin = QPushButton(self.frame_botoes_admin)
        self.botao_alterar_admin.setObjectName(u"botao_alterar_admin")
        self.botao_alterar_admin.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_alterar_admin.setStyleSheet(u"    QPushButton {\n"
"        background-color: rgb(230,230,230); /* Cor de fundo */\n"
"        color: black; /* Cor do texto */\n"
"        border: 1px solid rgb(84,84,84);/* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(84,84,84); /* Cor de fundo */\n"
"        color: white; /* Cor do texto */\n"
"        border: 1px solid black; /* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }")

        self.verticalLayout_17.addWidget(self.botao_alterar_admin)

        self.botao_excluir_admin = QPushButton(self.frame_botoes_admin)
        self.botao_excluir_admin.setObjectName(u"botao_excluir_admin")
        self.botao_excluir_admin.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_excluir_admin.setStyleSheet(u"    QPushButton {\n"
"        background-color: rgb(230,230,230); /* Cor de fundo */\n"
"        color: black; /* Cor do texto */\n"
"        border: 1px solid rgb(84,84,84);/* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(84,84,84); /* Cor de fundo */\n"
"        color: white; /* Cor do texto */\n"
"        border: 1px solid black; /* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }")

        self.verticalLayout_17.addWidget(self.botao_excluir_admin)

        self.verticalSpacer_botoes_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_botoes_3)


        self.gridLayout_14.addWidget(self.frame_botoes_admin, 0, 2, 2, 1)

        self.frame_filtro_admin = QFrame(self.tab_administradores)
        self.frame_filtro_admin.setObjectName(u"frame_filtro_admin")
        sizePolicy6.setHeightForWidth(self.frame_filtro_admin.sizePolicy().hasHeightForWidth())
        self.frame_filtro_admin.setSizePolicy(sizePolicy6)
        self.frame_filtro_admin.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid black;\n"
"border-radius: 2px;\n"
"}\n"
"QFrame{\n"
"    border: 0px solid black;\n"
"    border-radius: 2px;\n"
"}\n"
"font: 12pt \"HeIvetica\";\n"
"")
        self.frame_filtro_admin.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_filtro_admin.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_filtro_admin)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalSpacer_topo_filtro_admin = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_topo_filtro_admin)

        self.label_filtro_admin = QLabel(self.frame_filtro_admin)
        self.label_filtro_admin.setObjectName(u"label_filtro_admin")
        self.label_filtro_admin.setFont(font3)
        self.label_filtro_admin.setStyleSheet(u"font: 700 14pt \"HeIvetica\";\n"
"border: 0px solid black;\n"
"border-radius: 2px;")

        self.verticalLayout_16.addWidget(self.label_filtro_admin)

        self.linha_filtro_admin = QFrame(self.frame_filtro_admin)
        self.linha_filtro_admin.setObjectName(u"linha_filtro_admin")
        self.linha_filtro_admin.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(0, 0, 0);\n"
"    max-height: 1px;\n"
"    min-height: 1px;\n"
"}\n"
"")
        self.linha_filtro_admin.setFrameShape(QFrame.Shape.HLine)
        self.linha_filtro_admin.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_16.addWidget(self.linha_filtro_admin)

        self.comboBox_filtro_admin = QComboBox(self.frame_filtro_admin)
        self.comboBox_filtro_admin.addItem("")
        self.comboBox_filtro_admin.addItem("")
        self.comboBox_filtro_admin.addItem("")
        self.comboBox_filtro_admin.setObjectName(u"comboBox_filtro_admin")
        sizePolicy7.setHeightForWidth(self.comboBox_filtro_admin.sizePolicy().hasHeightForWidth())
        self.comboBox_filtro_admin.setSizePolicy(sizePolicy7)
        self.comboBox_filtro_admin.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_filtro_admin.setStyleSheet(u"    QComboBox {\n"
"        background-color: rgb(230,230,230); /* Cor de fundo */\n"
"        color: black; /* Cor do texto */\n"
"        border: 1px solid rgb(84,84,84);/* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"    QComboBox:pressed {\n"
"        background-color: rgb(84,84,84); /* Cor de fundo */\n"
"        color: white; /* Cor do texto */\n"
"        border: 1px solid black; /* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }")

        self.verticalLayout_16.addWidget(self.comboBox_filtro_admin)

        self.lineEdit_filtro_admin = QLineEdit(self.frame_filtro_admin)
        self.lineEdit_filtro_admin.setObjectName(u"lineEdit_filtro_admin")
        sizePolicy7.setHeightForWidth(self.lineEdit_filtro_admin.sizePolicy().hasHeightForWidth())
        self.lineEdit_filtro_admin.setSizePolicy(sizePolicy7)

        self.verticalLayout_16.addWidget(self.lineEdit_filtro_admin)

        self.frame_botoes_filtro_admin = QFrame(self.frame_filtro_admin)
        self.frame_botoes_filtro_admin.setObjectName(u"frame_botoes_filtro_admin")
        sizePolicy8.setHeightForWidth(self.frame_botoes_filtro_admin.sizePolicy().hasHeightForWidth())
        self.frame_botoes_filtro_admin.setSizePolicy(sizePolicy8)
        self.frame_botoes_filtro_admin.setStyleSheet(u"    QPushButton {\n"
"        background-color: rgb(230,230,230); /* Cor de fundo */\n"
"        color: black; /* Cor do texto */\n"
"        border: 1px solid rgb(84,84,84);/* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(84,84,84); /* Cor de fundo */\n"
"        color: white; /* Cor do texto */\n"
"        border: 1px solid black; /* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"QFrame{\n"
"    border: 0px solid black;\n"
"    border-radius: 2px;\n"
"}")
        self.frame_botoes_filtro_admin.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_botoes_filtro_admin.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_botoes_filtro_admin)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.botao_aplicar_admin = QPushButton(self.frame_botoes_filtro_admin)
        self.botao_aplicar_admin.setObjectName(u"botao_aplicar_admin")
        self.botao_aplicar_admin.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_17.addWidget(self.botao_aplicar_admin)

        self.botao_restaurar_filtro_admin = QPushButton(self.frame_botoes_filtro_admin)
        self.botao_restaurar_filtro_admin.setObjectName(u"botao_restaurar_filtro_admin")
        self.botao_restaurar_filtro_admin.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_17.addWidget(self.botao_restaurar_filtro_admin)


        self.verticalLayout_16.addWidget(self.frame_botoes_filtro_admin)

        self.verticalSpacer_embaixo_filtro_admin = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_embaixo_filtro_admin)


        self.gridLayout_14.addWidget(self.frame_filtro_admin, 0, 3, 1, 1)

        self.frame_alteracoes_admin = QFrame(self.tab_administradores)
        self.frame_alteracoes_admin.setObjectName(u"frame_alteracoes_admin")
        sizePolicy6.setHeightForWidth(self.frame_alteracoes_admin.sizePolicy().hasHeightForWidth())
        self.frame_alteracoes_admin.setSizePolicy(sizePolicy6)
        self.frame_alteracoes_admin.setStyleSheet(u"QLabel{\n"
"border: 1px solid black;\n"
"border-radius: 2px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 1px solid black;\n"
"border-radius: 2px;\n"
"}\n"
"QFrame{\n"
"    border: 0px solid black;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"font: 12pt \"HeIvetica\";")
        self.frame_alteracoes_admin.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_alteracoes_admin.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_alteracoes_admin)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_id_admin_num = QLabel(self.frame_alteracoes_admin)
        self.label_id_admin_num.setObjectName(u"label_id_admin_num")
        self.label_id_admin_num.setStyleSheet(u"QLabel{\n"
"border: 1px solid black;\n"
"border-radius: 2px;\n"
"	border-top-color: rgb(255, 255, 255);\n"
"	border-right-color: rgb(255, 255, 255);\n"
"	border-bottom-color: rgb(0, 0, 0);\n"
"	border-left-color: rgb(255, 255, 255);\n"
"}\n"
"font: 12pt \"HeIvetica\";")

        self.gridLayout_13.addWidget(self.label_id_admin_num, 2, 1, 1, 1)

        self.lineEdit_nome_admin_alterar = QLineEdit(self.frame_alteracoes_admin)
        self.lineEdit_nome_admin_alterar.setObjectName(u"lineEdit_nome_admin_alterar")
        sizePolicy7.setHeightForWidth(self.lineEdit_nome_admin_alterar.sizePolicy().hasHeightForWidth())
        self.lineEdit_nome_admin_alterar.setSizePolicy(sizePolicy7)
        self.lineEdit_nome_admin_alterar.setStyleSheet(u"")

        self.gridLayout_13.addWidget(self.lineEdit_nome_admin_alterar, 3, 1, 1, 1)

        self.label_email_alterar = QLabel(self.frame_alteracoes_admin)
        self.label_email_alterar.setObjectName(u"label_email_alterar")
        sizePolicy2.setHeightForWidth(self.label_email_alterar.sizePolicy().hasHeightForWidth())
        self.label_email_alterar.setSizePolicy(sizePolicy2)
        self.label_email_alterar.setStyleSheet(u"font: 700 12pt \"HeIvetica\";")

        self.gridLayout_13.addWidget(self.label_email_alterar, 4, 0, 1, 1)

        self.lineEdit_email_alterar = QLineEdit(self.frame_alteracoes_admin)
        self.lineEdit_email_alterar.setObjectName(u"lineEdit_email_alterar")
        sizePolicy7.setHeightForWidth(self.lineEdit_email_alterar.sizePolicy().hasHeightForWidth())
        self.lineEdit_email_alterar.setSizePolicy(sizePolicy7)
        self.lineEdit_email_alterar.setStyleSheet(u"")

        self.gridLayout_13.addWidget(self.lineEdit_email_alterar, 4, 1, 1, 1)

        self.label_nome_admin_alterar = QLabel(self.frame_alteracoes_admin)
        self.label_nome_admin_alterar.setObjectName(u"label_nome_admin_alterar")
        sizePolicy2.setHeightForWidth(self.label_nome_admin_alterar.sizePolicy().hasHeightForWidth())
        self.label_nome_admin_alterar.setSizePolicy(sizePolicy2)
        self.label_nome_admin_alterar.setFont(font1)
        self.label_nome_admin_alterar.setStyleSheet(u"font: 700 12pt \"HeIvetica\";\n"
"\n"
"")

        self.gridLayout_13.addWidget(self.label_nome_admin_alterar, 3, 0, 1, 1)

        self.label_alterar_admin = QLabel(self.frame_alteracoes_admin)
        self.label_alterar_admin.setObjectName(u"label_alterar_admin")
        self.label_alterar_admin.setStyleSheet(u"font: 700 14pt \"HeIvetica\";\n"
"border: 0px solid black;\n"
"border-radius: 2px;")

        self.gridLayout_13.addWidget(self.label_alterar_admin, 0, 0, 1, 2)

        self.frame_botoes_alterar_admin = QFrame(self.frame_alteracoes_admin)
        self.frame_botoes_alterar_admin.setObjectName(u"frame_botoes_alterar_admin")
        sizePolicy.setHeightForWidth(self.frame_botoes_alterar_admin.sizePolicy().hasHeightForWidth())
        self.frame_botoes_alterar_admin.setSizePolicy(sizePolicy)
        self.frame_botoes_alterar_admin.setStyleSheet(u"    QPushButton {\n"
"        background-color: rgb(230,230,230); /* Cor de fundo */\n"
"        color: black; /* Cor do texto */\n"
"        border: 1px solid rgb(84,84,84);/* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(84,84,84); /* Cor de fundo */\n"
"        color: white; /* Cor do texto */\n"
"        border: 1px solid black; /* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"QFrame{\n"
"    border: 0px solid black;\n"
"    border-radius: 2px;\n"
"}")
        self.frame_botoes_alterar_admin.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_botoes_alterar_admin.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_botoes_alterar_admin)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.botao_salvar_alterar_admin = QPushButton(self.frame_botoes_alterar_admin)
        self.botao_salvar_alterar_admin.setObjectName(u"botao_salvar_alterar_admin")
        self.botao_salvar_alterar_admin.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_18.addWidget(self.botao_salvar_alterar_admin)

        self.botao_cancelar_alterar_admin = QPushButton(self.frame_botoes_alterar_admin)
        self.botao_cancelar_alterar_admin.setObjectName(u"botao_cancelar_alterar_admin")
        self.botao_cancelar_alterar_admin.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_18.addWidget(self.botao_cancelar_alterar_admin)


        self.gridLayout_13.addWidget(self.frame_botoes_alterar_admin, 5, 0, 1, 2)

        self.linha_alterar_admin = QFrame(self.frame_alteracoes_admin)
        self.linha_alterar_admin.setObjectName(u"linha_alterar_admin")
        self.linha_alterar_admin.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(0, 0, 0);\n"
"    max-height: 1px;\n"
"    min-height: 1px;\n"
"}\n"
"")
        self.linha_alterar_admin.setFrameShape(QFrame.Shape.HLine)
        self.linha_alterar_admin.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_13.addWidget(self.linha_alterar_admin, 1, 0, 1, 2)

        self.label_id_admin_alterar = QLabel(self.frame_alteracoes_admin)
        self.label_id_admin_alterar.setObjectName(u"label_id_admin_alterar")
        self.label_id_admin_alterar.setStyleSheet(u"font: 700 12pt \"HeIvetica\";")

        self.gridLayout_13.addWidget(self.label_id_admin_alterar, 2, 0, 1, 1)


        self.gridLayout_14.addWidget(self.frame_alteracoes_admin, 1, 3, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_7, 0, 4, 2, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_8, 0, 0, 2, 1)

        self.tabWidget_listas.addTab(self.tab_administradores, "")

        self.gridLayout_5.addWidget(self.tabWidget_listas, 0, 0, 1, 1)

        self.tabWidget_telas.addTab(self.tab_listas, "")
        self.tab_cadastro = QWidget()
        self.tab_cadastro.setObjectName(u"tab_cadastro")
        self.horizontalLayout_4 = QHBoxLayout(self.tab_cadastro)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tabWidget_cadastro = QTabWidget(self.tab_cadastro)
        self.tabWidget_cadastro.setObjectName(u"tabWidget_cadastro")
        self.tabWidget_cadastro.setCursor(QCursor(Qt.ArrowCursor))
        self.tab_cadastro_morador = QWidget()
        self.tab_cadastro_morador.setObjectName(u"tab_cadastro_morador")
        self.horizontalLayout_7 = QHBoxLayout(self.tab_cadastro_morador)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_cadastro_morador = QFrame(self.tab_cadastro_morador)
        self.frame_cadastro_morador.setObjectName(u"frame_cadastro_morador")
        self.frame_cadastro_morador.setStyleSheet(u"QLabel{\n"
"border: 1px solid black;\n"
"border-radius: 2px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 1px solid black;\n"
"border-radius: 2px;\n"
"}")
        self.frame_cadastro_morador.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_cadastro_morador.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_cadastro_morador)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.lineEdit_endereco = QLineEdit(self.frame_cadastro_morador)
        self.lineEdit_endereco.setObjectName(u"lineEdit_endereco")
        sizePolicy1.setHeightForWidth(self.lineEdit_endereco.sizePolicy().hasHeightForWidth())
        self.lineEdit_endereco.setSizePolicy(sizePolicy1)
        self.lineEdit_endereco.setStyleSheet(u"    min-height: 29px;\n"
"    max-height: 29px;")

        self.gridLayout_7.addWidget(self.lineEdit_endereco, 3, 1, 1, 1)

        self.label_resultado_morador = QLabel(self.frame_cadastro_morador)
        self.label_resultado_morador.setObjectName(u"label_resultado_morador")
        sizePolicy3.setHeightForWidth(self.label_resultado_morador.sizePolicy().hasHeightForWidth())
        self.label_resultado_morador.setSizePolicy(sizePolicy3)
        self.label_resultado_morador.setStyleSheet(u"    min-height: 102px;\n"
"   ")

        self.gridLayout_7.addWidget(self.label_resultado_morador, 2, 2, 3, 1)

        self.lineEdit_senha_morador = QLineEdit(self.frame_cadastro_morador)
        self.lineEdit_senha_morador.setObjectName(u"lineEdit_senha_morador")
        sizePolicy1.setHeightForWidth(self.lineEdit_senha_morador.sizePolicy().hasHeightForWidth())
        self.lineEdit_senha_morador.setSizePolicy(sizePolicy1)
        self.lineEdit_senha_morador.setStyleSheet(u"    min-height: 29px;\n"
"    max-height: 29px;")

        self.gridLayout_7.addWidget(self.lineEdit_senha_morador, 5, 1, 1, 1)

        self.label_endereco = QLabel(self.frame_cadastro_morador)
        self.label_endereco.setObjectName(u"label_endereco")
        sizePolicy2.setHeightForWidth(self.label_endereco.sizePolicy().hasHeightForWidth())
        self.label_endereco.setSizePolicy(sizePolicy2)
        self.label_endereco.setFont(font1)
        self.label_endereco.setStyleSheet(u"min-height: 29px;\n"
"max-height: 29px;\n"
"font: 700 12pt \"HeIvetica\";\n"
"\n"
"")

        self.gridLayout_7.addWidget(self.label_endereco, 3, 0, 1, 1)

        self.lineEdit_nome_morador = QLineEdit(self.frame_cadastro_morador)
        self.lineEdit_nome_morador.setObjectName(u"lineEdit_nome_morador")
        sizePolicy1.setHeightForWidth(self.lineEdit_nome_morador.sizePolicy().hasHeightForWidth())
        self.lineEdit_nome_morador.setSizePolicy(sizePolicy1)
        self.lineEdit_nome_morador.setStyleSheet(u"    min-height: 29px;\n"
"    max-height: 29px;")

        self.gridLayout_7.addWidget(self.lineEdit_nome_morador, 2, 1, 1, 1)

        self.label_cadastro_morador = QLabel(self.frame_cadastro_morador)
        self.label_cadastro_morador.setObjectName(u"label_cadastro_morador")
        sizePolicy2.setHeightForWidth(self.label_cadastro_morador.sizePolicy().hasHeightForWidth())
        self.label_cadastro_morador.setSizePolicy(sizePolicy2)
        self.label_cadastro_morador.setFont(font2)
        self.label_cadastro_morador.setStyleSheet(u"font: 700 18pt \"Helvetica\";\n"
"border: 0px solid black;\n"
"border-radius: 2px;\n"
"\n"
"\n"
"\n"
"")
        self.label_cadastro_morador.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.label_cadastro_morador, 1, 0, 1, 3)

        self.botao_cadastro_morador = QPushButton(self.frame_cadastro_morador)
        self.botao_cadastro_morador.setObjectName(u"botao_cadastro_morador")
        self.botao_cadastro_morador.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_cadastro_morador.setStyleSheet(u"    QPushButton {\n"
"        background-color: rgb(230,230,230); /* Cor de fundo */\n"
"        color: black; /* Cor do texto */\n"
"        border: 1px solid rgb(84,84,84);/* Borda */\n"
"        border-radius: 10px; /* Cantos arredondados */\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(84,84,84); /* Cor de fundo */\n"
"        color: white; /* Cor do texto */\n"
"        border: 1px solid black; /* Borda */\n"
"        border-radius: 10px; /* Cantos arredondados */\n"
"    }\n"
"min-height: 29px;\n"
"max-height: 29px;\n"
"font: 700 12pt \"HeIvetica\";")

        self.gridLayout_7.addWidget(self.botao_cadastro_morador, 5, 2, 1, 1)

        self.label_senha_morador = QLabel(self.frame_cadastro_morador)
        self.label_senha_morador.setObjectName(u"label_senha_morador")
        sizePolicy2.setHeightForWidth(self.label_senha_morador.sizePolicy().hasHeightForWidth())
        self.label_senha_morador.setSizePolicy(sizePolicy2)
        self.label_senha_morador.setFont(font1)
        self.label_senha_morador.setStyleSheet(u"min-height: 29px;\n"
"max-height: 29px;\n"
"font: 700 12pt \"HeIvetica\";\n"
"\n"
"")

        self.gridLayout_7.addWidget(self.label_senha_morador, 5, 0, 1, 1)

        self.label_telefone = QLabel(self.frame_cadastro_morador)
        self.label_telefone.setObjectName(u"label_telefone")
        sizePolicy2.setHeightForWidth(self.label_telefone.sizePolicy().hasHeightForWidth())
        self.label_telefone.setSizePolicy(sizePolicy2)
        self.label_telefone.setFont(font1)
        self.label_telefone.setStyleSheet(u"min-height: 29px;\n"
"max-height: 29px;\n"
"font: 700 12pt \"HeIvetica\";\n"
"\n"
"")

        self.gridLayout_7.addWidget(self.label_telefone, 4, 0, 1, 1)

        self.lineEdit_telefone = QLineEdit(self.frame_cadastro_morador)
        self.lineEdit_telefone.setObjectName(u"lineEdit_telefone")
        sizePolicy1.setHeightForWidth(self.lineEdit_telefone.sizePolicy().hasHeightForWidth())
        self.lineEdit_telefone.setSizePolicy(sizePolicy1)
        self.lineEdit_telefone.setStyleSheet(u"    min-height: 29px;\n"
"    max-height: 29px;")

        self.gridLayout_7.addWidget(self.lineEdit_telefone, 4, 1, 1, 1)

        self.verticalSpacer_topo_morador = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.gridLayout_7.addItem(self.verticalSpacer_topo_morador, 0, 0, 1, 3)

        self.label_nome_morador = QLabel(self.frame_cadastro_morador)
        self.label_nome_morador.setObjectName(u"label_nome_morador")
        sizePolicy2.setHeightForWidth(self.label_nome_morador.sizePolicy().hasHeightForWidth())
        self.label_nome_morador.setSizePolicy(sizePolicy2)
        self.label_nome_morador.setFont(font1)
        self.label_nome_morador.setStyleSheet(u"min-height: 29px;\n"
"max-height: 29px;\n"
"font: 700 12pt \"HeIvetica\";\n"
"\n"
"")

        self.gridLayout_7.addWidget(self.label_nome_morador, 2, 0, 1, 1)

        self.verticalSpacer_embaixo_morador = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.gridLayout_7.addItem(self.verticalSpacer_embaixo_morador, 6, 0, 1, 3)


        self.horizontalLayout_7.addWidget(self.frame_cadastro_morador)

        self.tabWidget_cadastro.addTab(self.tab_cadastro_morador, "")
        self.tab_cadastro_admin = QWidget()
        self.tab_cadastro_admin.setObjectName(u"tab_cadastro_admin")
        self.horizontalLayout_5 = QHBoxLayout(self.tab_cadastro_admin)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_cadastro_admin = QFrame(self.tab_cadastro_admin)
        self.frame_cadastro_admin.setObjectName(u"frame_cadastro_admin")
        self.frame_cadastro_admin.setStyleSheet(u"QLabel{\n"
"border: 1px solid black;\n"
"border-radius: 2px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 1px solid black;\n"
"border-radius: 2px;\n"
"}")
        self.frame_cadastro_admin.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_cadastro_admin.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_cadastro_admin)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_resultado_admin = QLabel(self.frame_cadastro_admin)
        self.label_resultado_admin.setObjectName(u"label_resultado_admin")
        sizePolicy3.setHeightForWidth(self.label_resultado_admin.sizePolicy().hasHeightForWidth())
        self.label_resultado_admin.setSizePolicy(sizePolicy3)
        self.label_resultado_admin.setStyleSheet(u"    min-height: 69px;\n"
"   ")

        self.gridLayout_6.addWidget(self.label_resultado_admin, 2, 2, 2, 1)

        self.verticalSpacer_topo_admin_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.gridLayout_6.addItem(self.verticalSpacer_topo_admin_2, 0, 0, 1, 3)

        self.botao_cadastro_admin = QPushButton(self.frame_cadastro_admin)
        self.botao_cadastro_admin.setObjectName(u"botao_cadastro_admin")
        self.botao_cadastro_admin.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_cadastro_admin.setStyleSheet(u"    QPushButton {\n"
"        background-color: rgb(230,230,230); /* Cor de fundo */\n"
"        color: black; /* Cor do texto */\n"
"        border: 1px solid rgb(84,84,84);/* Borda */\n"
"        border-radius: 10px; /* Cantos arredondados */\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(84,84,84); /* Cor de fundo */\n"
"        color: white; /* Cor do texto */\n"
"        border: 1px solid black; /* Borda */\n"
"        border-radius: 10px; /* Cantos arredondados */\n"
"    }\n"
"min-height: 29px;\n"
"max-height: 29px;\n"
"font: 700 12pt \"HeIvetica\";")

        self.gridLayout_6.addWidget(self.botao_cadastro_admin, 4, 2, 1, 1)

        self.lineEdit_nome_admin = QLineEdit(self.frame_cadastro_admin)
        self.lineEdit_nome_admin.setObjectName(u"lineEdit_nome_admin")
        sizePolicy1.setHeightForWidth(self.lineEdit_nome_admin.sizePolicy().hasHeightForWidth())
        self.lineEdit_nome_admin.setSizePolicy(sizePolicy1)
        self.lineEdit_nome_admin.setStyleSheet(u"    min-height: 29px;\n"
"    max-height: 29px;")

        self.gridLayout_6.addWidget(self.lineEdit_nome_admin, 2, 1, 1, 1)

        self.lineEdit_email_admin = QLineEdit(self.frame_cadastro_admin)
        self.lineEdit_email_admin.setObjectName(u"lineEdit_email_admin")
        sizePolicy1.setHeightForWidth(self.lineEdit_email_admin.sizePolicy().hasHeightForWidth())
        self.lineEdit_email_admin.setSizePolicy(sizePolicy1)
        self.lineEdit_email_admin.setStyleSheet(u"    min-height: 29px;\n"
"    max-height: 29px;")

        self.gridLayout_6.addWidget(self.lineEdit_email_admin, 3, 1, 1, 1)

        self.label_email_admin = QLabel(self.frame_cadastro_admin)
        self.label_email_admin.setObjectName(u"label_email_admin")
        sizePolicy2.setHeightForWidth(self.label_email_admin.sizePolicy().hasHeightForWidth())
        self.label_email_admin.setSizePolicy(sizePolicy2)
        self.label_email_admin.setFont(font1)
        self.label_email_admin.setStyleSheet(u"min-height: 29px;\n"
"max-height: 29px;\n"
"font: 700 12pt \"HeIvetica\";\n"
"\n"
"")

        self.gridLayout_6.addWidget(self.label_email_admin, 3, 0, 1, 1)

        self.label_senha_admin = QLabel(self.frame_cadastro_admin)
        self.label_senha_admin.setObjectName(u"label_senha_admin")
        sizePolicy2.setHeightForWidth(self.label_senha_admin.sizePolicy().hasHeightForWidth())
        self.label_senha_admin.setSizePolicy(sizePolicy2)
        self.label_senha_admin.setFont(font1)
        self.label_senha_admin.setStyleSheet(u"min-height: 29px;\n"
"max-height: 29px;\n"
"font: 700 12pt \"HeIvetica\";\n"
"\n"
"")

        self.gridLayout_6.addWidget(self.label_senha_admin, 4, 0, 1, 1)

        self.label_nome_admin = QLabel(self.frame_cadastro_admin)
        self.label_nome_admin.setObjectName(u"label_nome_admin")
        sizePolicy2.setHeightForWidth(self.label_nome_admin.sizePolicy().hasHeightForWidth())
        self.label_nome_admin.setSizePolicy(sizePolicy2)
        self.label_nome_admin.setFont(font1)
        self.label_nome_admin.setStyleSheet(u"min-height: 29px;\n"
"max-height: 29px;\n"
"font: 700 12pt \"HeIvetica\";\n"
"\n"
"")

        self.gridLayout_6.addWidget(self.label_nome_admin, 2, 0, 1, 1)

        self.lineEdit_senha_admin = QLineEdit(self.frame_cadastro_admin)
        self.lineEdit_senha_admin.setObjectName(u"lineEdit_senha_admin")
        sizePolicy1.setHeightForWidth(self.lineEdit_senha_admin.sizePolicy().hasHeightForWidth())
        self.lineEdit_senha_admin.setSizePolicy(sizePolicy1)
        self.lineEdit_senha_admin.setStyleSheet(u"    min-height: 29px;\n"
"    max-height: 29px;")

        self.gridLayout_6.addWidget(self.lineEdit_senha_admin, 4, 1, 1, 1)

        self.label_cadastro_admin = QLabel(self.frame_cadastro_admin)
        self.label_cadastro_admin.setObjectName(u"label_cadastro_admin")
        sizePolicy2.setHeightForWidth(self.label_cadastro_admin.sizePolicy().hasHeightForWidth())
        self.label_cadastro_admin.setSizePolicy(sizePolicy2)
        self.label_cadastro_admin.setFont(font2)
        self.label_cadastro_admin.setStyleSheet(u"font: 700 18pt \"Helvetica\";\n"
"border: 0px solid black;\n"
"border-radius: 2px;\n"
"\n"
"\n"
"\n"
"")
        self.label_cadastro_admin.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.label_cadastro_admin, 1, 0, 1, 3)

        self.verticalSpacer_embaixo_admin_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.gridLayout_6.addItem(self.verticalSpacer_embaixo_admin_2, 5, 0, 1, 3)


        self.horizontalLayout_5.addWidget(self.frame_cadastro_admin)

        self.tabWidget_cadastro.addTab(self.tab_cadastro_admin, "")

        self.horizontalLayout_4.addWidget(self.tabWidget_cadastro)

        self.tabWidget_telas.addTab(self.tab_cadastro, "")

        self.verticalLayout_11.addWidget(self.tabWidget_telas)

        self.stackedWidget.addWidget(self.pag_conteudo)
        self.pag_configurar_conta = QWidget()
        self.pag_configurar_conta.setObjectName(u"pag_configurar_conta")
        self.verticalLayout_2 = QVBoxLayout(self.pag_configurar_conta)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_configurar_conta = QFrame(self.pag_configurar_conta)
        self.frame_configurar_conta.setObjectName(u"frame_configurar_conta")
        self.frame_configurar_conta.setStyleSheet(u"    QPushButton {\n"
"        background-color: rgb(230,230,230); /* Cor de fundo */\n"
"        color: black; /* Cor do texto */\n"
"        border: 1px solid rgb(84,84,84);/* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(84,84,84); /* Cor de fundo */\n"
"        color: white; /* Cor do texto */\n"
"        border: 1px solid black; /* Borda */\n"
"        border-radius: 2px; /* Cantos arredondados */\n"
"		font: 700 12pt \"HeIvetica\";\n"
"    }")
        self.frame_configurar_conta.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_configurar_conta.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_configurar_conta)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_18.addItem(self.verticalSpacer)

        self.frame_minha_conta = QFrame(self.frame_configurar_conta)
        self.frame_minha_conta.setObjectName(u"frame_minha_conta")
        self.frame_minha_conta.setMinimumSize(QSize(0, 0))
        self.frame_minha_conta.setStyleSheet(u"QLabel{\n"
"border: 1px solid black;\n"
"border-radius: 2px;\n"
"min-height: 29px;\n"
"max-height: 29px;\n"
"font: 700 12pt \"HeIvetica\";\n"
"}\n"
"\n"
"QLineEdit{\n"
"min-height: 29px;\n"
"max-height: 29px;\n"
"max-width: 200px;\n"
"border: 1px solid black;\n"
"border-radius: 2px;\n"
"font: 12pt \"HeIvetica\";\n"
"}\n"
"QFrame{\n"
"border:0px;\n"
"}\n"
"")
        self.frame_minha_conta.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_minha_conta.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_minha_conta)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_minha_conta = QLabel(self.frame_minha_conta)
        self.label_minha_conta.setObjectName(u"label_minha_conta")
        self.label_minha_conta.setStyleSheet(u"font: 700 18pt \"Helvetica\";\n"
"border: 0px solid black;\n"
"border-radius: 2px;")
        self.label_minha_conta.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_15.addWidget(self.label_minha_conta, 0, 2, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_11, 1, 4, 1, 1)

        self.label_email_minha_conta = QLabel(self.frame_minha_conta)
        self.label_email_minha_conta.setObjectName(u"label_email_minha_conta")

        self.gridLayout_15.addWidget(self.label_email_minha_conta, 2, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_10, 1, 0, 1, 1)

        self.botao_alterar_senha_conta = QPushButton(self.frame_minha_conta)
        self.botao_alterar_senha_conta.setObjectName(u"botao_alterar_senha_conta")
        self.botao_alterar_senha_conta.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_alterar_senha_conta.setStyleSheet(u"")

        self.gridLayout_15.addWidget(self.botao_alterar_senha_conta, 2, 3, 1, 1)

        self.lineEdit_nome_minha_conta = QLineEdit(self.frame_minha_conta)
        self.lineEdit_nome_minha_conta.setObjectName(u"lineEdit_nome_minha_conta")

        self.gridLayout_15.addWidget(self.lineEdit_nome_minha_conta, 1, 2, 1, 1)

        self.botao_editar_conta = QPushButton(self.frame_minha_conta)
        self.botao_editar_conta.setObjectName(u"botao_editar_conta")
        self.botao_editar_conta.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_editar_conta.setStyleSheet(u"")

        self.gridLayout_15.addWidget(self.botao_editar_conta, 1, 3, 1, 1)

        self.label_nome_minha_conta = QLabel(self.frame_minha_conta)
        self.label_nome_minha_conta.setObjectName(u"label_nome_minha_conta")

        self.gridLayout_15.addWidget(self.label_nome_minha_conta, 1, 1, 1, 1)

        self.frame_botoes_minha_conta = QFrame(self.frame_minha_conta)
        self.frame_botoes_minha_conta.setObjectName(u"frame_botoes_minha_conta")
        self.frame_botoes_minha_conta.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_botoes_minha_conta.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_botoes_minha_conta)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.botao_salvar_minha_conta = QPushButton(self.frame_botoes_minha_conta)
        self.botao_salvar_minha_conta.setObjectName(u"botao_salvar_minha_conta")
        self.botao_salvar_minha_conta.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_21.addWidget(self.botao_salvar_minha_conta)

        self.botao_cancelar_minha_conta = QPushButton(self.frame_botoes_minha_conta)
        self.botao_cancelar_minha_conta.setObjectName(u"botao_cancelar_minha_conta")
        self.botao_cancelar_minha_conta.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_21.addWidget(self.botao_cancelar_minha_conta)


        self.gridLayout_15.addWidget(self.frame_botoes_minha_conta, 3, 2, 1, 1)

        self.lineEdit_email_minha_conta = QLineEdit(self.frame_minha_conta)
        self.lineEdit_email_minha_conta.setObjectName(u"lineEdit_email_minha_conta")

        self.gridLayout_15.addWidget(self.lineEdit_email_minha_conta, 2, 2, 1, 1)


        self.verticalLayout_18.addWidget(self.frame_minha_conta)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_2)


        self.verticalLayout_2.addWidget(self.frame_configurar_conta)

        self.stackedWidget.addWidget(self.pag_configurar_conta)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_telas)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget_telas.setCurrentIndex(0)
        self.tabWidget_listas.setCurrentIndex(0)
        self.tabWidget_cadastro.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.botao_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.botao_configurar_conta.setText(QCoreApplication.translate("MainWindow", u"Configurar conta", None))
        self.botao_sair.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.label_peso.setText(QCoreApplication.translate("MainWindow", u"Peso", None))
        self.botao_realizar_cadastro.setText(QCoreApplication.translate("MainWindow", u"Realizar Cadastro", None))
        self.label_resultado_cadastro.setText(QCoreApplication.translate("MainWindow", u"O pacote foi inserido com o id:", None))
        self.label_descricao.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        self.label_status.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_cadastro_pacotes.setText(QCoreApplication.translate("MainWindow", u"Cadastro de Pacotes", None))
        self.label_volume.setText(QCoreApplication.translate("MainWindow", u"Volume", None))
        self.label_id_morador.setText(QCoreApplication.translate("MainWindow", u"ID Morador", None))
        self.tabWidget_telas.setTabText(self.tabWidget_telas.indexOf(self.tab_cadastro_pacotes), QCoreApplication.translate("MainWindow", u"Cadastro de Pacotes", None))
        self.label_criacao_remessas.setText(QCoreApplication.translate("MainWindow", u"Cria\u00e7\u00e3o de Remessas", None))
        ___qtablewidgetitem = self.tableWidget_morador.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID_Morador", None));
        ___qtablewidgetitem1 = self.tableWidget_morador.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem2 = self.tableWidget_morador.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None));
        ___qtablewidgetitem3 = self.tableWidget_morador.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Telefone", None));
        ___qtablewidgetitem4 = self.tableWidget_pacote.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"ID_Pacote", None));
        ___qtablewidgetitem5 = self.tableWidget_pacote.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtablewidgetitem6 = self.tableWidget_pacote.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"ID_Morador", None));
        ___qtablewidgetitem7 = self.tableWidget_pacote.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem8 = self.tableWidget_pacote.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Volume", None));
        ___qtablewidgetitem9 = self.tableWidget_pacote.horizontalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Peso", None));
        self.label_mapa_remessa.setText(QCoreApplication.translate("MainWindow", u"Mapa", None))

        self.label_id_pacote_1.setText(QCoreApplication.translate("MainWindow", u"ID_Pacote", None))
        self.label_endereco_1.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None))
        self.botao_iniciar_remessa.setText("Iniciar Remessa")
        self.QlineEdit_Id_Remessa.setPlaceholderText("ID Remessa")

        self.label_compartimento_1.setText(QCoreApplication.translate("MainWindow", u"Compartimento 1", None))
        self.label_texto_endereco_1.setText("")

        self.label_endereco_2.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None))
        self.label_id_pacote_2.setText(QCoreApplication.translate("MainWindow", u"ID_Pacote", None))
        self.label_compartimento_2.setText(QCoreApplication.translate("MainWindow", u"Compartimento 2", None))
        self.label_texto_endereco_2.setText("")

        self.botao_json_remessa.setText(QCoreApplication.translate("MainWindow", u"Cadastrar\nRemessa", None))
        self.tabWidget_telas.setTabText(self.tabWidget_telas.indexOf(self.tab_criacao_remessa), QCoreApplication.translate("MainWindow", u"Cria\u00e7\u00e3o de Remessas", None))

        self.label_volume_alterar.setText(QCoreApplication.translate("MainWindow", u"Volume", None))
        self.label_id_morador_alterar.setText(QCoreApplication.translate("MainWindow", u"ID Morador", None))
        self.label_alterar_pacote.setText(QCoreApplication.translate("MainWindow", u"Alterar Pacote", None))
        self.label_status_alterar.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.botao_salvar_alterar_pacote.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.botao_cancelar_alterar_pacote.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.label_peso_alterar.setText(QCoreApplication.translate("MainWindow", u"Peso", None))
        self.label_descricao_alterar.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        self.label_id_pacote_alterar_2.setText(QCoreApplication.translate("MainWindow", u"ID_Pacote", None))
        self.label_id_pacote_num.setText("")
        ___qtablewidgetitem10 = self.tableWidget_lista_pacotes.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"ID_Pacote", None));
        ___qtablewidgetitem11 = self.tableWidget_lista_pacotes.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtablewidgetitem12 = self.tableWidget_lista_pacotes.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"ID_Morador", None));
        ___qtablewidgetitem13 = self.tableWidget_lista_pacotes.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem14 = self.tableWidget_lista_pacotes.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Volume", None));
        ___qtablewidgetitem15 = self.tableWidget_lista_pacotes.horizontalHeaderItem(5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Peso", None));
        self.label_filtro.setText(QCoreApplication.translate("MainWindow", u"Filtro", None))
        self.comboBox_filtro_pacotes.setItemText(0, QCoreApplication.translate("MainWindow", u"ID_Pacote", None))
        self.comboBox_filtro_pacotes.setItemText(1, QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        self.comboBox_filtro_pacotes.setItemText(2, QCoreApplication.translate("MainWindow", u"ID_Morador", None))
        self.comboBox_filtro_pacotes.setItemText(3, QCoreApplication.translate("MainWindow", u"Status", None))
        self.comboBox_filtro_pacotes.setItemText(4, QCoreApplication.translate("MainWindow", u"Volume", None))
        self.comboBox_filtro_pacotes.setItemText(5, QCoreApplication.translate("MainWindow", u"Peso", None))

        self.botao_aplicar_pacotes.setText(QCoreApplication.translate("MainWindow", u"Aplicar", None))
        self.botao_restaurar_filtro_pacotes.setText(QCoreApplication.translate("MainWindow", u"Restaurar", None))
        self.botao_filtro_pacote.setText(QCoreApplication.translate("MainWindow", u"Filtro", None))
        self.botao_alterar_pacote.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.botao_excluir_pacote.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget_listas.setTabText(self.tabWidget_listas.indexOf(self.tab_pacotes), QCoreApplication.translate("MainWindow", u"Pacotes", None))
        ___qtablewidgetitem16 = self.tableWidget_lista_remessa.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"ID_Remessa", None));
        ___qtablewidgetitem17 = self.tableWidget_lista_remessa.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"ID_Pacote_1", None));
        ___qtablewidgetitem18 = self.tableWidget_lista_remessa.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"ID_Pacote_2", None));
        self.botao_filtro_remessa.setText(QCoreApplication.translate("MainWindow", u"Filtro", None))
        self.botao_alterar_remessa.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.botao_excluir_remessa.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.label_filtro_remessa.setText(QCoreApplication.translate("MainWindow", u"Filtro", None))
        self.comboBox_filtro_remessa.setItemText(0, QCoreApplication.translate("MainWindow", u"ID_Remessa", None))
        self.comboBox_filtro_remessa.setItemText(1, QCoreApplication.translate("MainWindow", u"ID_Pacote_1", None))
        self.comboBox_filtro_remessa.setItemText(2, QCoreApplication.translate("MainWindow", u"ID_Pacote_2", None))

        self.botao_aplicar_remessa.setText(QCoreApplication.translate("MainWindow", u"Aplicar", None))
        self.botao_restaurar_filtro_remessa.setText(QCoreApplication.translate("MainWindow", u"Restaurar", None))
        self.label_alterar_remessa.setText(QCoreApplication.translate("MainWindow", u"Alterar Remessa", None))
        self.label_id_pacote_1_alterar.setText(QCoreApplication.translate("MainWindow", u"ID_Pacote 1", None))
        self.botao_salvar_alterar_remessa.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.botao_cancelar_alterar_remessa.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.label_id_pacote_2_alterar.setText(QCoreApplication.translate("MainWindow", u"ID_Pacote 2", None))
        self.label_id_remessa_alterar.setText(QCoreApplication.translate("MainWindow", u"ID_Remessa", None))
        self.label_id_remessa_alterar_num.setText("")
        self.tabWidget_listas.setTabText(self.tabWidget_listas.indexOf(self.tab_remessas), QCoreApplication.translate("MainWindow", u"Remessas", None))
        ___qtablewidgetitem19 = self.tableWidget_lista_moradores.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"ID_Morador", None));
        ___qtablewidgetitem20 = self.tableWidget_lista_moradores.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem21 = self.tableWidget_lista_moradores.horizontalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None));
        ___qtablewidgetitem22 = self.tableWidget_lista_moradores.horizontalHeaderItem(3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Telefone", None));
        self.botao_filtro_morador.setText(QCoreApplication.translate("MainWindow", u"Filtro", None))
        self.botao_alterar_morador.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.botao_excluir_morador.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.label_filtro_morador.setText(QCoreApplication.translate("MainWindow", u"Filtro", None))
        self.comboBox_filtro_morador.setItemText(0, QCoreApplication.translate("MainWindow", u"ID_Morador", None))
        self.comboBox_filtro_morador.setItemText(1, QCoreApplication.translate("MainWindow", u"Nome", None))
        self.comboBox_filtro_morador.setItemText(2, QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None))
        self.comboBox_filtro_morador.setItemText(3, QCoreApplication.translate("MainWindow", u"Telefone", None))

        self.botao_aplicar_morador.setText(QCoreApplication.translate("MainWindow", u"Aplicar", None))
        self.botao_restaurar_filtro_morador.setText(QCoreApplication.translate("MainWindow", u"Restaurar", None))
        self.label_id_morador_num.setText("")
        self.label_telefone_alterar.setText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.label_id_morador_alterar_2.setText(QCoreApplication.translate("MainWindow", u"ID_Morador", None))
        self.label_alterar_morador.setText(QCoreApplication.translate("MainWindow", u"Alterar Morador", None))
        self.label_nome_morador_alterar.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_endereco_alterar.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None))
        self.botao_salvar_alterar_morador.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.botao_cancelar_alterar_morador.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.tabWidget_listas.setTabText(self.tabWidget_listas.indexOf(self.tab_moradores), QCoreApplication.translate("MainWindow", u"Moradores", None))
        ___qtablewidgetitem23 = self.tableWidget_lista_admin.horizontalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"ID_Administrador", None));
        ___qtablewidgetitem24 = self.tableWidget_lista_admin.horizontalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem25 = self.tableWidget_lista_admin.horizontalHeaderItem(2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        self.botao_filtro_admin.setText(QCoreApplication.translate("MainWindow", u"Filtro", None))
        self.botao_alterar_admin.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.botao_excluir_admin.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.label_filtro_admin.setText(QCoreApplication.translate("MainWindow", u"Filtro", None))
        self.comboBox_filtro_admin.setItemText(0, QCoreApplication.translate("MainWindow", u"ID_Administrador", None))
        self.comboBox_filtro_admin.setItemText(1, QCoreApplication.translate("MainWindow", u"Nome", None))
        self.comboBox_filtro_admin.setItemText(2, QCoreApplication.translate("MainWindow", u"Email", None))

        self.botao_aplicar_admin.setText(QCoreApplication.translate("MainWindow", u"Aplicar", None))
        self.botao_restaurar_filtro_admin.setText(QCoreApplication.translate("MainWindow", u"Restaurar", None))
        self.label_id_admin_num.setText("")
        self.label_email_alterar.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_nome_admin_alterar.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_alterar_admin.setText(QCoreApplication.translate("MainWindow", u"Alterar Administrador", None))
        self.botao_salvar_alterar_admin.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.botao_cancelar_alterar_admin.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.label_id_admin_alterar.setText(QCoreApplication.translate("MainWindow", u"ID_Administrador", None))
        self.tabWidget_listas.setTabText(self.tabWidget_listas.indexOf(self.tab_administradores), QCoreApplication.translate("MainWindow", u"Administradores", None))
        self.tabWidget_telas.setTabText(self.tabWidget_telas.indexOf(self.tab_listas), QCoreApplication.translate("MainWindow", u"Listas", None))
        self.label_resultado_morador.setText(QCoreApplication.translate("MainWindow", u"Morador cadastrado com o id:", None))
        self.label_endereco.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None))
        self.label_cadastro_morador.setText(QCoreApplication.translate("MainWindow", u"Cadastro de Morador", None))
        self.botao_cadastro_morador.setText(QCoreApplication.translate("MainWindow", u"Realizar Cadastro", None))
        self.label_senha_morador.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.label_telefone.setText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.label_nome_morador.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.tabWidget_cadastro.setTabText(self.tabWidget_cadastro.indexOf(self.tab_cadastro_morador), QCoreApplication.translate("MainWindow", u"Cadastro de Moradores", None))
        self.label_resultado_admin.setText(QCoreApplication.translate("MainWindow", u"Administrador cadastrado com o id:", None))
        self.botao_cadastro_admin.setText(QCoreApplication.translate("MainWindow", u"Realizar Cadastro", None))
        self.label_email_admin.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_senha_admin.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.label_nome_admin.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_cadastro_admin.setText(QCoreApplication.translate("MainWindow", u"Cadastro de Administrador", None))
        self.tabWidget_cadastro.setTabText(self.tabWidget_cadastro.indexOf(self.tab_cadastro_admin), QCoreApplication.translate("MainWindow", u"Cadastro de Administradores", None))
        self.tabWidget_telas.setTabText(self.tabWidget_telas.indexOf(self.tab_cadastro), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.label_minha_conta.setText(QCoreApplication.translate("MainWindow", u"Minha Conta", None))
        self.label_email_minha_conta.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.botao_alterar_senha_conta.setText(QCoreApplication.translate("MainWindow", u"Alterar Senha", None))
        self.botao_editar_conta.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.label_nome_minha_conta.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.botao_salvar_minha_conta.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.botao_cancelar_minha_conta.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
    # retranslateUi
