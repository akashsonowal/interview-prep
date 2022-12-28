#Concurrency
import threading
import time

def func():
  print('ran')
  time.sleep(1)
  print('done')
  
x = threading.Thread(target=func)
x.start()
print(threading.activeCount())
