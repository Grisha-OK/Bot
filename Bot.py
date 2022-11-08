import time
import keyboard 

sleep_time1 = ""
sleep_time2 = ""
namber_for = ""
input_hotkey = ""

print("Введите значение задершки, если ноль то не получится мотать камерой, желатиль не челое число")
sleep_time1 = input()

print("Введите значение задершки, это почти не на что не влияет, желатиль не челое число")
sleep_time2 = input()

print("Введите число итераций, целое число")
namber_for = input()

print("Введите хоткей")
input_hotkey = input()

sleep_time1 = float(sleep_time1)
sleep_time2 = float(sleep_time2)
namber_for =  int(namber_for)
input_hotkey = str(input_hotkey)

def fast_name():
    for x in range(namber_for):
        time.sleep(sleep_time1)
        keyboard.press_and_release("/")
        time.sleep(sleep_time2)
        keyboard.press_and_release("ctrl + v")
        keyboard.press_and_release("enter")

keyboard.add_hotkey(input_hotkey, lambda: fast_name())
keyboard.wait()