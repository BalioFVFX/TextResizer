import json
import os.path

# -0.5778829311823857 -> 90%
# 0.0 -> 100%
# 0.5227586988632231 -> 110%
# 1.2239010857415449 -> 125%
# 1.5778829311823854 -> 133%

def adjustFont(size):
    braveDir = os.path.expanduser("~") + "/Library/Application Support/BraveSoftware/Brave-Browser"

    if os.path.exists(braveDir) == False:
        raise FileNotFoundError("Brave dir not found")

    bravePrefsDir = braveDir + "/Default/Preferences"

    if os.path.exists(bravePrefsDir) == False:
        raise FileNotFoundError("Brave Preferences not found")

    prefsFile = open(bravePrefsDir, 'r')
    prefsJson = json.load(prefsFile)
    prefsFile.close()

    prefsJson['partition'] = {}

    partition = prefsJson['partition']
    partition['default_zoom_level'] = {'x': float(size)}
    partition['per_host_zoom_levels'] = {'x': {}}

    prefsFile = open(bravePrefsDir, 'w')
    json.dump(prefsJson, prefsFile, indent=2)
    prefsFile.close()

    print("Brave preferences updated")