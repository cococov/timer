import sys
import time

FULL_SCREEN_ASCII = '\033[H\033[J'
HIDE_CURSOR_ASCII = '\033[?25l'
SHOW_CURSOR_ASCII = '\033[?25h'
DELETE_LINE_ASCII = '\033[K'

script_params = sys.argv[1].split(':')
hours = int(script_params[0])
minutes = int(script_params[1])
seconds = int(script_params[2])

def timer(hours, minutes, seconds):
    total_seconds = hours * 60 * 60 + minutes * 60 + seconds
    now_epoch = time.time()
    future_epoch = now_epoch + total_seconds
    while now_epoch < future_epoch:
        now_epoch = time.time()
        seconds = int(future_epoch - now_epoch)
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        print(f'{FULL_SCREEN_ASCII}{HIDE_CURSOR_ASCII}{DELETE_LINE_ASCII}{hours:02d}:{minutes:02d}:{seconds:02d}', end='\r')
        sys.stdout.flush()
        time.sleep(1)

try:
  timer(hours, minutes, seconds)
except KeyboardInterrupt:
  print(SHOW_CURSOR_ASCII, end='\r')
