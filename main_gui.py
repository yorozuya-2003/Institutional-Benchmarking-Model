# MODULE STUFF
from modules import *

# UI STUFF
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets, QtCore

QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

# for dependent comboboxes
from PyQt5.QtGui import QStandardItemModel, QStandardItem

# counter for keeping in check the back and previous screen windows
counter = -1


# ABILITY JOB-TYPE SCALING SCREEN
abilityEntry, abiltyIntermediate, abilityHigh, abilityExpert \
    = map(float, [1, 1, 1, 1])


class ability_scaling_window(QMainWindow):
    def __init__(self):
        super(ability_scaling_window, self).__init__()
        uic.loadUi('ui_files/ability_scaling_screen.ui', self)

        self.nextButton.clicked.connect(self.checkInput)

    def checkInput(self):
        try:
            float(self.abilityEntry.text())
            float(self.abilityIntermediate.text())
            float(self.abilityHigh.text())
            float(self.abilityExpert.text())

            self.nextScreen()
        except:
            msg = QMessageBox()
            msg.setWindowTitle('ERROR')
            msg.setIcon(QMessageBox.Critical)
            error_text = 'Error detected in user input. '\
                'Ensure that the input is decimal or integer '\
                'value and there are no blank spaces '\
                'or other characters/symbols used.'
            msg.setText(error_text)
            msg.exec_()

    def nextScreen(self):
        global abilityEntry, abilityIntermediate, abilityHigh, abilityExpert
        abilityEntry = float(self.abilityEntry.text())
        abilityIntermediate = float(self.abilityIntermediate.text())
        abilityHigh = float(self.abilityHigh.text())
        abilityExpert = float(self.abilityExpert.text())

        abilityEntry, abilityIntermediate, abilityHigh, abilityExpert \
            = map(lambda x: x/abilityEntry,
                  [abilityEntry,
                   abilityIntermediate,
                   abilityHigh,
                   abilityExpert])

        print('Ability scaling:',
              abilityEntry, abiltyIntermediate, abilityHigh, abilityExpert)
        
        global counter
        if counter == -1:
            counter += 1
            next_window = jobType_scaling_window()
            widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


# JOB-TYPE SCALING SCREEN
jobSimple, jobMedium, jobHigh, jobComplex = map(float, [1, 1, 1, 1])


class jobType_scaling_window(QMainWindow):
    def __init__(self):
        super(jobType_scaling_window, self).__init__()
        uic.loadUi('ui_files/jobType_scaling_screen.ui', self)

        # adjusting label size
        self.heading.adjustSize()
        self.jobLabel.adjustSize()

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

    def checkInput(self):
        try:
            float(self.jobSimple.text())
            float(self.jobMedium.text())
            float(self.jobHigh.text())
            float(self.jobComplex.text())

            self.nextScreen()
        except:
            msg = QMessageBox()
            msg.setWindowTitle('ERROR')
            msg.setIcon(QMessageBox.Critical)
            error_text = 'Error detected in user input. '\
                'Ensure that the input is decimal or integer '\
                'value and there are no blank spaces '\
                'or other characters/symbols used.'
            msg.setText(error_text)
            msg.exec_()

    def nextScreen(self):
        global jobSimple, jobMedium, jobHigh, jobComplex
        jobSimple = float(self.jobSimple.text())
        jobMedium = float(self.jobMedium.text())
        jobHigh = float(self.jobHigh.text())
        jobComplex = float(self.jobComplex.text())

        jobSimple, jobMedium, jobHigh, jobComplex \
            = map(lambda x: x/jobSimple,
                  [jobSimple, jobMedium, jobHigh, jobComplex])

        print('JobType scaling:',
              jobSimple, jobMedium, jobHigh, jobComplex)

        global counter
        if counter == 0:
            counter += 1
            next_window = ability_jobType_window()
            widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# ABILITY JOB TYPE SCREEN
class ability_jobType_window(QMainWindow):
    def __init__(self):
        super(ability_jobType_window, self).__init__()
        uic.loadUi('ui_files/ability_jobType_screen.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

    def checkInput(self):
        try:
            int(self.s1.text())
            int(self.s2.text())
            int(self.s3.text())
            int(self.s4.text())

            int(self.m1.text())
            int(self.m2.text())
            int(self.m3.text())
            int(self.m4.text())

            int(self.h1.text())
            int(self.h2.text())
            int(self.h3.text())
            int(self.h4.text())

            int(self.c1.text())
            int(self.c2.text())
            int(self.c3.text())
            int(self.c4.text())

            self.nextScreen()
        except:
            msg = QMessageBox()
            msg.setWindowTitle('ERROR')
            msg.setIcon(QMessageBox.Critical)
            error_text = 'Error detected in user input. '\
                'Ensure that the input is an integer '\
                'value and there are no blank spaces '\
                'or other characters/symbols used.'
            msg.setText(error_text)
            msg.exec_()

    def nextScreen(self):
        global s1, s2, s3, s4
        s1 = self.s1.text()
        s2 = self.s2.text()
        s3 = self.s3.text()
        s4 = self.s4.text()

        global m1, m2, m3, m4
        m1 = self.m1.text()
        m2 = self.m2.text()
        m3 = self.m3.text()
        m4 = self.m4.text()

        global h1, h2, h3, h4
        h1 = self.h1.text()
        h2 = self.h2.text()
        h3 = self.h3.text()
        h4 = self.h4.text()

        global c1, c2, c3, c4
        c1 = self.c1.text()
        c2 = self.c2.text()
        c3 = self.c3.text()
        c4 = self.c4.text()

        s1, s2, s3, s4, m1, m2, m3, m4, h1, h2, h3, h4, c1, c2, c3, c4 \
            = map(int,
                  [s1, s2, s3, s4,
                   m1, m2, m3, m4,
                   h1, h2, h3, h4,
                   c1, c2, c3, c4])

        global E_Simple, E_Medium, E_High, E_Complex
        E_Simple = {
            "Entry": E(abilityEntry, jobSimple, s1),
            "Intermediate": E(abilityIntermediate, jobSimple, s2),
            "High": E(abilityHigh, jobSimple, s3),
            "Expert": E(abilityExpert, jobSimple, s4)
            }
        E_Medium = {
            "Entry": E(abilityEntry, jobMedium, m1),
            "Intermediate": E(abilityIntermediate, jobMedium, m2),
            "High": E(abilityHigh, jobMedium, m3),
            "Expert": E(abilityExpert, jobMedium, m4)
            }
        E_High = {
            "Entry": E(abilityEntry, jobHigh, h1),
            "Intermediate": E(abilityIntermediate, jobHigh, h2),
            "High": E(abilityHigh, jobHigh, h3),
            "Expert": E(abilityExpert, jobHigh, h4)
            }
        E_Complex = {
            "Entry": E(abilityEntry, jobComplex, c1),
            "Intermediate": E(abilityIntermediate, jobComplex, c2),
            "High": E(abilityHigh, jobComplex, c3),
            "Expert": E(abilityExpert, jobComplex, c4)
            }

        global Effort_Dict
        Effort_Dict = {
            'Simple': E_Simple,
            'Medium': E_Medium,
            'High': E_High,
            'Complex': E_Complex
            }

        global counter
        if counter == 1:
            counter += 1
            next_window = quality_window()
            widget.addWidget(next_window)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# QUALITY SCREEN
class quality_window(QMainWindow):
    def __init__(self):
        super(quality_window, self).__init__()
        uic.loadUi('ui_files/quality_screen.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

    def checkInput(self):
        try:
            float(self.paramA.text())
            float(self.paramB.text())
            float(self.paramC.text())
            float(self.paramD.text())

            self.nextScreen()
        except:
            msg = QMessageBox()
            msg.setWindowTitle('ERROR')
            msg.setIcon(QMessageBox.Critical)
            error_text = 'Error detected in user input. '\
                'Ensure that the input is decimal or integer '\
                'value and there are no blank spaces '\
                'or other characters/symbols used.'
            msg.setText(error_text)
            msg.exec_()

    def nextScreen(self):
        A = self.paramA.text()
        B = self.paramB.text()
        C = self.paramC.text()
        D = self.paramD.text()
        A, B, C, D = map(float, [A, B, C, D])

        global Q_parameterArray
        Q_parameterArray = [A, B, C, D]

        print('Q_parameterArray:', Q_parameterArray)

        global counter
        if counter == 2:
            counter += 1
            next_window = quality_scaling_window()
            widget.addWidget(next_window)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# QUALITY SCALING SCREEN
class quality_scaling_window(QMainWindow):
    def __init__(self):
        super(quality_scaling_window, self).__init__()
        uic.loadUi('ui_files/quality_scaling_screen.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

    def checkInput(self):
        try:
            float(self.qualityBasic.text())
            float(self.qualityStandard.text())
            float(self.qualityHigh.text())
            float(self.qualityPremium.text())

            self.nextScreen()
        except:
            msg = QMessageBox()
            msg.setWindowTitle('ERROR')
            msg.setIcon(QMessageBox.Critical)
            error_text = 'Error detected in user input. '\
                'Ensure that the input is decimal or integer '\
                'value and there are no blank spaces '\
                'or other characters/symbols used.'
            msg.setText(error_text)
            msg.exec_()

    def nextScreen(self):
        qualityBasic = self.qualityBasic.text()
        qualityStandard = self.qualityStandard.text()
        qualityHigh = self.qualityHigh.text()
        qualityPremium = self.qualityPremium.text()

        qualityBasic, qualityStandard, qualityHigh, qualityPremium \
            = map(float,
                  [qualityBasic, qualityStandard, qualityHigh, qualityPremium])
        qualityBasic, qualityStandard, qualityHigh, qualityPremium \
            = map(lambda x: x/qualityBasic,
                  [qualityBasic, qualityStandard, qualityHigh, qualityPremium])

        qualityScalingFactorsArray = [
            qualityBasic, qualityStandard, qualityHigh, qualityPremium
            ]

        print('qualityScalingFactorsArray:', qualityScalingFactorsArray)

        qualityFactorsInput(qualityScalingFactorsArray)

        # Quality Factors Mapping
        global Q_Simple, Q_Medium, Q_High, Q_Complex
        Q_Simple = {
            "Entry": Q(qualityBasic, s1, Q_parameterArray),
            "Intermediate": Q(0.75*qualityBasic, s2, Q_parameterArray),
            "High": Q(0.5*qualityBasic, s3, Q_parameterArray),
            "Expert": Q(0.25*qualityBasic, s4, Q_parameterArray)
            }
        Q_Medium = {
            "Entry": Q(qualityStandard, m1, Q_parameterArray),
            "Intermediate": Q(qualityStandard, m2, Q_parameterArray),
            "High": Q(qualityBasic, m3, Q_parameterArray),
            "Expert": Q(0.5*qualityBasic, m4, Q_parameterArray)
            }
        Q_High = {
            "Entry": Q(qualityHigh, h1, Q_parameterArray),
            "Intermediate": Q(qualityHigh, h2, Q_parameterArray),
            "High": Q(qualityStandard, h3, Q_parameterArray),
            "Expert": Q(qualityBasic, h4, Q_parameterArray)
            }
        Q_Complex = {
            "Entry": Q(qualityPremium, c1, Q_parameterArray),
            "Intermediate": Q(qualityPremium, c2, Q_parameterArray),
            "High": Q(qualityHigh, c3, Q_parameterArray),
            "Expert": Q(qualityStandard, c4, Q_parameterArray)
            }

        # Quality Output Dictionary
        global Quality_Dict
        Quality_Dict = {
            'Simple': Q_Simple,
            'Medium': Q_Medium,
            'High': Q_High,
            'Complex': Q_Complex
            }

        global counter
        if counter == 3:
            counter += 1
            next_window = management_window()
            widget.addWidget(next_window)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# MANAGEMENT SCREEN
class management_window(QMainWindow):
    def __init__(self):
        super(management_window, self).__init__()
        uic.loadUi('ui_files/management_screen.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

    def checkInput(self):
        try:
            float(self.paramE.text())
            float(self.paramF.text())
            float(self.paramG.text())
            float(self.paramH.text())
            float(self.paramI.text())

            self.nextScreen()
        except:
            msg = QMessageBox()
            msg.setWindowTitle('ERROR')
            msg.setIcon(QMessageBox.Critical)
            error_text = 'Error detected in user input. '\
                'Ensure that the input is decimal or integer '\
                'value and there are no blank spaces '\
                'or other characters/symbols used.'
            msg.setText(error_text)
            msg.exec_()

    def nextScreen(self):
        E = self.paramE.text()
        F = self.paramF.text()
        G = self.paramG.text()
        H = self.paramH.text()
        I = self.paramI.text()
        E, F, G, H, I = map(float, [E, F, G, H, I])

        global M_parameterArray
        M_parameterArray = [E, F, G, H, I]

        print('M_parameterArray:', M_parameterArray)

        global counter
        if counter == 4:
            counter += 1
            next_window = management_scaling_window()
            widget.addWidget(next_window)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# MANAGEMENT SCALING SCREEN
class management_scaling_window(QMainWindow):
    def __init__(self):
        super(management_scaling_window, self).__init__()
        uic.loadUi('ui_files/management_scaling_screen.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

    def checkInput(self):
        try:
            float(self.managementLow.text())
            float(self.managementMedium.text())
            float(self.managementHigh.text())

            self.nextScreen()
        except:
            msg = QMessageBox()
            msg.setWindowTitle('ERROR')
            msg.setIcon(QMessageBox.Critical)
            error_text = 'Error detected in user input. '\
                'Ensure that the input is decimal or integer '\
                'value and there are no blank spaces '\
                'or other characters/symbols used.'
            msg.setText(error_text)
            msg.exec_()

    def nextScreen(self):
        managementLow = self.managementLow.text()
        managementMedium = self.managementMedium.text()
        managementHigh = self.managementHigh.text()

        managementLow, managementMedium, managementHigh \
            = map(float,
                  [managementLow, managementMedium, managementHigh])
        managementLow, managementMedium, managementHigh \
            = map(lambda x: x/managementLow,
                  [managementLow, managementMedium, managementHigh])

        managementScalingFactorsArray \
            = [managementLow, managementMedium, managementHigh]

        print('managementScalingFactorsArray:', managementScalingFactorsArray)

        managementFactorsInput(managementScalingFactorsArray)

        # Management Factors Mapping
        global M_Simple, M_Medium, M_High, M_Complex
        M_Simple = {
            "Entry": M(managementLow, s1, M_parameterArray),
            "Intermediate": M(managementLow, s2, M_parameterArray)
            }
        M_Medium = {
            "Entry": M(managementMedium, m1, M_parameterArray),
            "Intermediate": M(managementMedium, m2, M_parameterArray),
            "High": M(managementLow, m3, M_parameterArray),
            "Expert": M(managementLow, m4, M_parameterArray)
            }
        M_High = {
            "Entry": M(managementHigh, h1, M_parameterArray),
            "Intermediate": M(managementHigh, h2, M_parameterArray),
            "High": M(managementMedium, h3, M_parameterArray),
            "Expert": M(managementLow, h4, M_parameterArray)
            }
        M_Complex = {
            "High": M(managementHigh, c3, M_parameterArray),
            "Expert": M(managementHigh, c4, M_parameterArray)
            }

        # Management Output Dictionary
        global Management_Dict
        Management_Dict = {
            'Simple': M_Simple,
            'Medium': M_Medium,
            'High': M_High,
            'Complex': M_Complex
            }

        global counter
        if counter == 5:
            counter += 1
            next_window = risk_window()
            widget.addWidget(next_window)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# RISK SCREEN
class risk_window(QMainWindow):
    def __init__(self):
        super(risk_window, self).__init__()
        uic.loadUi('ui_files/risk_screen.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

    def checkInput(self):
        try:
            float(self.paramJ.text())
            float(self.paramK.text())

            self.nextScreen()
        except:
            msg = QMessageBox()
            msg.setWindowTitle('ERROR')
            msg.setIcon(QMessageBox.Critical)
            error_text = 'Error detected in user input. '\
                'Ensure that the input is decimal or integer '\
                'value and there are no blank spaces '\
                'or other characters/symbols used.'
            msg.setText(error_text)
            msg.exec_()

    def nextScreen(self):
        J = self.paramJ.text()
        K = self.paramK.text()
        J, K = map(float, [J, K])

        global R_parameterArray
        R_parameterArray = [J, K]

        print('R_parameterArray:', R_parameterArray)

        global counter
        if counter == 6:
            counter += 1
            next_window = risk_scaling_window()
            widget.addWidget(next_window)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# RISK SCALING SCREEN
class risk_scaling_window(QMainWindow):
    def __init__(self):
        super(risk_scaling_window, self).__init__()
        uic.loadUi('ui_files/risk_scaling_screen.ui', self)

        self.nextButton.clicked.connect(self.checkInput)
        self.backButton.clicked.connect(self.backScreen)

        self.viewButton.clicked.connect(self.viewLookupTable)

    def checkInput(self):
        try:
            float(self.riskLow.text())
            float(self.riskMedium.text())
            float(self.riskHigh.text())
            float(self.riskComplex.text())

            self.nextScreen()
        except:
            msg = QMessageBox()
            msg.setWindowTitle('ERROR')
            msg.setIcon(QMessageBox.Critical)
            error_text = 'Error detected in user input. '\
                'Ensure that the input is decimal or integer '\
                'value and there are no blank spaces '\
                'or other characters/symbols used.'
            msg.setText(error_text)
            msg.exec_()

    def nextScreen(self):
        riskLow = self.riskLow.text()
        riskMedium = self.riskMedium.text()
        riskHigh = self.riskHigh.text()
        riskComplex = self.riskComplex.text()

        riskLow, riskMedium, riskHigh, riskComplex \
            = map(float,
                  [riskLow, riskMedium, riskHigh, riskComplex])
        riskLow, riskMedium, riskHigh, riskComplex \
            = map(lambda x: x/riskLow,
                  [riskLow, riskMedium, riskHigh, riskComplex])

        riskScalingFactorsArray = [riskLow, riskMedium, riskHigh, riskComplex]

        print('riskScalingFactorsArray:', riskScalingFactorsArray)

        riskFactorsInput(riskScalingFactorsArray)

        # Risk Factors Mapping
        global R_Low, R_Medium, R_High, R_NA
        R_Low = {
            "Simple": R(riskLow, R_parameterArray)
            }
        R_Medium = {
            "Simple": R(riskLow, R_parameterArray),
            "Medium": R(riskLow, R_parameterArray)
            }
        R_High = {
            "Simple": R(riskMedium, R_parameterArray),
            "Medium": R(riskMedium, R_parameterArray),
            "High": R(riskHigh, R_parameterArray)
            }
        R_NA = {
            "Simple": R(riskComplex, R_parameterArray),
            "Medium": R(riskComplex, R_parameterArray),
            "High": R(riskComplex, R_parameterArray),
            "NA": R(riskComplex, R_parameterArray)
            }

        # Risk Output Dictionary
        global Risk_Dict
        Risk_Dict = {
            'Low': R_Low,
            'Medium': R_Medium,
            'High': R_High,
            'NA': R_NA
            }

        global counter
        if counter == 7:
            counter += 1
            next_window = lookup_table_window()
            widget.addWidget(next_window)

        if counter == 8:
            counter += 1
            next_window = output_drop_down_window()
            widget.addWidget(next_window)

        widget.setCurrentIndex(widget.currentIndex() + 2)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def viewLookupTable(self):
        global counter
        if counter == 7:
            counter += 1
            next_window = lookup_table_window()
            widget.addWidget(next_window)

        if counter == 8:
            counter += 1
            next_window = output_drop_down_window()
            widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


# BUSINESS IMPACT LOOKUP TABLE
class lookup_table_window(QMainWindow):
    def __init__(self):
        super(lookup_table_window, self).__init__()
        uic.loadUi('ui_files/risk_lookup_table.ui', self)
        self.returnButton.clicked.connect(self.returnBack)

    def returnBack(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# OUTPUT SCREEN
class output_drop_down_window(QMainWindow):
    def __init__(self):
        super(output_drop_down_window, self).__init__()
        uic.loadUi('ui_files/output_drop_down_screen.ui', self)
        self.show()

        self.model = QStandardItemModel(self)

        self.factors.setModel(self.model)
        self.parameters1.setModel(self.model)
        self.parameters2.setModel(self.model)

        self.backButton.clicked.connect(self.backScreen)

        for factor_key in dictionary.keys():
            FACTOR = QStandardItem(factor_key)
            self.model.appendRow(FACTOR)
            factor_key_dict = dictionary.get(factor_key)

            for param1_key in factor_key_dict.keys():
                PARAM1 = QStandardItem(param1_key)
                FACTOR.appendRow(PARAM1)

                param1_array = factor_key_dict.get(param1_key)

                for value in param1_array:
                    PARAM2 = QStandardItem(value)
                    PARAM1.appendRow(PARAM2)

        self.factors.currentIndexChanged.connect(self.updateParam1Combo)
        self.updateParam1Combo(0)
        self.factors.activated.connect(self.labelUpdate)

        # initial default values for labels
        self.paramLabel1.setText('Job Type')
        self.paramLabel2.setText('Ability')

        self.generateButton.clicked.connect(self.generateOutput)

    def labelUpdate(self):
        if self.factors.currentText() == "Quality" \
                or \
                self.factors.currentText() == "Management" \
                or \
                self.factors.currentText() == "Effort":
            self.paramLabel1.setText('Job Type')
            self.paramLabel2.setText('Ability')
        elif self.factors.currentText() == "Risk":
            self.paramLabel1.setText('Risk Impact')
            self.paramLabel2.setText('Mitigation Options')

    def updateParam1Combo(self, index):
        model_index = self.model.index(
            index, 0, self.factors.rootModelIndex()
            )
        self.parameters1.setRootModelIndex(model_index)
        self.parameters1.setCurrentIndex(0)
        self.parameters1.currentIndexChanged.connect(self.updateParam2Combo)
        self.updateParam2Combo(0)

    def updateParam2Combo(self, index):
        model_index = self.model.index(
            index, 0, self.parameters1.rootModelIndex()
            )
        self.parameters2.setRootModelIndex(model_index)
        self.parameters2.setCurrentIndex(0)

    def generateOutput(self):
        # output_text = self.factors.currentText() + " " \
        #   + self.parameters1.currentText() + " " \
        #   + self.parameters2.currentText()
        # self.outputDataLabel.setText(output_text)

        # OUTPUT DICTIONARY
        output_dictionary = {
            'Quality': Quality_Dict,
            'Management': Management_Dict,
            'Risk': Risk_Dict,
            'Effort': Effort_Dict
            }

        output_text \
            = output_dictionary\
            [self.factors.currentText()]\
            [self.parameters1.currentText()]\
            [self.parameters2.currentText()]

        self.outputDataLabel.setText(
            f'{output_text:.2f}' + " " \
                + str(self.factors.currentText()) + " units"
            )

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 2)


# FACTORS & PARAMETERS DICTIONARY
dictionary = {
    'Quality': {
        'Simple': ['Entry', 'Intermediate', 'High', 'Expert'],
        'Medium': ['Entry', 'Intermediate', 'High', 'Expert'],
        'High': ['Entry', 'Intermediate', 'High', 'Expert'],
        'Complex': ['Entry', 'Intermediate', 'High', 'Expert']
        },
    'Management': {
        'Simple': ['Entry', 'Intermediate'],
        'Medium': ['Entry', 'Intermediate', 'High', 'Expert'],
        'High': ['Entry', 'Intermediate', 'High', 'Expert'],
        'Complex': ['High', 'Expert']
        },
    'Risk': {
        'Low': ['Simple'],
        'Medium': ['Simple', 'Medium'],
        'High': ['Simple', 'Medium', 'High'],
        'NA': ['Simple', 'Medium', 'High', 'NA']
        },
    'Effort': {
        'Simple': ['Entry', 'Intermediate', 'High', 'Expert'],
        'Medium': ['Entry', 'Intermediate', 'High', 'Expert'],
        'High': ['Entry', 'Intermediate', 'High', 'Expert'],
        'Complex': ['Entry', 'Intermediate', 'High', 'Expert']
    }
}


if __name__ == '__main__':
    demoApp = QApplication([])

    widget = QtWidgets.QStackedWidget()
    first_window = ability_scaling_window()

    # debugging
    # first_window = name_of_window()

    widget.addWidget(first_window)
    widget.showMaximized()

    demoApp.exec_()