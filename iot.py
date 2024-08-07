"""from subprocess import check_output"""
import subprocess
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import drivers
from time import sleep
import os.path
display = drivers.Lcd()
print(os.path.abspath(subprocess.__file__))

# Fetch the service account key JSON file contents

cred = credentials.Certificate('PATH/TO/CREDENTIALS.json')


n = 0

def est_connecte(n):
    
    """try:"""
    test = 0
        # Check for the presence of "CYP-WIFI2" in the list of Wi-Fi networks
    """"iwlist","""
    try:
        
        scanoutput = subprocess.check_output([ "/usr/sbin/iwlist","wlan0", "scan"]).decode('utf-8')
    except:
        display.lcd_display_string("erreur fetch wifi", 1)
        scanout = ""
        print("erreur retour wifi")
    """print(scanoutput)"""
    if "PHONE_HOTSPOT" in scanoutput:
        if n ==0 :
            """display.lcd_display_string("fetching", 1)"""
            firebase_admin.initialize_app(cred)
                
            sleep(1)
        else: 
            """display.lcd_display_string("pqs de fetch", 1)"""
            # Create a Firestore client
        try :
            """display.lcd_display_string("1", 2)"""
            db = firestore.client()
            """display.lcd_display_string("2", 2)"""
            # Reference to the "messages" collection
            messages_ref = db.collection('messages')
            print(messages_ref)
            """display.lcd_display_string("3", 2)"""
            # Get all documents in the "messages" collection
            docs = messages_ref.stream()
            """display.lcd_display_string("4", 2)"""
            # Iterate through the documents and print their data
            
            for doc in docs:
                data = doc.to_dict()
                print(data)
                message = data['text']
                print(message)
                scroll_text(message)
            """except:
                display.lcd_display_string("F", 2)"""
                    
        except :
            """display.lcd_display_string("5", 1)"""
            print("deco")
            test =0
        sleep(1)
        display.lcd_display_string( "connecte!", 1)
        sleep(1)
            #display.lcd_clear()
        if test == 0 :
            return True
        else :
            return False
    else:
        display.lcd_display_string(str(n) +"deco!", 1)
        sleep(1)
            #display.lcd_clear()
        return False
    """except OSError:"""
    """display.lcd_display_string(str(n) + "je suis deconnecte!", 1)"""
    sleep(1)
        #display.lcd_clear()
    return False
        

# Using the function to check the Internet connection

def scroll_text(message):
    if len(message) <= 16:
        display.lcd_display_string(message, 2)  # If message fits the display, show it as is
    else:
        while True:
            for i in range(len(message) - 15):  # Scroll through the message
                display.lcd_display_string(message[i:i+16], 2)
                sleep(0.5)  # Adjust scroll speed if necessary
            sleep(2)  # Wait a bit before repeating the scroll


# Execute the function every 5 seconds in a loop
while True:
    """display.lcd_display_string("wsh", 2)"""

    if est_connecte(n):
        print("Vous êtes connecté à Internet.")
        n += 1
    else:
        print("Vous n'êtes pas connecté à Internet.")
        
    time.sleep(1)  # Adjust the interval as needed