import keyboard ,mouse ,random, time, platform , os
if os.geteuid() != 0 && platform.system() == "Linux":
    exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")
if(input('R or L:\n') == "R"):
    button = "right"
else:
    button = "left"
stopkey = input('what key do you use to self distruct??:\n')
startkey = input('what key do you use to start clicking??:\n')
mincps = int(input('how many cps do you min want??:\n'))
maxcps = int(input('how many cps do you max want??:\n'))
toggle = input('toggle??:\n')
toggleble = 1
if toggle == 'False':
    while not keyboard.is_pressed(stopkey):
        cps = random.randint(mincps, maxcps)
        if keyboard.is_pressed(startkey):
            mouse.click(button=button)
            try:
                time.sleep(1 / cps)
            except:
                pass
if toggle == 'True':
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
