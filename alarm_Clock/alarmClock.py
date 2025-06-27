import time, datetime, pygame

def setAlarm(alarm_time):
    print(f"Alarm set for { alarm_time}")
    Sound_path = 'alarm_Clock/audio.mp3'
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        
        if(current_time == alarm_time):
            print("Despierta care monda")

            pygame.mixer.init()
            pygame.mixer.music.load(Sound_path)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running= False

        time.sleep(1)


alarm_time = input("Enter the alarm time (HH:MM:SS): ")
setAlarm(alarm_time)