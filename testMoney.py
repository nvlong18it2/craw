import csv
import time
import pyautogui
import random
money = 100
chuoi= [0,5,10,25,40,30,20]
delay=0
ran = random.randint(0, 1)
level = 1
cuoc = chuoi[1]
sleepTime = 0.2
filename ="craw_2.csv"
def Num(num):
    for x in range(int(num/50)):
        # dat 50k
        pyautogui.click(170, 510)
        time.sleep(delay)
    for x in range(int(num%100%50/10)):
        # dat 10k
        pyautogui.click(130, 510)
        time.sleep(delay)
    for x in range(int(num%10)):
        # dat 1k
        pyautogui.click(90, 510)
        time.sleep(delay)

def Click(state, number):
    if state==0:
        print("Dat Tai")
        pyautogui.click(120, 450)
        time.sleep(delay)
        Num(number)
    if state==1:
        print("Dat Xiu")
        pyautogui.click(330, 450) 
        time.sleep(delay)
        Num(number)
    pyautogui.click(230, 550)

with open(filename, 'r') as data:
    for line in csv.DictReader(data):
        if money>=cuoc:
            if(int(line['d1']+line['d2']+line['d3'])<=10):
                kq = 1
                if (ran==kq):
                    money+=chuoi[level]
                    cuoc = chuoi[1]
                    level = 1
                    message = 'an tien dat:' + str(cuoc) + 'k'
                    print(message)
                    # client.sendMessage(message, thread_id=client.uid, thread_type=ThreadType.USER)
                    
                else:
                    money-=chuoi[level]
                    level +=1
                    if (level < len(chuoi)):
                        cuoc = chuoi[level]

                    else:
                        level = 1
                        cuoc = chuoi[level]
                        
                    message = 'thua tien dat:' + str(cuoc) + 'k'
                    print(message)
                    # client.sendMessage(message, thread_id=client.uid, thread_type=ThreadType.USER)
            
            if(int(line['d1']+line['d2']+line['d3'])>10):
                kq = 0
                if (ran==kq):
                    money+=chuoi[level]
                    cuoc = chuoi[1]
                    level = 1
                    message = 'an tien dat:' + str(cuoc) + 'k'
                    print(message)
                    # client.sendMessage(messagplaysound('ring.mp3')
                else:
                    money-=chuoi[level]
                    level +=1
                    if (level < len(chuoi)):
                        cuoc = chuoi[level]

                    else:
                        level = 1
                        cuoc = chuoi[level]
                        
                    message = 'thua tien dat:' + str(cuoc) + 'k'
                    print(message)
                    # client.sendMessage(message, thread_id=client.uid, thread_type=ThreadType.USER)
                    
            print("van: ",line['No'],"money:",money)
            time.sleep(sleepTime)
            ran = random.randint(0, 1)
        # Click(ran, cuoc)
                
    

                
            
  