import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import io
import os

def convert_pdf(pdfFile):
    try:
        inputPdfFile = open(pdfFile, 'rb')
        resourceManager = PDFResourceManager()
        resourceData = io.StringIO()
        filename = os.path.basename(pdfFile)

        textConverter = TextConverter(resourceManager, resourceData, laparams=LAParams())
        interpreter = PDFPageInterpreter(resourceManager, textConverter)

        outputFileName = 'temp' + filename + '.txt'
        print(outputFileName)

        for page in PDFPage.get_pages(inputPdfFile):
            interpreter.process_page(page)
            txt = resourceData.getvalue()
            with open(outputFileName, 'w', encoding='utf-8') as f:
                f.write(txt)

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
    return outputFileName
