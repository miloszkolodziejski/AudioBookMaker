from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import Credentials as cr
import fileManager
import voiceList


def convert_audio(text, voice, language):
    authenticator = IAMAuthenticator(cr.apikey)
    tts = TextToSpeechV1(authenticator=authenticator)
    tts.set_service_url(cr.ulr)

    voiceName = None
    outputFileName = fileManager.saveFile()

    if language == 'Arabic':
        voiceName = voiceList.Arabic.get(voice)
    if language == 'Portuguese':
        voiceName = voiceList.Portuguese.get(voice)
    if language == 'Chinese':
        voiceName = voiceList.Chinese.get(voice)
    if language == 'Dutch':
        voiceName = voiceList.Dutch.get(voice)
    if language == 'English':
        voiceName = voiceList.English.get(voice)
    if language == 'French':
        voiceName = voiceList.French.get(voice)
    if language == 'German':
        voiceName = voiceList.German.get(voice)
    if language == 'Italian':
        voiceName = voiceList.Italian.get(voice)
    if language == 'Japanese':
        voiceName = voiceList.Japanese.get(voice)
    if language == 'Korean':
        voiceName = voiceList.Korean.get(voice)
    if language == 'Spanish':
        voiceName = voiceList.Korean.get(voice)

    with open(outputFileName, 'wb') as audio_file:
        res = tts.synthesize(text, accept='audio/mp3', voice=voiceName, ).get_result()
        audio_file.write(res.content)
