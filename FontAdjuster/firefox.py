import os.path
import sqlite3

process = "Firefox.app"

def adjustFont(percent):

    profilesDir = os.path.expanduser("~") + "/Library/Application Support/Firefox/Profiles/"

    if os.path.exists(profilesDir) == False:
        raise FileNotFoundError("Firefox profiles dir not found")

    profileDir = None
    for item in os.listdir(profilesDir):
        if item.endswith("-release"):
            profileDir = item
            break

    if profileDir is None:
        raise FileNotFoundError("Could not find release Firefox profile")

    contentPrefsPath = profilesDir + profileDir + "/" + "content-prefs.sqlite"

    if os.path.exists(contentPrefsPath) == False:
        raise FileNotFoundError("Could not find firefox content-prefs.sqlite")

    connection = sqlite3.connect(contentPrefsPath)

    cursor = connection.cursor()
    settings = cursor.execute("select * from settings").fetchall()

    settingId = None

    for setting in settings:
        if setting[1] == 'browser.content.full-zoom':
            settingId = setting[0]
            break

    if settingId is None:
        cursor.execute("INSERT INTO settings VALUES ('browser.content.full-zoom')")
        settingId = cursor.lastrowid

    cursor.execute("DELETE FROM prefs WHERE settingID = ? AND groupId IS NOT NULL", (settingId,))
    cursor.execute("UPDATE prefs SET value = ? WHERE settingID = ?", (percent, settingId))
    connection.commit()

    print("Firefox: content-prefs.sqlite updated")
