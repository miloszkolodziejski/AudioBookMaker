import docx2txt
import os


def convert_doc(docFile):
    filename = os.path.basename(docFile)
    text = docx2txt.process(docFile)
    outputFileName = 'temp' + filename + '.txt'
    print(outputFileName)

    with open(outputFileName, "w", encoding='utf-8') as f:
        f.write(text)
    return outputFileName
