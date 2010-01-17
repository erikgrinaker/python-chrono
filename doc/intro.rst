Introduction
============

python-chrono is a Python module for simple and convenient date/time
handling, including parsing, arithmetic, comparison, formatting,
and calendar functionality.

The main classes are :class:`chrono.Date`, :class:`chrono.Time`, and
:class:`chrono.DateTime`, which handles dates, times, and date/times
respectively. It also contains a range of support modules which provide
the functionaliy that these classes build upon.

Currently, python-chrono is built for the ISO 8601 date standard, which
is widely used internationally (especially in west-Europe and east-Asia),
with the notable exception of the United States. As such, it only accepts
dates in ISO format (for example, *yyyy-mm-dd*), and calendar-related
functionality is based on the ISO calendar - more on this later. Support
for the US date standard is planned for a future release.

python-chrono does not include any functionality for time zones or daylight
savings time, but this is planned for a future release.

The following sections describe some typical usage of the
:class:`chrono.Date` class. The :class:`chrono.Time` and :class:`chrono.DateTime`
classes behave in much the same way, but only :class:`chrono.Date` is
covered, for simplicity.

Date parsing
------------

Date parsing is done simply by instantiating a :class:`chrono.Date` object,
passing the date string to be parsed as input. Once instantiated, the
attributes :attr:`chrono.Date.year`, :attr:`chrono.Date.month`, and
:attr:`chrono.Date.day` contain the respective date parts, like so::

   >>> date = chrono.Date("2009-07-23")
   >>> date.year
   2009
   >>> date.month
   7
   >>> date.day
   23

To retrieve all the attributes at once, you can use :meth:`chrono.Date.get`::

   >>> date = chrono.Date("2009-07-23")
   >>> date.get()
   (2009, 7, 23)

If :class:`chrono.Date` is passed an invalid date it will raise either
:exc:`chrono.error.ParseError` for invalid/unknown format, or a subclass
of :exc:`chrono.error.DateError` (such as :exc:`chrono.error.MonthError`)
if the date was parsed properly but contained an invalid date value::

   >>> date = chrono.Date("xyz")
   chrono.error.ParseError: Invalid ISO date value 'xyz'

   >>> date = chrono.Date("2009-13-27")
   chrono.error.MonthError: Month '13' not in range 1-12

All the date formats described in the ISO 8601 standard are supported,
such as::

   >>> # week dates
   >>> chrono.Date("2009-W32").get()
   (2009, 8, 3)

   >>> # ordinal dates
   >>> chrono.Date("2009-314").get()
   (2009, 11, 10)

   >>> # month dates
   >>> chrono.Date("2009-07").get()
   (2009, 7, 1)

You can also pass a range of non-string inputs to the class, which will
be handled according to the object type::

   >>> # boolean True indicates the current time
   >>> chrono.Date(True).get()
   (2010, 1, 23)

   >>> # integers are interpreted as UNIX timestamps
   >>> chrono.Date(1263745408).get()
   (2010, 1, 17)

   >>> # fetch data from time.struct_time objects
   >>> chrono.Date(time.localtime())
   (2010, 1, 23)

   >>> # fetch data from datetime.date objects
   >>> chrono.Date(datetime.date(2010, 7, 23)).get()
   (2010, 7, 23)

For a complete list of valid formats, see the :class:`chrono.parser.ISOParser`
documentation. For other input types, see the :class:`chrono.Date` documentation.

If you would like to parse date strings without instantiating a
:class:`chrono.Date` object, you can use the underlying
:class:`chrono.parser.ISOParser` class directly::

   >>> # parses all supported date formats
   >>> chrono.parser.ISOParser.parse_date("2009-07-23")
   (2009, 7, 23)

   >>> # only parses week dates
   >>> chrono.parser.ISOParser.week("2009-W32")
   (2009, 32)

   >>> # only parses ordinal dates
   >>> chrono.parser.ISOParser.month("2009-314")
   (2009, 314)

See the :class:`chrono.parser.ISOParser` documentation for more
information.

Date formatting
---------------

Date formatting is done via the :meth:`chrono.Date.format` method, which
takes a string containing substitution variables of the form ''$name'' or
''${name}'', and replaces them with actual values::

   >>> # full human-readable date
   >>> chrono.Date("2009-07-23").format("$weekdayname $day. $monthname $year")
   'Thursday 23. July 2009'

   >>> # ISO-date, using 0-padded values
   >>> chrono.Date("2009-07-23").format("$0year-$0month-$0day")
   '2009-07-23'

For a full list of substitution variables, see the :class:`chrono.Formatter`
documentation.

Calendar information
--------------------

python-chrono uses the ISO calendar, which has the following
characteristics:

 * Weeks start on Monday
 * The first week of a year is the week which contains the first Thursday

:class:`chrono.Date` has a number of methods for retreiving
calendar-related information about the date - for example::

   >>> # week that contains the date
   >>> chrono.Date("2009-07-23").week()
   (2009, 30)

   >>> # whether the date is in a leap year
   >>> chrono.Date("2008-07-23").leapyear()
   True

   >>> # number of days in the month
   >>> chrono.Date("2009-07-23").monthdays()
   31

   >>> # weekday of the date
   >>> chrono.Date("2009-07-23").weekday()
   4

For a full list of such methods, see the :class:`chrono.Date` documentation.

If you would like to retreive calendar information without having to
instantiate a :class:`chrono.Date` object, you can use the underlying
:class:`chrono.calendar.ISOCalendar` class directly::

   >>> chrono.calendar.ISOCalendar.yeardays(2008)
   366

   >>> chrono.calendar.ISOCalendar.ordinal(2009, 7, 23)
   204

   >>> chrono.calendar.ISOCalendar.weekdate(2009, 7, 23)
   (2009, 30, 4)

See the :class:`chrono.calendar.ISOCalendar` documentation for more
information.

Date arithmetic
---------------

Date arithmetic (addition, subtraction, etc) is done by special handling of
the :attr:`chrono.Date.year`, :attr:`chrono.Date.month`, and :attr:`chrono.Date.day`
attributes. If any of these are set to a value that is outside their valid range,
the object will automatically update the attributes to a proper date, by
incrementing or decrementing values as necessary.

Here are some examples::

   >>> # adding days to a date
   >>> date = chrono.Date("2009-07-26")
   >>> date.day += 10
   >>> date.get()
   (2009, 8, 5)

   >>> # subtracting months from a date
   >>> date.month -= 2
   >>> date.get()
   (2009, 6, 5)

   >>> # adding years to a date
   >>> date.year += 3
   >>> date.get()
   (2012, 6, 5)

.. warning::

   When the date is on one of the last days of a month, and the :attr:`chrono.Date.month` or
   :attr:`chrono.Date.year` attribute is changed, you may get a result which is in a different
   month than the one you expect. This happens when the day number is out of range
   for the new month, due to differences in month lengths::

      >>> date = chrono.Date("2009-07-31")
      >>> date.month -= 1
      >>> date.get()
      (2009, 7, 1)

   When :attr:`chrono.Date.month` is set to 6, the date will become 2009-06-31. Since June
   only has 30 days this will trigger the overflow-handling that the date arithmetic relies
   on, and update the date to a valid date. The same happens with leap years::

      >>> date = chrono.Date("2008-02-29")
      >>> date.year += 1
      >>> date.get()
      (2009, 3, 1)

Date comparison
---------------

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
:class:`time.struct_time` or :class:`datetime.date` objects, and any other value that
:class:`chrono.Date` is able to process::

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

