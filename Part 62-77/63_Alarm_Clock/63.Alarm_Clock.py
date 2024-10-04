import time     # for updating time
import datetime # for String formatation
import pygame   # for sound

def set_alarm(alarm_time):
    print(f"alarm set for {alarm_time}")
    sound_file = "alarm_clock_sound.mp3"
    
    is_running = True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        
      
        if current_time == alarm_time:
            print(":::::Wake Up:::::")
            
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)     # it will Load the file
            pygame.mixer.music.play()                        # it will play the file
            
            while pygame.mixer.music.get_busy():
                time.sleep(1)
                
            is_running = False
                
        time.sleep(1)
        

if __name__ == "__main__":
    alarm_time = input("Enter the Alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)