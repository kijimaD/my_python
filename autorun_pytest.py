#! /usr/bin/python3
from __future__ import print_function

import os
import sys
import subprocess
import time
from plyer import notification

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

# 例) ~/roguelike/tests/unit$ autorun_pytest.py ~/roguelike pytest -v py

HOME_DIR = os.path.split(os.path.abspath(__file__))[0]
ICON_SUCCESS = os.path.join(HOME_DIR,"data","success.png")
ICON_FAILED  = os.path.join(HOME_DIR,"data","failed.png")

class MyHandler(PatternMatchingEventHandler):
    def __init__(self, command, patterns):
        super(MyHandler, self).__init__(patterns=patterns)
        self.command = command
        self.std = ""

    def _run_command(self):
        self.std = subprocess.call([self.command, "-sv"])

    def on_moved(self, event):
        # self._run_command()
        pass

    def on_created(self, event):
        # self._run_command()
        pass

    def on_deleted(self, event):
        # self._run_command()
        pass

    def on_modified(self, event):
        print("\n\n")
        print("▼▽▼▽▼▽▼▽▼▽▼modified▼▽▼▽▼▽▼▽▼▽▼")
        print("\n\n")
        self._run_command()

        error_count = str(self.std)
        if error_count == '0':
            notify_message = '*成功*しました!!'
            notify_title = 'pytest'
            notify_icon = ICON_SUCCESS
        else:
            notify_message = '*失敗*ユニットテストが' + error_count + 'つ失敗しました'
            notify_title = 'pytest'
            notify_icon =ICON_FAILED
        notification.notify(
            title=notify_title,
            message=notify_message,
            app_name='autorun_pytest.py',
            app_icon=notify_icon,
        )


def watch(path, command, extension):
    event_handler = MyHandler(command, ["*"+extension])
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    if 4 > len(sys.argv):
        print("Usage:", sys.argv[0], "dir_to_watch command extension")
    else:
        watch(sys.argv[1], sys.argv[2], sys.argv[3])
