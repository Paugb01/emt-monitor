import emtvlcapi
import time
import pygame
# get bus times for stop 508 and line 93
response = emtvlcapi.get_bus_times(1616, 92)

print(response)

# run a loop to get the bus times every 10 seconds and if the bus is coming in less than 5 minutes, play a sound with playsound


pygame.init()
pygame.mixer.music.load("./assets/mysound.wav")

already_played = []

while True:
    response = emtvlcapi.get_bus_times(1616)
    for bus in response:
        if bus['minutos'] in [9,10]:
            print("Bus is coming in less than 5 minutes")
            print(response)
            # play sound
            pygame.mixer.music.play()
    time.sleep(60)




