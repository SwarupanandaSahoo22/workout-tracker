# Alarm Clock

import time
import datetime

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("YEAHHH BUDDY! TIME TO WAKE UP 😴")
        
            is_running = False

        time.sleep(1)


if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)