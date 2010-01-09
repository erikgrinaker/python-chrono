:class:`chrono.Date` - main class for date handling
===================================================

The :class:`chrono.Date` class is the main class used for handling dates.
It has the attributes :attr:`year`, :attr:`month`, and :attr:`day` for
storing date information, and can parse a range for date formats on
class initialization, or via the various :func:`set_*` methods.

The class has :func:`set_*` methods for setting the date from various formats,
:func:`get_*` methods for retreiving various representations of the date, and
a :func:`format` method for custom formatting of the date. It also has a range
of methods to get extra information about the date based on the calendar backend
that is used, such as :func:`leapyear` (if date is in a leap year), :func:`monthdays`
(number of days in the month), :func:`week` (the week number of the date),
:func:`weekday` (the weekday of the date), and so on.

Date formats and calendars
--------------------------

See :class:`chrono.parser.ISOParser` and :class:`chrono.parser.ISOCalendar`.

Date arithmetic via attribute overflow
--------------------------------------

Date arithmetic (addition, subtraction, etc) is done by special handling of
the :attr:`year`, :attr:`month`, and :attr:`day` attributes. If any of these
are set to a value that is outside their valid range, the object will automatically
update the attributes to the proper date, by incrementing or decrementing values
as necessary.

Here are some examples::

   >>> # adding days to a date
   >>> d = chrono.Date("2009-07-26")
   >>> d.day += 10
   >>> d.get()
   (2009, 8, 5)

   >>> # subtracting months from a date
   >>> d.month -= 2
   >>> d.get()
   (2009, 6, 5)

   >>> # adding years to a date
   >>> d.year += 3
   >>> d.get()
   (2012, 6, 5)

.. warning::

   When the date is on one of the last days of a month, and the :attr:`month` or
   :attr:`year` attribute is changed directly, you may get a resulting date which
   is in a different month than the one you specified. This happens when the day
   number is out of range for the new month, due to differences in month lengths.
   Here is an example::

      >>> d = chrono.Date("2009-07-31")
      >>> d.month = 6
      >>> d.get()
      (2009, 7, 1)

   When :attr:`month` is set to 6, the date will become 2009-06-31. Since June only
   has 30 days this will trigger the overflow-handling that the date arithmetic relies
   on, and update the date to a valid date. The same happens with leap years::

      >>> d = chrono.Date("2008-02-29")
      >>> d.year += 1
      >>> d.get()
      (2009, 3, 1)

   To avoid making unwitting errors like these when setting a full date, it is
   recommended to use one of the :meth:`set_*` methods instead of setting the
   attributes directly.

Date comparisons
----------------

Date comparisons can be done using the normal Python comparison operators: ``==``,
``!=``, ``>``, and ``<``::

   >>> chrono.Date("2009-07-31") == chrono.Date(year = 2009, month = 7, day = 31)
   True

   >>> chrono.Date("2009-07-31") > chrono.Date("2009-07-01")
   True

   >>> chrono.Date("2009-07-31") <= chrono.Date("2009-07-01")
   False

If the value that is being compared with is not a :class:`chrono.Date` object, it will
be converted to one if possible. This allows for comparisons with strings, UNIX timestamps,
:class:`time.struct_time` or :class:`datetime.date`, and any other value that :class:`chrono.Date`
is able to process::

   >>> # string with ISO date
   >>> chrono.Date("2009-07-31") == "2009-07-31"
   True

   >>> # string with ISO weekdate
   >>> chrono.Date("2009-07-31") != "2009-W31-5"
   False

   >>> # integer UNIX timestamp
   >>> chrono.Date("2009-07-31") > 1241683613
   True

   >>> # time.struct_time, as returned by time.localtime() etc
   >>> chrono.Date("2009-07-31") > time.localtime()
   False

   >>> # datetime.date objects
   >>> chrono.Date("2009-07-31") < datetime.date(2009, 2, 17)
   True


Class reference
---------------

.. autoclass:: chrono.Date
   :members:
   :member-order: groupwise
