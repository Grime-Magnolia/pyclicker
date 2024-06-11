import keyboard ,mouse ,random, time, platform , os
if os.geteuid() != 0 and platform.system() == "Linux":
    exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")
if(input('R or L:\n') == "R"):
    button = "right"
else:
    button = "left"
stopkey = input('what key do you use to self distruct?? {Key}:\n')
startkey = input('what key do you use to start clicking?? {Key}:\n')
mincps = float(input('how many cps do you min want?? {Float}:\n'))
maxcps = float(input('how many cps do you max want?? {Float}:\n'))
toggle = input('toggle?? {Y/N}:\n')
toggleble = 1
if toggle == 'n':
    while not keyboard.is_pressed(stopkey):
        cps = random.randint(mincps, maxcps)
        if keyboard.is_pressed(startkey):
            mouse.click(button=button)
            try:
                time.sleep(1 / cps)
            except:
                pass
if toggle == 'y':
    toggleble = 0
    while not keyboard.is_pressed(stopkey):
        if toggleble == 1:
            mouse.click(button=button)
        cps = random.randint(mincps, maxcps)
        if keyboard.is_pressed(startkey):
            if toggleble != 1:
                toggleble = 1
            else:
                toggleble = 0
            while keyboard.is_pressed(startkey):
                pass
        try:
            time.sleep(1 / cps)
        except:
            pass
