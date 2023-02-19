# Form implementation generated from reading ui file '.\benkpress\ui\newsession.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_NewSessionDialog(object):
    def setupUi(self, NewSessionDialog):
        NewSessionDialog.setObjectName("NewSessionDialog")
        NewSessionDialog.resize(464, 617)
        self.verticalLayout = QtWidgets.QVBoxLayout(NewSessionDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.general_settings_group = QtWidgets.QGroupBox(parent=NewSessionDialog)
        self.general_settings_group.setObjectName("general_settings_group")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.general_settings_group)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=self.general_settings_group)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.sample_folder_path_line_edit = PathEdit(parent=self.general_settings_group)
        self.sample_folder_path_line_edit.setProperty("folder", True)
        self.sample_folder_path_line_edit.setObjectName("sample_folder_path_line_edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.sample_folder_path_line_edit)
        self.label_2 = QtWidgets.QLabel(parent=self.general_settings_group)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.page_filter_combo_box = PageFilterBox(parent=self.general_settings_group)
        self.page_filter_combo_box.setObjectName("page_filter_combo_box")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.page_filter_combo_box)
        self.label_3 = QtWidgets.QLabel(parent=self.general_settings_group)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.pipeline_combo_box = PipelineBox(parent=self.general_settings_group)
        self.pipeline_combo_box.setObjectName("pipeline_combo_box")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.pipeline_combo_box)
        self.label_6 = QtWidgets.QLabel(parent=self.general_settings_group)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.file_target_radio_button = QtWidgets.QRadioButton(parent=self.general_settings_group)
        self.file_target_radio_button.setObjectName("file_target_radio_button")
        self.target_button_group = QtWidgets.QButtonGroup(NewSessionDialog)
        self.target_button_group.setObjectName("target_button_group")
        self.target_button_group.addButton(self.file_target_radio_button)
        self.verticalLayout_4.addWidget(self.file_target_radio_button)
        self.page_target_radio_button = QtWidgets.QRadioButton(parent=self.general_settings_group)
        self.page_target_radio_button.setObjectName("page_target_radio_button")
        self.target_button_group.addButton(self.page_target_radio_button)
        self.verticalLayout_4.addWidget(self.page_target_radio_button)
        self.sentence_target_radio_button = QtWidgets.QRadioButton(parent=self.general_settings_group)
        self.sentence_target_radio_button.setChecked(True)
        self.sentence_target_radio_button.setObjectName("sentence_target_radio_button")
        self.target_button_group.addButton(self.sentence_target_radio_button)
        self.verticalLayout_4.addWidget(self.sentence_target_radio_button)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.verticalLayout_4)
        self.label_7 = QtWidgets.QLabel(parent=self.general_settings_group)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.spacy_model_combo_box = SpacyModelsBox(parent=self.general_settings_group)
        self.spacy_model_combo_box.setObjectName("spacy_model_combo_box")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.spacy_model_combo_box)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.verticalLayout.addWidget(self.general_settings_group)
        self.reader_settings_group = QtWidgets.QGroupBox(parent=NewSessionDialog)
        self.reader_settings_group.setObjectName("reader_settings_group")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.reader_settings_group)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_4 = QtWidgets.QLabel(parent=self.reader_settings_group)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(parent=self.reader_settings_group)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.poppler_dpi_spin_box = QtWidgets.QSpinBox(parent=self.reader_settings_group)
        self.poppler_dpi_spin_box.setMinimum(72)
        self.poppler_dpi_spin_box.setMaximum(300)
        self.poppler_dpi_spin_box.setSingleStep(10)
        self.poppler_dpi_spin_box.setProperty("value", 120)
        self.poppler_dpi_spin_box.setObjectName("poppler_dpi_spin_box")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.poppler_dpi_spin_box)
        self.reader_combo_box = ReaderBox(parent=self.reader_settings_group)
        self.reader_combo_box.setObjectName("reader_combo_box")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.reader_combo_box)
        self.poppler_path_line_edit = PathEdit(parent=self.reader_settings_group)
        self.poppler_path_line_edit.setProperty("folder", True)
        self.poppler_path_line_edit.setObjectName("poppler_path_line_edit")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.poppler_path_line_edit)
        self.tesseract_path_line_edit = PathEdit(parent=self.reader_settings_group)
        self.tesseract_path_line_edit.setObjectName("tesseract_path_line_edit")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.tesseract_path_line_edit)
        self.label_8 = QtWidgets.QLabel(parent=self.reader_settings_group)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(parent=self.reader_settings_group)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_9)
        self.label_10 = QtWidgets.QLabel(parent=self.reader_settings_group)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_10)
        self.tesseract_language_line_edit = QtWidgets.QLineEdit(parent=self.reader_settings_group)
        self.tesseract_language_line_edit.setObjectName("tesseract_language_line_edit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.tesseract_language_line_edit)
        self.verticalLayout_3.addLayout(self.formLayout_2)
        self.verticalLayout.addWidget(self.reader_settings_group)
        self.dialog_button_box = QtWidgets.QDialogButtonBox(parent=NewSessionDialog)
        self.dialog_button_box.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.dialog_button_box.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.dialog_button_box.setObjectName("dialog_button_box")
        self.verticalLayout.addWidget(self.dialog_button_box)

        self.retranslateUi(NewSessionDialog)
        QtCore.QMetaObject.connectSlotsByName(NewSessionDialog)

    def retranslateUi(self, NewSessionDialog):
        _translate = QtCore.QCoreApplication.translate
        NewSessionDialog.setWindowTitle(_translate("NewSessionDialog", "New session"))
        self.general_settings_group.setTitle(_translate("NewSessionDialog", "General Settings"))
        self.label.setText(_translate("NewSessionDialog", "Sample folder"))
        self.label_2.setText(_translate("NewSessionDialog", "Page filter"))
        self.label_3.setText(_translate("NewSessionDialog", "Pipeline"))
        self.label_6.setText(_translate("NewSessionDialog", "Target"))
        self.file_target_radio_button.setText(_translate("NewSessionDialog", "File"))
        self.page_target_radio_button.setText(_translate("NewSessionDialog", "Page"))
        self.sentence_target_radio_button.setText(_translate("NewSessionDialog", "Sentence"))
        self.label_7.setText(_translate("NewSessionDialog", "Spacy model"))
        self.reader_settings_group.setTitle(_translate("NewSessionDialog", "PDF Reader Settings"))
        self.label_4.setText(_translate("NewSessionDialog", "Reader"))
        self.label_5.setText(_translate("NewSessionDialog", "DPI"))
        self.label_8.setText(_translate("NewSessionDialog", "Language"))
        self.label_9.setText(_translate("NewSessionDialog", "Poppler path"))
        self.label_10.setText(_translate("NewSessionDialog", "Tesseract path"))
        self.tesseract_language_line_edit.setText(_translate("NewSessionDialog", "eng"))
from benkpress.widget import PageFilterBox, PathEdit, PipelineBox, ReaderBox, SpacyModelsBox
