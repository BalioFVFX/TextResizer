import os
import signal


def closeApps(appProcessNames):
    currentUser = os.path.expanduser("~").split("/")[2]
    runningProcesses = os.popen('ps aux').readlines()
    closedApps = []

    for runningProcess in runningProcesses:
        split = runningProcess.split()

        if split[0] != currentUser:
            continue

        for appProcessToClose in appProcessNames:
            if runningProcess.__contains__(appProcessToClose):
                os.kill(int(split[1]), signal.SIGTERM)
                if appProcessToClose not in closedApps:
                    closedApps.append(appProcessToClose)
                break


    for closedApp in closedApps:
        print("Closed: " + closedApp)