import os
from os.path import join
import speech_recognition as sr
from gtts import gTTS
from time import sleep
from translate import Translator 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def googlespeak(x):
    tts=gTTS(str(x))
    tts.save('source.mp3')
    os.system("start source.mp3")



languages={'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}
mailids={'a':'abc@gmail.com','b':'uthej2001@gmail.com','c':'pqr@gmail.com','d':'xyz@gmail.com'}
mic=sr.Microphone(device_index=1)
record=sr.Recognizer()
record.energy_threshold=5000

print("Natural Language Processing Model for Visually Challenged or illiterates")


with mic as source:

    #Source Language
    while(1):
        s="Enter Source Language"
        print(s)
        googlespeak(s)
        sleep(3)
        record.adjust_for_ambient_noise(source,duration=0.2)
        audio=record.listen(source)
        try:
            text=record.recognize_google(audio)
            print("you said : {}".format(text))
            if((str(text)).lower() in languages.keys()):
                source_lang=languages[(str(text)).lower()]
                #print(source_lang)
                googlespeak("Your source language is set to "+ (str(text)).lower() )
                break
            break
        except:
            print("Sorry,I Could not recognize that, please try again")


    sleep(3)

    #Target Language
    while(1):
        d="Enter Destination Language"
        print(d)
        googlespeak(d)
        sleep(3)
        audio=record.listen(source)
        try:
            text=record.recognize_google(audio)
            print("you said : {}".format(text))
            if((str(text)).lower() in languages.keys()):
                destination_lang=languages[(str(text)).lower()]
                #print(destination_lang)
                googlespeak("Your Target language is set to "+ (str(text)).lower() )
                sleep(3)
                break
            break
        except:
            print("Sorry,I Could not recognize that, please try again")


    sleep(3)

    #Tranlation
    while(1):
        s="Sentence to be translated"
        print(s)
        googlespeak(s)
        sleep(3)
        record.adjust_for_ambient_noise(source,duration=0.2)
        audio=record.listen(source)
        try:
            textt=record.recognize_google(audio)
            print("phrase to be translated : "+ textt)
            translator= Translator(from_lang=str(source_lang),to_lang=str(destination_lang))
            translation = translator.translate(str(textt))
            print(translation)
            break
        except sr.UnknownValueError:
            print("Unable to Understand the Input")

    # Saving the Transalted text into text file
    file1= open(r'C:\Users\UTHEJ\Desktop\NLPproject\TranslatedText.txt','w') #Path
    file1.write(translation)
    file1.close()
    googlespeak("Translation is done and the text file is saved")
    sleep(5)

    while(1):
        m="Do you want to send a mail?"
        print(m)
        googlespeak(m)
        sleep(1)
        record.adjust_for_ambient_noise(source,duration=0.5)
        audio=record.listen(source)
        text=record.recognize_google(audio)
        print("you said : {}".format(text))

        try:
            if((str(text)).lower()=='yes'):
                di="Select mail ID from Dictionary"
                print(di)
                googlespeak(di)
                sleep(2)
                record.adjust_for_ambient_noise(source,duration=0.5)
                audio=record.listen(source)
                #sleep(1)
                text=record.recognize_google(audio)
                print("you said : {}".format(text))
                if((str(text)).lower() in mailids.keys()):
                    receive_address=mailids[(str(text)).lower()]
                    print("you said : {}".format(receive_address))
                    googlespeak(receive_address)
                    break
                break
            else:
                break
        except:
            print("Sorry,I Could not recognize that, please try again")



    #SENDING MAIL

    content_of_the_mail = "Hello " + str(receive_address) + " Please find the attached text file. Thank you!"

    sender_address = 'lightningc20@gmail.com' #From Address
    sender_password = 'Qwerty@123$'               #Sender Password
    receiver_address = str(receive_address) #Receiver Address
    message = MIMEMultipart()
    message['From'] = sender_address   
    message['To'] = receiver_address 
    message['Subject'] = 'Translation Mail. It has an attachment.' #The subject line
    
    #The body and the attachments
    message.attach(MIMEText(content_of_the_mail, 'plain'))
    file_to_be_attached = open(r'C:\Users\UTHEJ\Desktop\NLPproject\TranslatedText.txt', 'rb') # Open the file as binary mode
    load = MIMEBase('application', 'octate-stream')
    load.set_payload((file_to_be_attached).read())
    encoders.encode_base64(load) #encode the attachment
    load.add_header('Content-Decomposition', 'attachment', filename=r'C:\Users\UTHEJ\Desktop\eduternintern\TranslatedText.txt')
    message.attach(load)

    #SMTP for sending the mail
    ses = smtplib.SMTP('smtp.gmail.com', 587) 
    ses.starttls() 
    ses.login(sender_address, sender_password) 
    text = message.as_string()
    ses.sendmail(sender_address, receiver_address, text)
    ses.quit()

    mailsent="The mail has been sent successfully"
    print(mailsent)
    googlespeak(mailsent)
    


