import  pyttsx3
import time

engine = pyttsx3.init(driverName='sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def main():
    
    def talk(text):
        engine.say(text)
        engine.runAndWait()
        engine.stop()
        
        
        
        
    
    talk("Enter Email Address")
    email = input(": ")
    while email.lower() != "no":
        if "@" in email and "." in email:

            (userName,domain) = email.split("@")
            (domain,extension) = domain.split (".")

            print(userName)
            print(domain)
            print(extension)

            # Call the function and pass the text you want to convert to speech
            talk("Your username is " +  userName)   
            talk("The domain you use is " + domain)
            talk("The extension of the email address is dot " + extension)
            talk("Those are the spliced parts of your email address")
            time.sleep(3)
            talk("Enter Email Address")
            email = input(": ")
            if email.lower() == "no":
                talk("What else do you need")
            else:()
            
            
                    
        
            
        else:
            print("Invalid Email")
