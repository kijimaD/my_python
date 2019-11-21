#! /usr/bin/python3
from __future__ import print_function

import sys
import subprocess
import time
from plyer import notification

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

# 例) ~/roguelike/tests/unit$ autorun_pytest.py ~/roguelike pytest -v py 

class MyHandler(PatternMatchingEventHandler):
    def __init__(self, command, patterns):
        super(MyHandler, self).__init__(patterns=patterns)
        self.command = command

    def _run_command(self):
        subprocess.call([self.command, "-sv"])

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
        # 成功か失敗かで分岐させたい
        notification.notify(
            title='pytest',
            message='ユニットテストが完了しました',
            app_name='autorun_pytest.py',
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
