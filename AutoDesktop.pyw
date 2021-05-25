import keyboard
import os


# vars
Desktop = True

while Desktop:
    if keyboard.is_pressed("TAB + 1"):
        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Edge.lnk")

    elif keyboard.is_pressed("TAB + 2"):
        os.startfile("C:\\Users\\Lizenznehmer\\Desktop\\Programmieren")

    elif keyboard.is_pressed("TAB + 3"):
        os.startfile("C:\\Users\\Lizenznehmer\\Desktop\\Schule")

    elif keyboard.is_pressed("TAB + 4"):
        os.startfile("C:\\Users\\Lizenznehmer\\Desktop\\Minecraft")

    elif keyboard.is_pressed("TAB + 5"):
        os.startfile("C:\\Users\\Lizenznehmer\\Desktop\\Games")

    elif keyboard.is_pressed("TAB + 6"):
        os.startfile("C:\\Users\\Lizenznehmer\\Desktop\\Norton")

    elif keyboard.is_pressed("TAB + 7"):
        os.startfile("C:\\Users\\Lizenznehmer\\Desktop\\Pics")

    elif keyboard.is_pressed("TAB + 8"):
        os.startfile("C:\\Users\\Lizenznehmer\\Desktop\\Tools")
