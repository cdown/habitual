`habits` is a simple application to send reminders throughout the day, for
things which are on a fixed, repeated schedule.

You can tell `habits` which application to use using `--exec`. The default is
`notify-send`. The application should take one argument -- the name of the
reminder. If you need to pass more, create a wrapper script and call that. The
default is `notify-send`, but you may want to send to other services like
[Pushbullet](https://www.pushbullet.com/) or [Pushover](https://pushover.net/),
for example.
