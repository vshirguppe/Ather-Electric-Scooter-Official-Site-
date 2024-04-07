import speech_recognition as sr
import smtplib
import pyaudio
import platform
import sys
from bs4 import BeautifulSoup
import email
import imaplib
from gtts import gTTS
import pyglet
import os, time
import mysql
import mysql.connector
from email.header import decode_header
import webbrowser

tts = gTTS(text="Voice based Email system for visually challenged people", lang='en')                        #First message
ttsname=("name.mp3")
tts.save(ttsname)
music = pyglet.media.load(ttsname, streaming = False)
music.play()
time.sleep(music.duration)
os.remove(ttsname)


while True:

    print("Hello. Would you like to login into the system or exit the application?")
    tts = gTTS(text="Hello. Would you like to login into the system or exit the application?", lang='en')
    ttschoice=("choice.mp3") 
    tts.save(ttschoice)

    music = pyglet.media.load(ttschoice, streaming = False)
    music.play()

    time.sleep(music.duration)
    os.remove(ttschoice)

    n = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Your choice: ")
        audio=n.listen(source)
        print ("ok done!!")

    try:
        choice=n.recognize_google(audio)
        print ("You said : "+choice)
        tts = gTTS(text=choice, lang='en')
        ttschoice=("fifth.mp3")
        tts.save(ttschoice)
        music = pyglet.media.load(ttschoice, streaming = True)
        music.play()
        time.sleep(music.duration)
        os.remove(ttschoice)
        

        
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
        choice=""
        # os.system("python composetry.py")
         
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


    if choice=="login" or choice=="Login" and choice!="":

        # nickname=""
        rname=""

        def database():
            newnickname=(nickname,)
            newrecipientname=(rname,)
            mydb=mysql.connector.connect(host="localhost",user="root",password="",database="megaprojectlogin")
            mycursor=mydb.cursor()
            query="select * from login where nickname= %s "
            mycursor.execute(query,newnickname)
            myresult=mycursor.fetchone()
            e_mail=myresult[1]
            password=myresult[2]
            security_number=myresult[3]

            mycursor1=mydb.cursor()
            query1="select * from recipient where rname= %s "
            mycursor1.execute(query1,newrecipientname)
            myresult1=mycursor1.fetchone()
            e_mail1=myresult1[1]

            return[e_mail,password,e_mail1,security_number]



        print("Enter your name:")
        tts = gTTS(text="What is your name ", lang='en')
        ttsnickname=("name.mp3") 
        tts.save(ttsnickname)

        music = pyglet.media.load(ttsnickname, streaming = False)
        music.play()

        time.sleep(music.duration)
        os.remove(ttsnickname)

        n = sr.Recognizer()
        with sr.Microphone() as source:
            print ("Your name: ")
            audio=n.listen(source)
            print ("ok done!!")

        try:
            nickname=n.recognize_google(audio)
            print ("You said : "+nickname)
            tts = gTTS(text=nickname, lang='en')
            ttsnickname=("fifth.mp3")
            tts.save(ttsnickname)
            music = pyglet.media.load(ttsnickname, streaming = True)
            music.play()
            time.sleep(music.duration)
            os.remove(ttsnickname)
            newnickname=nickname

            
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")
             
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


        print("Enter your security number:")
        tts = gTTS(text="What is your security number ? ", lang='en')
        ttsnickname=("name.mp3") 
        tts.save(ttsnickname)

        music = pyglet.media.load(ttsnickname, streaming = False)
        music.play()

        time.sleep(music.duration)
        os.remove(ttsnickname)

        n = sr.Recognizer()
        with sr.Microphone() as source:
            audio=n.listen(source)
            print ("ok done!!")

        try:
            securitynumber=n.recognize_google(audio)
            print ("Let me check.......!")
            tts = gTTS(text="Let me Check. ", lang='en')
            ttssecuritynumber=("fifth.mp3")
            tts.save(ttssecuritynumber)
            music = pyglet.media.load(ttssecuritynumber, streaming = True)
            music.play()
            time.sleep(music.duration)
            os.remove(ttssecuritynumber)
            # securitynumber=securitynumber

            
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")
             
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        nickname1=(nickname,)
        mydb=mysql.connector.connect(host="localhost",user="root",password="",database="megaprojectlogin")
        mycursor=mydb.cursor()
        query="select * from login where nickname= %s "
        mycursor.execute(query,nickname1)
        myresult=mycursor.fetchone()
        security_number=myresult[3]
        databasesecuritynumber=security_number



        if(securitynumber!=databasesecuritynumber):
            print("Sorry, Your security number is incorrect.")
            tts = gTTS(text="Sorry, Your security number is incorrect.", lang='en')
            ttsnickname=("name.mp3") 
            tts.save(ttsnickname)

            music = pyglet.media.load(ttsnickname, streaming = False)
            music.play()

            time.sleep(music.duration)
            os.remove(ttsnickname)

            

        else:
            
            tts = gTTS(text="The login was successful. What do you want to do? option 1. Compose a mail.", lang='en')
            print ("1. Compose a mail.")
            ttsname=("hello.mp3") 
            tts.save(ttsname)

            music = pyglet.media.load(ttsname, streaming = False)
            music.play()

            time.sleep(music.duration)
            os.remove(ttsname)

            print ("2. Check your inbox")
            tts = gTTS(text="option 2. Check your inbox", lang='en')
            ttsname=("second.mp3")
            tts.save(ttsname)

            music = pyglet.media.load(ttsname, streaming = False)
            music.play()

            time.sleep(music.duration)
            os.remove(ttsname)

            #this is for input choices
            tts = gTTS(text="Your choice ", lang='en')
            ttsname=("hello.mp3")
            tts.save(ttsname)

            music = pyglet.media.load(ttsname, streaming = False)
            music.play()

            time.sleep(music.duration)
            os.remove(ttsname)

            #voice recognition part
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print ("Your choice:")
                audio=r.listen(source)
                print ("ok done!!")

            try:
                text=r.recognize_google(audio)
                print ("You said : "+text)
                tts = gTTS(text=text, lang='en')
                ttsname=("fifth.mp3")
                tts.save(ttsname)
                music = pyglet.media.load(ttsname, streaming = False)
                music.play()
                time.sleep(music.duration)
                os.remove(ttsname)

                
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio.")
                 
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))


             

            if text == '1' or text == 'One' or text == 'one'or text == 'van' or text=='when':
                print("Whom do you want to send the mail?")
                tts = gTTS(text="Whom do you want to send the mail ", lang='en')
                ttsrname=("rname.mp3") 
                tts.save(ttsrname)

                music = pyglet.media.load(ttsrname, streaming = False)
                music.play()

                time.sleep(music.duration)
                os.remove(ttsrname)

                m = sr.Recognizer()
                with sr.Microphone() as source:
                    print ("Your input: ")
                    audio=m.listen(source)
                    print ("ok done!!")

                try:
                    rname=m.recognize_google(audio)
                    print ("You said : "+rname)
                    tts = gTTS(text=rname, lang='en')
                    ttsrname=("chai.mp3")
                    tts.save(ttsrname)
                    music = pyglet.media.load(ttsrname, streaming = False)
                    music.play()
                    time.sleep(music.duration)
                    os.remove(ttsrname)


                    
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio.")
                     
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))




                r = sr.Recognizer() 
                with sr.Microphone() as source:
                    print ("Your message :")
                    tts = gTTS(text="Your message", lang='en')
                    ttsname=("sixth.mp3")
                    tts.save(ttsname)
                    music = pyglet.media.load(ttsname, streaming = False)
                    music.play()
                    time.sleep(music.duration)
                    os.remove(ttsname)
                    audio=r.listen(source)
                    print ("ok done!!")
                    
                try:
                    text1=r.recognize_google(audio)
                    print ("You said : "+text1)
                    tts = gTTS(text="You said."+text1, lang='en')
                    ttsname=("fourth.mp3")
                    tts.save(ttsname)
                    music = pyglet.media.load(ttsname, streaming = False)
                    music.play()
                    time.sleep(music.duration)
                    os.remove(ttsname)
                    tts = gTTS(text="Should I confirm the message or you want to change it ?", lang='en')
                    ttsname=("fourth.mp3")
                    tts.save(ttsname)
                    music = pyglet.media.load(ttsname, streaming = False)
                    music.play()
                    time.sleep(music.duration)
                    os.remove(ttsname)


                    n = sr.Recognizer()
                    with sr.Microphone() as source:
                        print ("Your choice: ")
                        audio=n.listen(source)
                        print ("ok done!!")

                    try:
                        response=n.recognize_google(audio)
                        # print ("You said : "+response)
                        tts = gTTS(text=response, lang='en')
                        ttsnickname=("fifth.mp3")
                        tts.save(ttsnickname)
                        music = pyglet.media.load(ttsnickname, streaming = True)
                        # music.play()
                        time.sleep(music.duration)
                        os.remove(ttsnickname)
                        

                        
                    except sr.UnknownValueError:
                        print("Google Speech Recognition could not understand audio.")
                         
                    except sr.RequestError as e:
                        print("Could not request results from Google Speech Recognition service; {0}".format(e))


                    if(response=="Confirm" or response=="confirm" or response=="Yes" or response=="yes"):
                        msg=text1

                    else:
                        tts = gTTS(text="Okay. What is your new message?", lang='en')
                        ttsnickname=("fifth.mp3")
                        tts.save(ttsnickname)
                        music = pyglet.media.load(ttsnickname, streaming = True)
                        music.play()
                        time.sleep(music.duration)
                        os.remove(ttsnickname)

                        n = sr.Recognizer()
                        with sr.Microphone() as source:
                            print ("Your message: ")
                            audio=n.listen(source)
                            print ("ok done!!")

                        newresponse=n.recognize_google(audio)
                        print ("You said : "+newresponse)
                        tts = gTTS(text=newresponse, lang='en')
                        ttsnickname=("fifth.mp3")
                        tts.save(ttsnickname)
                        music = pyglet.media.load(ttsnickname, streaming = True)
                        music.play()
                        time.sleep(music.duration)
                        os.remove(ttsnickname)
                        msg=newresponse



                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio.")
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))


                l=database();
                e_mail=l[0]
                password=l[1]
                e_mail1=l[2]



                mail = smtplib.SMTP('smtp.gmail.com',587)
                mail.ehlo()  
                mail.starttls()
                mail.login(e_mail,password) 
                mail.sendmail(e_mail,e_mail1,msg) 
                print ("Congrats! Your mail has been sent. ")
                tts = gTTS(text="Congrats! Your mail has been sent and you have been successfully logged out of your email service. ", lang='en')
                ttsname=("send.mp3")
                tts.save(ttsname)
                music = pyglet.media.load(ttsname, streaming = False)
                music.play()
                time.sleep(music.duration)
                os.remove(ttsname)
                mail.close()  

                
            if text == '2' or text == 'tu' or text == 'two' or text == 'Tu' or text == 'to' or text == 'Too' or text=='Vivek' or text=='inbox' or text=='Thu' or text=='Two' :

                newnickname=(nickname,)
                mydb=mysql.connector.connect(host="localhost",user="root",password="",database="megaprojectlogin")
                mycursor=mydb.cursor()
                query="select * from login where nickname= %s "
                mycursor.execute(query,newnickname)
                myresult=mycursor.fetchone()
                e_mail=myresult[1]
                password=myresult[2]



                mail = imaplib.IMAP4_SSL('imap.gmail.com',993)  
                mail.login(e_mail,password)  
                status,total = mail.select('Inbox')
                total=int(total[0]) 
                print ("Number of mails in your inbox :"+str(total))
                tts = gTTS(text="Total mails are :"+str(total), lang='en') 
                ttsname=("total.mp3")
                tts.save(ttsname)
                music = pyglet.media.load(ttsname, streaming = False)
                music.play()
                time.sleep(music.duration)
                os.remove(ttsname)
                
                
                unseen = mail.search(None, 'UnSeen')

                # print ("Number of UnSeen mails :"+str(unseen))
                list1=unseen[1]
                list1=list1[0]
                list1=list1.decode("utf-8")

                a_string =list1
                a_list = a_string.split()
                map_object = map(int, a_list)

                list_of_integers = list(map_object)
                N=len(list_of_integers)
                print ("Number of UnSeen mails :"+str(N))
                tts = gTTS(text="Your Unseen mail :"+str(N), lang='en')
                ttsname=("unseen.mp3")
                tts.save(ttsname)
                music = pyglet.media.load(ttsname, streaming = False)
                music.play()
                time.sleep(music.duration)
                os.remove(ttsname)

                finaltext=""

                status, messages = mail.select("INBOX")
                

                # total number of emails
                messages = int(messages[0])

                # N=3                                                                                     # number of top emails to fetch
                if(N!=0):
                    for i in range(total,total-N, -1):
                        
                        res, msg = mail.fetch(str(i), "(RFC822)")                                       # fetch the email message by ID
                        for response in msg:
                            if isinstance(response, tuple):
                                
                                msg = email.message_from_bytes(response[1])                             # parse a bytes email into a message object
                                # decode the email subject
                                try:
                                    subject, encoding = decode_header(msg["Subject"])[0]
                                except:
                                    pass
                                if isinstance(subject, bytes):
                                    
                                    subject = subject.decode(encoding)                                  # if it's a bytes, decode to str
                                # decoding the sender's email address
                                From, encoding = decode_header(msg.get("From"))[0]
                                if isinstance(From, bytes):
                                    From = From.decode(encoding)
                                print("From:", From)
                                print("Subject:", subject)
                                finaltext=finaltext+"From :" +From
                                finaltext=finaltext+". The subject is: "+subject
                                
                                # if the email message is multipart
                                if msg.is_multipart():
                                    # iterate over email parts
                                    for part in msg.walk():
                                        # extract content type of email
                                        content_type = part.get_content_type()                                          #returns text/plain if only plain text is there
                                        content_disposition = str(part.get("Content-Disposition"))                      #returns attachment,filename if it is multipart
                                        try:
                                            # get the email body
                                            body = part.get_payload(decode=True).decode()
                                        except:
                                            pass
                                        if content_type == "text/plain" and "attachment" not in content_disposition:
                                            # print text/plain emails and skip attachments
                                            print(body)
                                            finaltext=finaltext+". The body is: " +body+". Next mail is "
                                        
                                else:
                                    # extract content type of email
                                    content_type = msg.get_content_type()
                                    # get the email body
                                    body = msg.get_payload(decode=True).decode()
                                    if content_type == "text/plain":
                                        # print only text email parts
                                        print(body)
                                        finaltext=finaltext+". The body is : " +body+". Next mail is "
                            
                                print("="*100)
                

                if(N==0):

                    print ("Hello, currently there are no unread messages in your inbox.")
                    unreadmsg="Hello, currently there are no unread messages in your inbox."
                    tts = gTTS(text=""+unreadmsg, lang='en') 
                    ttsname=("unread.mp3")
                    tts.save(ttsname)
                    music = pyglet.media.load(ttsname, streaming = False)
                    music.play()
                    time.sleep(music.duration)
                    os.remove(ttsname)

                
                
                
                try:
                    tts = gTTS(finaltext, lang='en')
                    ttsname=("body.mp3") 
                    tts.save(ttsname)
                    music = pyglet.media.load(ttsname, streaming = False)
                    music.play()
                    time.sleep(music.duration)
                    os.remove(ttsname)

                except:
                    pass
                mail.close()
                mail.logout()




    if choice=="exit" or choice=="Exit" or choice=="Close" or choice=="close" and choice!="":
        break

    if choice=="":
        pass



