import time
import msvcrt
from datetime import datetime
import winsound 
import os.path
from os import path

def metronome(bpm):


    path.exists("metronomeup.wav")
    
    count = 0
    expected_count = 0
    delay = 60.0/float(bpm)
    ExitKeyPressed = False
    
    print(bpm, "bpm -", delay)
    print(datetime.now(), ", Beat:", count)
    
    start_time = time.time()
    begin_time = start_time

    while ExitKeyPressed == False:
        end_time = start_time + delay
        while end_time > time.time():
            continue  

        expected_count += int((time.time() - start_time) / delay)
        # increment count after every wait and beat after ever 2 counts 
        count += 1

        # set metronome audio according to beat count
    
        if count & 1:
            if path.exists("metronomel.wav") :
                winsound.PlaySound('metronomel.wav', winsound.SND_FILENAME)
            else:
                winsound.Beep(880, 100)
        else:
            if path.exists("metronomer.wav") :
                winsound.PlaySound('metronomer.wav', winsound.SND_FILENAME)
            else:
                winsound.Beep(440, 100)
  
        if count % bpm == 0:
            total_time = end_time - begin_time    
            print(datetime.now(), ", Beat:", count, expected_count)            
            print("used_time", convert_to_hms_format(total_time))
            winsound.Beep(1760, 100)     

        if msvcrt.kbhit() and ord(msvcrt.getch()) == 27:
            ExitKeyPressed = True
            total_time = end_time - begin_time   
            print(datetime.now(), ", Beat:", count, expected_count)
            print("total_time", convert_to_hms_format(total_time))
            if path.exists("tada.wav") :
                winsound.PlaySound('tada.wav', winsound.SND_FILENAME)
            else:
                winsound.Beep(3520, 100)            
            
        start_time = end_time     
        
def convert_to_hms_format(sec):
    sec += 1
    sec = sec % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60
#    print("seconds value in hours:",hour)
#    print("seconds value in minutes:",min)
    return "%02d:%02d:%02d" % (hour, min, sec) 

        
metronome (180)