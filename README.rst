``habitual`` is a simple application to send reminders for things which
are on a fixed, repeated schedule.

You can tell ``habitual`` which application to use using ``--exec``. The
default is ``notify-send``. The application should take one argument –
the name of the reminder. If you need to pass more, create a wrapper
script and call that. The default is ``notify-send``, but you may want
to send to other services like `Pushbullet`_ or `Pushover`_, for
example.

Configuration
=============

Reminders are is typically stored at ``~/.config/habitual/habitual``,
and are automatically reloaded when the file is changed. The format is
like so:

::

   cron|name

For example, here’s how someone’s reminders might look:

::

   0 0 10-20 ? * * *|Drink water
   0 0 1 ? * * *|Start winding down

.. _Pushbullet: https://www.pushbullet.com/
.. _Pushover: https://pushover.net/
