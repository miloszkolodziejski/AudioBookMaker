import os
import sys
import fileManager
from app import app
import pdfConversion
import docConversion
import languageDetector
import voiceList
import audioConversion


class buttonController:
    def __init__(self, obj):
        self.tempFile = None
        self.obj = obj
        self.apk = app()

    def browseClick(self):
        try:
            self.apk.inputFilePath = fileManager.openFile()

            if self.apk.inputFilePath != '':
                self.obj.fileName.setText(self.apk.inputFilePath)

                if self.apk.inputFilePath.endswith('.pdf'):
                    self.apk.extension = '.pdf'
                    self.apk.tempTxtFilePath = pdfConversion.convert_pdf(self.apk.inputFilePath)
                if self.apk.inputFilePath.endswith('.docx'):
                    self.apk.extension = '.docx'
                    self.apk.tempTxtFilePath = docConversion.convert_doc(self.apk.inputFilePath)
                if self.apk.inputFilePath.endswith('.txt'):
                    self.apk.extension = '.txt'
                    self.apk.tempTxtFilePath = self.apk.inputFilePath

                textBrowser = ""

                with open(self.apk.tempTxtFilePath, 'r', encoding='utf-8') as f:
                    self.tempFile = f.readlines()

                for text in self.tempFile:
                    textBrowser += text

                self.obj.textBrowser.setPlainText(textBrowser)

                self.tempFile = [line.replace('\n', '') for line in self.tempFile]
                self.tempFile = ''.join(str(line) for line in self.tempFile)
                language = languageDetector.languageDetect(self.tempFile)

                self.obj.languageLabel.setText(language)
                self.apk.language = language
                if language.endswith('!'):
                    self.apk.ableToConvert = False
                else:
                    self.apk.ableToConvert = True

            print(self.apk.language)

            try:
                self.obj.LanguageComboBox.clear()
                if self.apk.language == 'Arabic':
                    self.obj.LanguageComboBox.addItems(voiceList.Arabic)
                if self.apk.language == 'Portuguese':
                    self.obj.LanguageComboBox.addItems(voiceList.Portuguese)
                if self.apk.language == 'Chinese':
                    self.obj.LanguageComboBox.addItems(voiceList.Chinese)
                if self.apk.language == 'Dutch':
                    self.obj.LanguageComboBox.addItems(voiceList.Dutch)
                if self.apk.language == 'English':
                    self.obj.LanguageComboBox.addItems(voiceList.English)
                if self.apk.language == 'French':
                    self.obj.LanguageComboBox.addItems(voiceList.French)
                if self.apk.language == 'German':
                    self.obj.LanguageComboBox.addItems(voiceList.German)
                if self.apk.language == 'Italian':
                    self.obj.LanguageComboBox.addItems(voiceList.Italian)
                if self.apk.language == 'Japanese':
                    self.obj.LanguageComboBox.addItems(voiceList.Japanese)
                if self.apk.language == 'Korean':
                    self.obj.LanguageComboBox.addItems(voiceList.Korean)
                if self.apk.language == 'Spanish':
                    self.obj.LanguageComboBox.addItems(voiceList.Spanish)

            except Exception as e:
                print("type error: " + str(e))

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)

    def convertClick(self):
        if self.apk.ableToConvert:
            try:
                print(self.tempFile)
                audioConversion.convert_audio(self.tempFile, self.obj.LanguageComboBox.currentText(), self.apk.language)
            except Exception as e:
                print("type error: " + str(e))
        try:
            os.remove('temp' + os.path.basename(self.apk.inputFilePath) + '.txt')
        except Exception as e:
            print("type error: " + str(e))
