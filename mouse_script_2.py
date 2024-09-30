import pyautogui
import time
import random
import keyboard
pyautogui.FAILSAFE = False

def move_mouse():
    # 取得螢幕解析度大小
    size = pyautogui.size()
    print("{} x {}".format(size.width, size.height))

    # 取得目前滑鼠位置
    position = pyautogui.position()
    original_x=position.x
    original_y=position.y

    i = 0
    while i <= 2:
        # 產生隨機移動的距離
        random_x = random.uniform(-1, 1)
        random_y = random.uniform(-1, 1)
        random_move = random.uniform(0.1, 0.1)

        # 滑鼠移動
        #pyautogui.moveTo(size.width/2, size.height/2)
        #position = pyautogui.position()
        pyautogui.moveTo(position.x + random_x, position.y + random_y, random_move)
        pyautogui.moveTo(original_x, original_y)
        position = pyautogui.position()
        
        #print("({}, {})".format(position.x, position.y))
        i = i + 1

    pyautogui.moveTo(original_x, original_y, 0.2)
    pyautogui.press('win')  #按一下win鍵
    pyautogui.press('win')  #按一下win鍵

    
cycle_run=1

x=180   #每個cycle的間隔時間
duration_time= input('please keyin duration time(hr): ')
duration_time=float(duration_time)*3600

if int(duration_time)<x:
    print('Duration time is smaller than cycle time, total run time will be 24hr')
    totla_cycle_times= round(24*60*60/x)
else:
    totla_cycle_times= round(int(duration_time)/x)

# 設定每x秒執行一次click_mouse函數
while True:
    # 保存初始的x值
    original_x = x
       
    move_mouse()
    #pyautogui.write('Hello world!',0.1)


    print('Cycle='+str(cycle_run))
    cycle_run=cycle_run+1
    totla_cycle_times=totla_cycle_times-1
    print('remaining time='+str(totla_cycle_times*original_x/60)+' min')

        
    while x>0:
        time.sleep(1)
        print(x)
        x=x-1
    x=original_x
    # 檢查是否有按鍵輸入，如果是空格就停止
    if totla_cycle_times<=0:
        print("Porgram done")
        break
