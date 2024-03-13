from pywhatkit.core import core
import os, sys, json, datetime, time, pyautogui

def copy_path(path):
    print(os.getcwd() + "/" + path)
    core.copy_image(os.getcwd() + "/" + path)

def send_photo(path, wishes, mobile):
    core.send_image(path, wishes, mobile, wait_time=15)
    core.close_tab(5)
    pyautogui.press("enter")

def run(argv):
    photo = argv[0] 
    print(photo)
    wishes = open(argv[1], "r").read()
    mobiles = json.load(open(argv[2], "r"))
    print(mobiles)

    date_entry = input('Enter a date in YYYY-MM-DD format: ')
    year, month, day = map(int, date_entry.split('-'))
    date1 = datetime.date(year, month, day)

    while True:
        if datetime.date.today() == date1:
            for name in mobiles:
                print(f"saying hi to {name}")
                send_photo(photo, f"Dear {name} \n" + wishes, mobiles[name])
            break
        else: 
            print("see you in an hour")
            time.sleep(600)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        exit("USAGE: <photo> <wishes> <contacts>")
    run(sys.argv[1:])                                                                    