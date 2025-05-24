import os
import shutil
import subprocess
import time
from colorama import init,Fore, Back, Style
## Add a counter to check out of X how much passed and how much failed

TOTAL_TASKS = 5
CHARACTER_TEXT_COLOR= Fore.YELLOW
SYSTEM_TEXT_COLOR = Fore.WHITE
tasks_failed = []
tasks_passed = []

CHARACTER_NAME = "Momo"

## SFC - Passed
## CHKDSK - Failed


def banner():

    init()
    print(r"""
_________                               __                 ___________.__                     
\_   ___ \  ____   _____ ______  __ ___/  |_  ___________  \_   _____/|__|__  ___ ___________ 
/    \  \/ /  _ \ /     \\____ \|  |  \   __\/ __ \_  __ \  |    __)  |  \  \/  // __ \_  __ \
\     \___(  <_> )  Y Y  \  |_> >  |  /|  | \  ___/|  | \/  |     \   |  |>    <\  ___/|  | \/
 \______  /\____/|__|_|  /   __/|____/ |__|  \___  >__|     \___  /   |__/__/\_ \\___  >__|   
        \/             \/|__|                    \/             \/             \/    \/       
""")

def description():
    display_text_letter_by_letter(
        CHARACTER_TEXT_COLOR + '\n' + CHARACTER_NAME + ': Hi there! I’m ' + CHARACTER_NAME + ', your friendly digital assistant! ✨\n'+CHARACTER_NAME+': I’m here to make sure your computer is feeling its best. ♪\n\n( ´ ▽ ` )ﾉ\n\n'+CHARACTER_NAME+': Let’s make your computer super sparkly and fix any problems it might have. Shall we? ✩')
def features():
    display_text_letter_by_letter(
        CHARACTER_NAME + ": Okay, let’s make your computer super speedy! ⚡\n"+CHARACTER_NAME+": Don’t worry if you don’t understand everything. I’m here to help! ♪\n\n"+CHARACTER_NAME+" is on the case! (ﾉ◕ヮ◕)ﾉ\n\n"+ CHARACTER_NAME + ": Here’s what i’ll do:\n\n"+SYSTEM_TEXT_COLOR+"1. ✨ SFC Scan ✨\n2. 🧹 CHKDSK Scan 🧹\n3. 💿 Defragment of Drives 💿\n4. 🗑️ Deleting Temp File 🗑️")
def display_report():
    print(Fore.LIGHTGREEN_EX+"""
           +------------------------------------+
           |             REPORT                 |
           +------------------------------------+
                   """)
    print(SYSTEM_TEXT_COLOR)
    for x in tasks_passed:
        display_text_letter_by_letter(f"| {x:<20} | PASSED |")
    for x in tasks_failed:
        display_text_letter_by_letter(f"| {x:<20} | FAILED |")

    print("+------------------------------------+")

def permission():
    display_text_letter_by_letter(
        "\n" + CHARACTER_TEXT_COLOR + CHARACTER_NAME + ": Ok! " + CHARACTER_NAME + " has told you everything that she will do for you!\n" + CHARACTER_NAME + ": Now I would like your permission to proceed.\n")

    while True:
        display_text_letter_by_letter(SYSTEM_TEXT_COLOR + "SYSTEM: Please enter (Y/N)")
        answer = str(input("> ")).lower()

        if answer == "y":
            sfc_scan_now()
            chkdsk()
            defragment()
            temp_delete()
            display_report()
            display_text_letter_by_letter("\nThank you so much for using momo! Momo hopes you come back to use my services. Thank you!\nPROGRAM ENDED...\n")
            break
        elif answer == "n":
            display_text_letter_by_letter(
                CHARACTER_TEXT_COLOR + "\n" + CHARACTER_NAME + ': Momo is sad! 😢\n' + CHARACTER_NAME + ': All I want to do is help you! 🥺\n' + CHARACTER_NAME + ': If you want my help, please restart the program. 😤')
            return -1
        else:
            display_text_letter_by_letter(CHARACTER_TEXT_COLOR+"\n"+CHARACTER_NAME+": Heeeyyyy! What are you typing! I said Y or N!\n"+CHARACTER_NAME+": Follow the rules!\n(;__;)\n"+SYSTEM_TEXT_COLOR)
def get_current_username():
    try:
        return str(os.getlogin()).lower() # Gets the users name.
    except Exception as e:
        return e

def divider():
    print("\n===============================================================\n")

def temp_delete():
        divider()
        print(Fore.LIGHTGREEN_EX+"""
                +------------------------------------+
                |       BEGINNING TEMP DELETE        |
                +------------------------------------+
                        """)
        display_text_letter_by_letter(CHARACTER_TEXT_COLOR+ CHARACTER_NAME+ ": Ok now time for deleting those useless temporary files!")
        print(SYSTEM_TEXT_COLOR+"\nExplanation: free up space and improve your PC's performance!\n")
        try:

            home_directory = os.environ['USERPROFILE']
            print(home_directory)
            temp_dir = str(home_directory) + '\\AppData\\Local\\Temp'
            files = os.listdir(temp_dir)

            for file in files:
                filepath = os.path.join(temp_dir, file)
                try:
                    if os.path.isfile(filepath):
                        os.unlink(filepath)
                    elif os.path.isdir(filepath):
                        shutil.rmtree(filepath)
                except Exception as e:
                    print(e)

            display_text_letter_by_letter("\n"+CHARACTER_TEXT_COLOR+ CHARACTER_NAME+ ": Temporary files cleaned! YAAY!\n")
            print(SYSTEM_TEXT_COLOR)
        except FileNotFoundError:
            print(SYSTEM_TEXT_COLOR)

            print("\nExplanation: The temporary folder could not be found. Please check your system settings.\n")
        except Exception as e:
            print(SYSTEM_TEXT_COLOR)

            print(f"\nExplanation: An error occurred while deleting the temporary folder: {e}\n")
def chkdsk():
    try:
        divider()
        print(Fore.LIGHTGREEN_EX+"""
            +------------------------------------+
            |       BEGINNING CHKDSK SCAN        |
            +------------------------------------+
                """)
        display_text_letter_by_letter(
            CHARACTER_TEXT_COLOR + CHARACTER_NAME + ": Time to do the chkdsk scan!\n" + SYSTEM_TEXT_COLOR + "SYSTEM: Please be patient...beginning chkdsk scan.\n")
        display_text_letter_by_letter("Explanation: CHKDSK (check disk) is a system tool or utility on Windows operating systems that scans your hard drive for file system errors.\n")
        command = f"chkdsk"
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        handle_process(process, "CHKDSK Scan")
        print(SYSTEM_TEXT_COLOR)
    except Exception as e:
        display_text_letter_by_letter("\n"+CHARACTER_TEXT_COLOR+CHARACTER_NAME+": O..Oh no! Something happened with the CHKDSK scan! ;__;")
        print(SYSTEM_TEXT_COLOR+"\nSystem Error: " + str(e) + "\n")

def sfc_scan_now():
    try:
        divider()
        print(Fore.LIGHTGREEN_EX+"""
        +------------------------------------+
        |       BEGINNING SFC SCAN           |
        +------------------------------------+
        """)
        display_text_letter_by_letter(
            CHARACTER_TEXT_COLOR+CHARACTER_NAME+": Okay, " + get_current_username() + "! Let’s make this SFC Scan ✨sparkly✨.\nMomo: Please be patient...this might take a while. (´・ω・`)")
        display_text_letter_by_letter( SYSTEM_TEXT_COLOR+
            "\nExplanation: System File Checker is a built-in Windows utility that scans for corrupted system files and attempts to repair them. The results will indicate any repaired or unresolved issues.\n")
        command = f"sfc /scannow"
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        display_text_letter_by_letter(CHARACTER_TEXT_COLOR+
            CHARACTER_NAME+": Alright, let’s get started!\n\n"+SYSTEM_TEXT_COLOR+"SYSTEM: The program is working hard. Please don’t interrupt it.\n")
        handle_process(process, "SFC Scan")
        display_text_letter_by_letter("\n" + CHARACTER_TEXT_COLOR+ CHARACTER_NAME+": Yay! The SFC Scan is complete! 🎉")
        print(SYSTEM_TEXT_COLOR)
        return True
    except Exception as e:
        display_text_letter_by_letter(SYSTEM_TEXT_COLOR+"\nSystem Error: " + str(e))


def handle_process(process, title_of_command):
    stdout, stderr = process.communicate()
    print(process.communicate()[0].decode("utf-8").rstrip())
    if process.returncode != 0:
        # Check for errors in both streams
        if stderr:
            print(f"Error: {stderr.decode('utf-8').rstrip()}")
        else:
            print(f"Error: {stdout.decode('utf-8').rstrip()}")
        tasks_failed.append(str(title_of_command))
        raise Exception(str(title_of_command) + " Failed")
    else:
        print(f"\n{str(title_of_command)} completed successfully.")

        tasks_passed.append(str(title_of_command))



def display_text_letter_by_letter(text, delay=0.02):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(delay)
    print()

def defragment():
    try:
        divider()

        print(Fore.LIGHTGREEN_EX+"""
                +------------------------------------+
                |       BEGINNING DEFRAGMENT         |
                +------------------------------------+
                """)
        display_text_letter_by_letter(
            CHARACTER_TEXT_COLOR + CHARACTER_NAME + ": Now I'm going to defrag your computer! ✨ Let's make it super speedy! ⚡ Yay!")        # Listen Dude! The reason it targets HDD is because if we defragg SSD than the SSD lifespan may be cooked!
        # List of cool shit you can do!: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/defrag
        command = f"defrag /C /O" # /c => Performs the operation on all volumes.  /O => Performs the proper optimization for each media type.
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(SYSTEM_TEXT_COLOR)
        handle_process(process,"Defragment")

    except Exception as e:

        print(SYSTEM_TEXT_COLOR+e)
        return None


def is_admin():
    """Checks if the script is being run as an administrator.

    Returns:
        bool: True if the script is running as an administrator, False otherwise.
    """

    try:
        # Windows specific check
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except ImportError:
        # Unix/Linux check
        return os.geteuid() == 0