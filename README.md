## AudioBookMaker

![SampleJapanese](https://user-images.githubusercontent.com/59626117/109392666-b7d2f380-791d-11eb-980e-5792e77dbef3.PNG)

The app allows text to be transformed into sound using artificial intelligence. With the app we can, for example, create an audiobook from our own text.

The application recognises more than **170 languages**. It is currently possible to generate audio in **11 languages**:
  </br>   Arabic, 
  </br>   Portuguese, 
  </br>   Chinese, 
  </br>   Dutch, 
  </br>   English, 
  </br>   French, 
  </br>   German, 
  </br>   Italian, 
  </br>   Japanese, 
  </br>   Korean, 
  </br>   Spanish. 
  
A total of 34 voices are available, including male voices, female voices and in different accents.

## Run it yourself

* To run AudioBookMaker clone or download source code from Github. You can download it directly, or use a tool like Git-bash, tortoise git.
* Open project in PyCharm.
* Find file Credentials.py. To get the api key and url you need to register at - https://cloud.ibm.com/ and use the Text to Speech service - https://cloud.ibm.com/catalog/services/text-to-speech
```
apikey ='yourApiKeyHere'
ulr ='yourUrlHere'
```
* Check Additional libraries and complete missing libraries


## Additional libraries
* PyQt5
* ibm_watson
* docx2txt
* tkinter
* fasttext
* pdfminer

## Technologies
Project is created with:
* Python 3.8
* PyCharm
* IBM Cloud Services
