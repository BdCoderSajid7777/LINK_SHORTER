import sys
import time
import pyshorteners

username = "sajid"
password = "1234"

def end():
  sajid = input()
  sys.exit()
def animated(text):
  for x in text:
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.005)
givenUsername = input("\033[0;34mEnter your username: ")
if givenUsername == username:
  print("\033[0;32mCorrect username")
  givenPassword = input("\033[0;34mEnter your password: ")
  if givenPassword:
    print("\033[0;32mWELCOME TO THIS TOOL")
  else:
    print("\033[0;31mWrong password")
    time.sleep(1)
    print("Press enter to exit")
    end()

else:
  print("\033[0;31mWrong User")
  time.sleep(1)
  print("Press enter to exit")
  end()
logo = '''

\033[0;33m$$\       $$$$$$\ $$\   $$\ $$\   $$\        $$$$$$\  $$\   $$\  $$$$$$\  $$$$$$$\ $$$$$$$$\ $$$$$$$$\ $$$$$$$\  
$$ |      \_$$  _|$$$\  $$ |$$ | $$  |      $$  __$$\ $$ |  $$ |$$  __$$\ $$  __$$\\__$$  __|$$  _____|$$  __$$\ 
$$ |        $$ |  $$$$\ $$ |$$ |$$  /       $$ /  \__|$$ |  $$ |$$ /  $$ |$$ |  $$ |  $$ |   $$ |      $$ |  $$ |
$$ |        $$ |  $$ $$\$$ |$$$$$  /        \$$$$$$\  $$$$$$$$ |$$ |  $$ |$$$$$$$  |  $$ |   $$$$$\    $$$$$$$  |
$$ |        $$ |  $$ \$$$$ |$$  $$<          \____$$\ $$  __$$ |$$ |  $$ |$$  __$$<   $$ |   $$  __|   $$  __$$< 
$$ |        $$ |  $$ |\$$$ |$$ |\$$\        $$\   $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |  $$ |   $$ |      $$ |  $$ |
$$$$$$$$\ $$$$$$\ $$ | \$$ |$$ | \$$\       \$$$$$$  |$$ |  $$ | $$$$$$  |$$ |  $$ |  $$ |   $$$$$$$$\ $$ |  $$ |
\________|\______|\__|  \__|\__|  \__|       \______/ \__|  \__| \______/ \__|  \__|  \__|   \________|\__|  \__|
                                      
'''

animated(logo)

link = input("\033[0;34mEnter your link here: ")
s = pyshorteners.Shortener()
provide = s.tinyurl.short(link)

print(f"Your short link is : {provide}")
