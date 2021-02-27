import fasttext
import voiceList


def languageDetect(text):
    pretrained_lang_model = "./tmp/lid.176.ftz"
    model = fasttext.load_model(pretrained_lang_model)
    predictions = model.predict(text=text)
    language = predictions[0][0]

    return voiceList.languages.get(language[9:len(language)], language[9:len(language)] + " not supported!")
