import os.path

def adjustFont(size):
    spotifyDir = os.path.expanduser("~") + "/Library/Application Support/Spotify"

    if os.path.exists(spotifyDir) == False:
        raise FileNotFoundError("Spotify dir not found")

    usersDir = spotifyDir + "/Users"

    if os.path.exists(usersDir) == False:
        raise FileNotFoundError("Spotify users dir not found")

    users = list(filter(lambda name: name.endswith("-user"), os.listdir(usersDir)))
    users = sorted(users, key=lambda user: os.path.getmtime(os.path.join(usersDir, user)), reverse=True)

    userPrefsDir = os.path.join(usersDir, users[0], "prefs")

    with open(userPrefsDir, 'r') as file:
        fileContent = file.readlines()

    found = False

    for i in range(len(fileContent)):
        if fileContent[i].startswith("app.browser.zoom-level="):
            fileContent[i] = "app.browser.zoom-level=" + str(size)
            found = True
            break

    if not found:
        fileContent.append("app.browser.zoom-level=" + str(size))

    with open(userPrefsDir, 'w') as file:
        for line in fileContent:
            if line == "\n":
                continue
            file.write(line)

    print("Spotify prefs updated")
