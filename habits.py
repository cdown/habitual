#!/usr/bin/env python

import crontab
import sched
import os
import time

# TODO:
#
# - Tear down and rebuild scheduler on inotify events
# - External exec support
# - Logging at schedule and execution time
# - Code cleanliness

s = sched.scheduler(time.time)


def notify(title, ct):
    print(title)
    pending_secs = ct.next(default_utc=False)
    s.enter(pending_secs, 1, notify, argument=(title, ct))


def main():
    with open(os.path.expanduser("~/.config/habits/habits")) as f:
        for line in f:
            raw_schedule, name = line.strip().split("|", 1)
            ct = crontab.CronTab(raw_schedule)
            pending_secs = ct.next(default_utc=False)
            s.enter(pending_secs, 1, notify, argument=(name, ct))
        s.run()


if __name__ == "__main__":
    main()
