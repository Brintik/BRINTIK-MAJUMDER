# This is a programm to help worker who mainly work infront of computer. It reminds the user to take care of thier health and also keep an record of it.
# Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log
# Eyes - eyes.mp3 - every 30 min - EyDone - log
# Physical activity - physical.mp3 every - 45 min - ExDone - log
#
# Rules
# Pygame module to play audio

from pygame import mixer
mixer.init()
import datetime
import time

def waterReminder():
    print("Drink water first Dumbass\n")
    mixer.music.load("demon.mp3")
    mixer.music.play()
    enter = input("type done when you done\nand don't fucking try to cheat!\n>>>\t").lower()
    while True:
        if enter == "done":
            mixer.music.stop()
            print("Noicee!")
            with open("waterReminder.txt", "a") as a:
                a.write(f"Time\t{now0}\n")
            break
        else:
            print("type done -_-\"")
            enter = input(">>>\t").lower()

def eyeReminder():
    print("eyee")
    mixer.music.load("shape.mp3")
    mixer.music.play()
    enter = input("type done when you done\nand don't fucking try to cheat!\n>>>\t").lower()
    while True:
        if enter == "done":
            mixer.music.stop()
            print("Noicee!")
            with open("eyeReminder.txt", "a") as a:
                a.write(f"Time\t{now0}\n")
            break
        else:
            print("type done -_-\"")
            enter = input(">>>\t").lower()

def workoutReminder():
    print("workout time")
    mixer.music.load("onMyWay.mp3")
    mixer.music.play()
    enter = input("type done when you done\nand don't fucking try to cheat!\n>>>\t").lower()
    while True:
        if enter == "done":
            mixer.music.stop()
            print("Noicee!")
            with open("workoutReminder.txt", "a") as a:
                a.write(f"Time\t{now0}\n")
            break
        else:
            print("type done -_-\"")
            enter = input(">>>\t").lower()

def afternoonWorkout():
    print("workout time")
    mixer.music.load("onMyWay.mp3")
    mixer.music.play()
    enter = input("type done when you done\nand don't fucking try to cheat!\n>>>\t").lower()
    while True:
        if enter == "done":
            mixer.music.stop()
            print("Noicee!")
            with open("workoutReminder.txt", "a") as a:
                a.write(f"Time\t{now0}")
            break
        else:
            print("type done -_-\"")
            enter = input(">>>\t").lower()
while True:

    while True:

        now = datetime.datetime.now()
        start_time = now.replace(hour=7, minute=0, second=0, microsecond=0)
        start_day_time = now.replace(hour=10,minute=0,second=0,microsecond=0)
        end_time = now.replace(hour=23, minute=59, second=59, microsecond=0)
        # morning_excersice = now.replace(hour=7,minute=30,second=0,microsecond=0)
        afternoon_excersice = now.replace(hour=16,minute=30,second=0,microsecond=0)
        if now >= start_time and now <= end_time:
            break

    munite1 = 60
    minute2 = 30
    minute3 = 60
    minute_added1 = datetime.timedelta(minutes=munite1)
    minute_added2 = datetime.timedelta(minutes=minute2)
    minute_added3 = datetime.timedelta(minutes=minute3)

    waterTime = start_day_time + minute_added1
    eyeTime = start_day_time + minute_added2
    workoutTime = start_day_time + minute_added3

    while True:

        time.sleep(1)
        now0 = datetime.datetime.now()
        # print(f"{waterTime}\t{eyeTime}\t{workoutTime}\t{now0}")
        if now0 > end_time:
            break

        if now0 >= waterTime :
            waterReminder()
            now1 = datetime.datetime.now()
            waterTime = now1 + minute_added1
        elif now0 >= eyeTime :
            eyeReminder()
            now2 = datetime.datetime.now()
            eyeTime = now2 + minute_added2
        elif now0 >= workoutTime :
            workoutReminder()
            now3 = datetime.datetime.now()
            workoutTime = now3 + minute_added3
        elif now0 >= afternoon_excersice :
            afternoonWorkout()
