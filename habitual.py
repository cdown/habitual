#!/usr/bin/env python

import crontab
import subprocess
import logging
import argparse
import sched
import os
import time

# TODO:
#
# - Tear down and rebuild scheduler on inotify events
# - Code cleanliness

s = sched.scheduler(time.time)
LOG = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def notify(name, ct, prog):
    LOG.info("Running notifier for '%s'", name)
    ret = subprocess.call([prog, name])
    if ret != 0:
        LOG.warning("Command returned %d: %r", ret, [prog, name])

    pending_secs = ct.next(default_utc=False)
    LOG.info("Scheduling next run for '%s' in %d seconds", name, pending_secs)
    s.enter(pending_secs, 1, notify, argument=(name, ct, prog))


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-p",
        "--prog",
        default="notify-send",
        help="the program to send notifications to (default: %(default)s)",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    with open(os.path.expanduser("~/.config/habitual/habitual")) as f:
        for line in f:
            raw_schedule, name = line.strip().split("|", 1)
            ct = crontab.CronTab(raw_schedule)
            pending_secs = ct.next(default_utc=False)
            LOG.info("Scheduling next run for '%s' in %d seconds", name, pending_secs)
            s.enter(pending_secs, 1, notify, argument=(name, ct, args.prog))

        s.run()


if __name__ == "__main__":
    main()
