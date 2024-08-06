# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'telasNoFzDc.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QGridLayout,
                               QHBoxLayout, QHeaderView, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QScrollArea, QSizePolicy,
                               QSpacerItem, QTabWidget, QTableWidget, QTableWidgetItem,
                               QVBoxLayout, QWidget)
from remessa_controller import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setPointSize(12)
        self.centralwidget.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
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
        self.tabWidget_telas = QTabWidget(self.frame_telas)
        self.tabWidget_telas.setObjectName(u"tabWidget_telas")
        self.tab_cadastro_pacotes = QWidget()
        self.tab_cadastro_pacotes.setObjectName(u"tab_cadastro_pacotes")
        self.verticalLayout_11 = QVBoxLayout(self.tab_cadastro_pacotes)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
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

        self.vertocalSpacer_topo_pacote = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum,
                                                      QSizePolicy.Policy.MinimumExpanding)

        self.gridLayout.addItem(self.vertocalSpacer_topo_pacote, 0, 0, 1, 5)

        self.verticalSpacer_embaixo_pacote = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum,
                                                         QSizePolicy.Policy.MinimumExpanding)

        self.gridLayout.addItem(self.verticalSpacer_embaixo_pacote, 6, 0, 1, 5)

        self.verticalLayout_11.addWidget(self.frame_cadastro_pacotes)

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
        if (self.tableWidget_morador.columnCount() < 3):
            self.tableWidget_morador.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_morador.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_morador.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_morador.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget_morador.setObjectName(u"tableWidget_morador")
        self.tableWidget_morador.setStyleSheet(u"QTableWidget {\n"
                                               "    border: 1px solid black;\n"
                                               "    border-radius: 2px;\n"
                                               "}")

        self.horizontalLayout_10.addWidget(self.tableWidget_morador)

        self.tableWidget_pacote = QTableWidget(self.frame_tabelas_mapa)
        if (self.tableWidget_pacote.columnCount() < 6):
            self.tableWidget_pacote.setColumnCount(6)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_pacote.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_pacote.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_pacote.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_pacote.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_pacote.setHorizontalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_pacote.setHorizontalHeaderItem(5, __qtablewidgetitem8)
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
        self.label_remessa = QLabel(self.frame_dados_remessa)
        self.label_remessa.setObjectName(u"label_remessa")
        self.label_remessa.setStyleSheet(u"font: 700 12pt \"HeIvetica\";\n"
                                         "min-width: 95px;")

        self.gridLayout_3.addWidget(self.label_remessa, 0, 0, 1, 1)

        self.label_id_pacote_1 = QLabel(self.frame_dados_remessa)
        self.label_id_pacote_1.setObjectName(u"label_id_pacote_1")
        self.label_id_pacote_1.setStyleSheet(u"min-width: 95px;")

        self.gridLayout_3.addWidget(self.label_id_pacote_1, 2, 0, 1, 1)

        self.label_endereco_1 = QLabel(self.frame_dados_remessa)
        self.label_endereco_1.setObjectName(u"label_endereco_1")
        self.label_endereco_1.setStyleSheet(u"min-width: 95px;")

        self.gridLayout_3.addWidget(self.label_endereco_1, 3, 0, 1, 1)

        self.label_detalhes_remessa = QLabel(self.frame_dados_remessa)
        self.label_detalhes_remessa.setObjectName(u"label_detalhes_remessa")
        self.label_detalhes_remessa.setStyleSheet(u"QLabel{\n"
                                                  "border: 0px solid black;\n"
                                                  "font: 700 12pt \"HeIvetica\";\n"
                                                  "}\n"
                                                  "\n"
                                                  "\n"
                                                  "")

        self.gridLayout_3.addWidget(self.label_detalhes_remessa, 4, 0, 1, 5)

        self.label_intermediario_1 = QLabel(self.frame_dados_remessa)
        self.label_intermediario_1.setObjectName(u"label_intermediario_1")

        self.gridLayout_3.addWidget(self.label_intermediario_1, 6, 0, 1, 2)

        self.label_intermediario_2 = QLabel(self.frame_dados_remessa)
        self.label_intermediario_2.setObjectName(u"label_intermediario_2")

        self.gridLayout_3.addWidget(self.label_intermediario_2, 7, 0, 1, 2)

        self.label_intermediario_3 = QLabel(self.frame_dados_remessa)
        self.label_intermediario_3.setObjectName(u"label_intermediario_3")

        self.gridLayout_3.addWidget(self.label_intermediario_3, 8, 0, 1, 2)

        self.label_intermediario_4 = QLabel(self.frame_dados_remessa)
        self.label_intermediario_4.setObjectName(u"label_intermediario_4")

        self.gridLayout_3.addWidget(self.label_intermediario_4, 9, 0, 1, 2)

        self.label_ponto_final = QLabel(self.frame_dados_remessa)
        self.label_ponto_final.setObjectName(u"label_ponto_final")

        self.gridLayout_3.addWidget(self.label_ponto_final, 10, 0, 1, 2)

        self.label_texto_remessa = QLabel(self.frame_dados_remessa)
        self.label_texto_remessa.setObjectName(u"label_texto_remessa")
        self.label_texto_remessa.setStyleSheet(u"font: 12pt \"HeIvetica\";\n"
                                               "min-width: 95px;")

        self.gridLayout_3.addWidget(self.label_texto_remessa, 0, 1, 1, 1)

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

        self.label_ponto_inicial = QLabel(self.frame_dados_remessa)
        self.label_ponto_inicial.setObjectName(u"label_ponto_inicial")

        self.gridLayout_3.addWidget(self.label_ponto_inicial, 5, 0, 1, 2)

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

        self.lineEdit_ponto_inicial = QLineEdit(self.frame_dados_remessa)
        self.lineEdit_ponto_inicial.setObjectName(u"lineEdit_ponto_inicial")

        self.gridLayout_3.addWidget(self.lineEdit_ponto_inicial, 5, 2, 1, 3)

        self.lineEdit_intermediario_1 = QLineEdit(self.frame_dados_remessa)
        self.lineEdit_intermediario_1.setObjectName(u"lineEdit_intermediario_1")

        self.gridLayout_3.addWidget(self.lineEdit_intermediario_1, 6, 2, 1, 3)

        self.lineEdit_intermediario_2 = QLineEdit(self.frame_dados_remessa)
        self.lineEdit_intermediario_2.setObjectName(u"lineEdit_intermediario_2")

        self.gridLayout_3.addWidget(self.lineEdit_intermediario_2, 7, 2, 1, 3)

        self.lineEdit_intermediario_3 = QLineEdit(self.frame_dados_remessa)
        self.lineEdit_intermediario_3.setObjectName(u"lineEdit_intermediario_3")

        self.gridLayout_3.addWidget(self.lineEdit_intermediario_3, 8, 2, 1, 3)

        self.lineEdit_intermediario_4 = QLineEdit(self.frame_dados_remessa)
        self.lineEdit_intermediario_4.setObjectName(u"lineEdit_intermediario_4")

        self.gridLayout_3.addWidget(self.lineEdit_intermediario_4, 9, 2, 1, 3)

        self.lineEdit_ponto_final = QLineEdit(self.frame_dados_remessa)
        self.lineEdit_ponto_final.setObjectName(u"lineEdit_ponto_final")

        self.gridLayout_3.addWidget(self.lineEdit_ponto_final, 10, 2, 1, 3)

        self.horizontalLayout_9.addWidget(self.frame_dados_remessa)

        self.frame_gerar_json = QFrame(self.frame_remessa_json)
        self.frame_gerar_json.setObjectName(u"frame_gerar_json")
        sizePolicy.setHeightForWidth(self.frame_gerar_json.sizePolicy().hasHeightForWidth())
        self.frame_gerar_json.setSizePolicy(sizePolicy)
        self.frame_gerar_json.setStyleSheet(u"QFrame {\n"
                                            "    border: 1px solid black;\n"
                                            "    border-radius: 2px;\n"
                                            "}")
        self.frame_gerar_json.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_gerar_json.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_gerar_json)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_instrucoes_json = QLabel(self.frame_gerar_json)
        self.label_instrucoes_json.setObjectName(u"label_instrucoes_json")
        self.label_instrucoes_json.setStyleSheet(u"border: 0px solid black;\n"
                                                 "font: 700 12pt \"HeIvetica\";\n"
                                                 "")

        self.verticalLayout_8.addWidget(self.label_instrucoes_json)

        self.label_texto_criacao_json = QLabel(self.frame_gerar_json)
        self.label_texto_criacao_json.setObjectName(u"label_texto_criacao_json")
        sizePolicy3.setHeightForWidth(self.label_texto_criacao_json.sizePolicy().hasHeightForWidth())
        self.label_texto_criacao_json.setSizePolicy(sizePolicy3)
        self.label_texto_criacao_json.setStyleSheet(u"border: 1px solid black;\n"
                                                    "")

        self.verticalLayout_8.addWidget(self.label_texto_criacao_json)

        self.botao_json_remessa = QPushButton(self.frame_gerar_json)

        self.botao_json_remessa.clicked.connect(
                lambda:
                self.label_texto_criacao_json.setText(criar_remessa(
                        self.lineEdit_ponto_inicial.text(),
                        self.lineEdit_intermediario_1.text(),
                        self.lineEdit_intermediario_2.text(),
                        self.lineEdit_intermediario_3.text(),
                        self.lineEdit_intermediario_4.text(),
                        self.lineEdit_ponto_final.text()
                )
                )
        )

        self.botao_json_remessa.setObjectName(u"botao_json_remessa")
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

        self.verticalLayout_8.addWidget(self.botao_json_remessa)

        self.horizontalLayout_9.addWidget(self.frame_gerar_json)

        self.verticalLayout_10.addWidget(self.frame_remessa_json)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_8.addWidget(self.scrollArea)

        self.tabWidget_telas.addTab(self.tab_criacao_remessa, "")
        self.tab_acompanhamento = QWidget()
        self.tab_acompanhamento.setObjectName(u"tab_acompanhamento")
        self.verticalLayout_3 = QVBoxLayout(self.tab_acompanhamento)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_topo_acompanhamento = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum,
                                                              QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.verticalSpacer_topo_acompanhamento)

        self.label_acompanhamento = QLabel(self.tab_acompanhamento)
        self.label_acompanhamento.setObjectName(u"label_acompanhamento")
        self.label_acompanhamento.setStyleSheet(u"font: 700 18pt \"HeIvetica\";\n"
                                                "border: 0px solid black;\n"
                                                "border-radius: 2px;")
        self.label_acompanhamento.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_acompanhamento)

        self.frame_acompanhamento = QFrame(self.tab_acompanhamento)
        self.frame_acompanhamento.setObjectName(u"frame_acompanhamento")
        self.frame_acompanhamento.setStyleSheet(u"QFrame {\n"
                                                "    border: 0px solid black;\n"
                                                "    border-radius: 2px;\n"
                                                "}")
        self.frame_acompanhamento.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_acompanhamento.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_acompanhamento)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_mapa_acompanhamento = QFrame(self.frame_acompanhamento)
        self.frame_mapa_acompanhamento.setObjectName(u"frame_mapa_acompanhamento")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_mapa_acompanhamento.sizePolicy().hasHeightForWidth())
        self.frame_mapa_acompanhamento.setSizePolicy(sizePolicy4)
        self.frame_mapa_acompanhamento.setStyleSheet(u"QFrame {\n"
                                                     "    border: 1px solid black;\n"
                                                     "    border-radius: 2px;\n"
                                                     "}")
        self.frame_mapa_acompanhamento.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_mapa_acompanhamento.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_mapa_acompanhamento)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_mapa_acompanhamento = QLabel(self.frame_mapa_acompanhamento)
        self.label_mapa_acompanhamento.setObjectName(u"label_mapa_acompanhamento")
        self.label_mapa_acompanhamento.setStyleSheet(u"border: 0px solid black;\n"
                                                     "font: 700 12pt \"HeIvetica\";")

        self.verticalLayout_6.addWidget(self.label_mapa_acompanhamento)

        self.graphicsView_acompanhamento = QGraphicsView(self.frame_mapa_acompanhamento)
        self.graphicsView_acompanhamento.setObjectName(u"graphicsView_acompanhamento")

        self.verticalLayout_6.addWidget(self.graphicsView_acompanhamento)

        self.horizontalLayout.addWidget(self.frame_mapa_acompanhamento)

        self.frame_json_acompanhamento = QFrame(self.frame_acompanhamento)
        self.frame_json_acompanhamento.setObjectName(u"frame_json_acompanhamento")
        sizePolicy.setHeightForWidth(self.frame_json_acompanhamento.sizePolicy().hasHeightForWidth())
        self.frame_json_acompanhamento.setSizePolicy(sizePolicy)
        self.frame_json_acompanhamento.setStyleSheet(u"QFrame {\n"
                                                     "    border: 1px solid black;\n"
                                                     "    border-radius: 2px;\n"
                                                     "}")
        self.frame_json_acompanhamento.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_json_acompanhamento.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_json_acompanhamento)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_json_acompanhamento = QLabel(self.frame_json_acompanhamento)
        self.label_json_acompanhamento.setObjectName(u"label_json_acompanhamento")
        self.label_json_acompanhamento.setStyleSheet(u"border: 0px solid black;\n"
                                                     "font: 700 12pt \"HeIvetica\";")

        self.verticalLayout_7.addWidget(self.label_json_acompanhamento)

        self.label_texto_json_acompanhamento = QLabel(self.frame_json_acompanhamento)
        self.label_texto_json_acompanhamento.setObjectName(u"label_texto_json_acompanhamento")
        sizePolicy3.setHeightForWidth(self.label_texto_json_acompanhamento.sizePolicy().hasHeightForWidth())
        self.label_texto_json_acompanhamento.setSizePolicy(sizePolicy3)

        self.verticalLayout_7.addWidget(self.label_texto_json_acompanhamento)

        self.frame_botoes_json = QFrame(self.frame_json_acompanhamento)
        self.frame_botoes_json.setObjectName(u"frame_botoes_json")
        self.frame_botoes_json.setStyleSheet(u"QFrame {\n"
                                             "    border: 0px solid black;\n"
                                             "    border-radius: 2px;\n"
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
        self.frame_botoes_json.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_botoes_json.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_botoes_json)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.botao_selec_json = QPushButton(self.frame_botoes_json)
        self.botao_selec_json.setObjectName(u"botao_selec_json")

        self.horizontalLayout_6.addWidget(self.botao_selec_json)

        self.botao_iniciar_remessa = QPushButton(self.frame_botoes_json)
        self.botao_iniciar_remessa.setObjectName(u"botao_iniciar_remessa")

        self.horizontalLayout_6.addWidget(self.botao_iniciar_remessa)

        self.verticalLayout_7.addWidget(self.frame_botoes_json)

        self.horizontalLayout.addWidget(self.frame_json_acompanhamento)

        self.frame_posicoes_carrinho = QFrame(self.frame_acompanhamento)
        self.frame_posicoes_carrinho.setObjectName(u"frame_posicoes_carrinho")
        sizePolicy.setHeightForWidth(self.frame_posicoes_carrinho.sizePolicy().hasHeightForWidth())
        self.frame_posicoes_carrinho.setSizePolicy(sizePolicy)
        self.frame_posicoes_carrinho.setStyleSheet(u"QFrame {\n"
                                                   "    border: 1px solid black;\n"
                                                   "    border-radius: 2px;\n"
                                                   "}")
        self.frame_posicoes_carrinho.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_posicoes_carrinho.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_posicoes_carrinho)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_texto_instrucao_passada = QLabel(self.frame_posicoes_carrinho)
        self.label_texto_instrucao_passada.setObjectName(u"label_texto_instrucao_passada")
        sizePolicy4.setHeightForWidth(self.label_texto_instrucao_passada.sizePolicy().hasHeightForWidth())
        self.label_texto_instrucao_passada.setSizePolicy(sizePolicy4)
        self.label_texto_instrucao_passada.setStyleSheet(u"min-width: 74px;")

        self.gridLayout_2.addWidget(self.label_texto_instrucao_passada, 0, 1, 1, 1)

        self.label_intrucao_passada = QLabel(self.frame_posicoes_carrinho)
        self.label_intrucao_passada.setObjectName(u"label_intrucao_passada")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_intrucao_passada.sizePolicy().hasHeightForWidth())
        self.label_intrucao_passada.setSizePolicy(sizePolicy5)
        self.label_intrucao_passada.setStyleSheet(u"font: 700 12pt \"HeIvetica\";\n"
                                                  "max-width: 128px;")

        self.gridLayout_2.addWidget(self.label_intrucao_passada, 0, 0, 1, 1)

        self.label_instrucao_atual = QLabel(self.frame_posicoes_carrinho)
        self.label_instrucao_atual.setObjectName(u"label_instrucao_atual")
        sizePolicy5.setHeightForWidth(self.label_instrucao_atual.sizePolicy().hasHeightForWidth())
        self.label_instrucao_atual.setSizePolicy(sizePolicy5)
        self.label_instrucao_atual.setStyleSheet(u"font: 700 12pt \"HeIvetica\";\n"
                                                 "max-width: 128px;")

        self.gridLayout_2.addWidget(self.label_instrucao_atual, 1, 0, 1, 1)

        self.label_texto_instrucao_atual = QLabel(self.frame_posicoes_carrinho)
        self.label_texto_instrucao_atual.setObjectName(u"label_texto_instrucao_atual")
        sizePolicy4.setHeightForWidth(self.label_texto_instrucao_atual.sizePolicy().hasHeightForWidth())
        self.label_texto_instrucao_atual.setSizePolicy(sizePolicy4)
        self.label_texto_instrucao_atual.setStyleSheet(u"min-width: 74px;")

        self.gridLayout_2.addWidget(self.label_texto_instrucao_atual, 1, 1, 1, 1)

        self.label_texto_destino_final = QLabel(self.frame_posicoes_carrinho)
        self.label_texto_destino_final.setObjectName(u"label_texto_destino_final")
        sizePolicy4.setHeightForWidth(self.label_texto_destino_final.sizePolicy().hasHeightForWidth())
        self.label_texto_destino_final.setSizePolicy(sizePolicy4)
        self.label_texto_destino_final.setStyleSheet(u"min-width: 74px;")

        self.gridLayout_2.addWidget(self.label_texto_destino_final, 4, 1, 1, 1)

        self.label_posicao_atual = QLabel(self.frame_posicoes_carrinho)
        self.label_posicao_atual.setObjectName(u"label_posicao_atual")
        sizePolicy5.setHeightForWidth(self.label_posicao_atual.sizePolicy().hasHeightForWidth())
        self.label_posicao_atual.setSizePolicy(sizePolicy5)
        self.label_posicao_atual.setStyleSheet(u"font: 700 12pt \"HeIvetica\";\n"
                                               "max-width: 128px;")

        self.gridLayout_2.addWidget(self.label_posicao_atual, 3, 0, 1, 1)

        self.label_destino_final = QLabel(self.frame_posicoes_carrinho)
        self.label_destino_final.setObjectName(u"label_destino_final")
        sizePolicy5.setHeightForWidth(self.label_destino_final.sizePolicy().hasHeightForWidth())
        self.label_destino_final.setSizePolicy(sizePolicy5)
        self.label_destino_final.setStyleSheet(u"font: 700 12pt \"HeIvetica\";\n"
                                               "max-width: 128px;")

        self.gridLayout_2.addWidget(self.label_destino_final, 4, 0, 1, 1)

        self.label_texto_posicao_atual = QLabel(self.frame_posicoes_carrinho)
        self.label_texto_posicao_atual.setObjectName(u"label_texto_posicao_atual")
        sizePolicy4.setHeightForWidth(self.label_texto_posicao_atual.sizePolicy().hasHeightForWidth())
        self.label_texto_posicao_atual.setSizePolicy(sizePolicy4)
        self.label_texto_posicao_atual.setStyleSheet(u"min-width: 74px;")

        self.gridLayout_2.addWidget(self.label_texto_posicao_atual, 3, 1, 1, 1)

        self.verticalSpacer_embaixo_posicao = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum,
                                                          QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_embaixo_posicao, 5, 0, 1, 2)

        self.verticalSpacer_meio_posicao = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Ignored)

        self.gridLayout_2.addItem(self.verticalSpacer_meio_posicao, 2, 0, 1, 2)

        self.horizontalLayout.addWidget(self.frame_posicoes_carrinho)

        self.verticalLayout_3.addWidget(self.frame_acompanhamento)

        self.verticalSpacer_embaixo_acompanhamento = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum,
                                                                 QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.verticalSpacer_embaixo_acompanhamento)

        self.tabWidget_telas.addTab(self.tab_acompanhamento, "")

        self.verticalLayout.addWidget(self.tabWidget_telas)

        self.verticalLayout_2.addWidget(self.frame_telas)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget_telas.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_peso.setText(QCoreApplication.translate("MainWindow", u"Peso", None))
        self.botao_realizar_cadastro.setText(QCoreApplication.translate("MainWindow", u"Realizar Cadastro", None))
        self.label_resultado_cadastro.setText(
            QCoreApplication.translate("MainWindow", u"O pacote foi inserido com o id:", None))
        self.label_descricao.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        self.label_status.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_cadastro_pacotes.setText(QCoreApplication.translate("MainWindow", u"Cadastro de Pacotes", None))
        self.label_volume.setText(QCoreApplication.translate("MainWindow", u"Volume", None))
        self.label_id_morador.setText(QCoreApplication.translate("MainWindow", u"ID Morador", None))
        self.tabWidget_telas.setTabText(self.tabWidget_telas.indexOf(self.tab_cadastro_pacotes),
                                        QCoreApplication.translate("MainWindow", u"Cadastro de Pacotes", None))
        self.label_criacao_remessas.setText(
            QCoreApplication.translate("MainWindow", u"Cria\u00e7\u00e3o de Remessas", None))
        ___qtablewidgetitem = self.tableWidget_morador.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID_Morador", None));
        ___qtablewidgetitem1 = self.tableWidget_morador.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem2 = self.tableWidget_morador.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None));
        ___qtablewidgetitem3 = self.tableWidget_pacote.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"ID_Pacote", None));
        ___qtablewidgetitem4 = self.tableWidget_pacote.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtablewidgetitem5 = self.tableWidget_pacote.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"ID_Morador", None));
        ___qtablewidgetitem6 = self.tableWidget_pacote.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem7 = self.tableWidget_pacote.horizontalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Volume", None));
        ___qtablewidgetitem8 = self.tableWidget_pacote.horizontalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Peso", None));
        self.label_mapa_remessa.setText(QCoreApplication.translate("MainWindow", u"Mapa", None))
        self.label_remessa.setText(QCoreApplication.translate("MainWindow", u"Remessa", None))
        self.label_id_pacote_1.setText(QCoreApplication.translate("MainWindow", u"ID_Pacote", None))
        self.label_endereco_1.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None))
        self.label_detalhes_remessa.setText(QCoreApplication.translate("MainWindow", u"Definir detalhes Remessa", None))
        self.label_intermediario_1.setText(
            QCoreApplication.translate("MainWindow", u"Ponto intermedi\u00e1rio 1:", None))
        self.label_intermediario_2.setText(
            QCoreApplication.translate("MainWindow", u"Ponto intermedi\u00e1rio 2:", None))
        self.label_intermediario_3.setText(
            QCoreApplication.translate("MainWindow", u"Ponto intermedi\u00e1rio 3:", None))
        self.label_intermediario_4.setText(
            QCoreApplication.translate("MainWindow", u"Ponto intermedi\u00e1rio 4:", None))
        self.label_ponto_final.setText(QCoreApplication.translate("MainWindow", u"Ponto Final:", None))
        self.label_texto_remessa.setText("")
        self.label_compartimento_1.setText(QCoreApplication.translate("MainWindow", u"Compartimento 1", None))
        self.label_texto_endereco_1.setText("")
        self.label_ponto_inicial.setText(QCoreApplication.translate("MainWindow", u"Ponto Inicial:", None))
        self.label_endereco_2.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None))
        self.label_id_pacote_2.setText(QCoreApplication.translate("MainWindow", u"ID_Pacote", None))
        self.label_compartimento_2.setText(QCoreApplication.translate("MainWindow", u"Compartimento 2", None))
        self.label_texto_endereco_2.setText("")
        self.label_instrucoes_json.setText(
            QCoreApplication.translate("MainWindow", u"Intru\u00e7\u00f5es - JSON", None))
        self.label_texto_criacao_json.setText("")
        self.botao_json_remessa.setText(QCoreApplication.translate("MainWindow", u"Gerar JSON/Cadastrar Remessa", None))
        self.tabWidget_telas.setTabText(self.tabWidget_telas.indexOf(self.tab_criacao_remessa),
                                        QCoreApplication.translate("MainWindow", u"Cria\u00e7\u00e3o de Remessas",
                                                                   None))
        self.label_acompanhamento.setText(QCoreApplication.translate("MainWindow", u"Acompanhamento de Remessas", None))
        self.label_mapa_acompanhamento.setText(QCoreApplication.translate("MainWindow", u"Mapa", None))
        self.label_json_acompanhamento.setText(
            QCoreApplication.translate("MainWindow", u"Intru\u00e7\u00f5es - JSON", None))
        self.label_texto_json_acompanhamento.setText("")
        self.botao_selec_json.setText(QCoreApplication.translate("MainWindow", u"Selec. JSON", None))
        self.botao_iniciar_remessa.setText(QCoreApplication.translate("MainWindow", u"Iniciar Remessa", None))
        self.label_texto_instrucao_passada.setText("")
        self.label_intrucao_passada.setText(QCoreApplication.translate("MainWindow", u"Instr. Passada", None))
        self.label_instrucao_atual.setText(QCoreApplication.translate("MainWindow", u"Instr. Atual", None))
        self.label_texto_instrucao_atual.setText("")
        self.label_texto_destino_final.setText("")
        self.label_posicao_atual.setText(QCoreApplication.translate("MainWindow", u"Posi\u00e7\u00e3o Atual", None))
        self.label_destino_final.setText(QCoreApplication.translate("MainWindow", u"Destino Final", None))
        self.label_texto_posicao_atual.setText("")
        self.tabWidget_telas.setTabText(self.tabWidget_telas.indexOf(self.tab_acompanhamento),
                                        QCoreApplication.translate("MainWindow", u"Acompanhamento de Remessas", None))
    # retranslateUi
