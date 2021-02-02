from pynput import mouse
import keyboard

mouseCtr = mouse.Controller()

def on_scroll(x, y, dx, dy):
    if(dy < 0):
        print('down')
        mouseCtr.scroll(0,1)
        keyboard.press_and_release('ctrl+-')
    else:
        print('up')
        keyboard.press_and_release('ctrl+plus')

if __name__ == '__main__':


    with mouse.Listener(
            on_scroll=on_scroll) as listener:
        listener.join()
