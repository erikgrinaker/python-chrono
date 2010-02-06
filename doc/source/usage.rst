.. _usage:

Usage
=====

The main classes are :class:`chrono.Date`, :class:`chrono.Time`, and
:class:`chrono.DateTime`, which handles dates, times, and date/times
respectively. A range of other classes are also available, which provide
the functionality that these classes build upon.

python-chrono does not include any handling of time zones or daylight
savings time, but this is planned for a future release.

The following sections describe some typical usage of the
:class:`chrono.Date` class. The :class:`chrono.Time` and :class:`chrono.DateTime`
classes behave in much the same way, but for simplicity only :class:`chrono.Date` is
covered here.

Parsing
-------

Dates can be specified using either ISO, US, or european formats. Lists
of valid formats are available in the :mod:`chrono.parser` documentation.

By default, python-chrono uses the parser :class:`chrono.parser.CommonParser`,
which accepts the most commonly used date formats. The notable exceptions
are formats without separators (which for example can be interpreted as
either US or european dates), and unusual separators such as . in US dates
(which is the standard separator in Europe). In order to parse such formats,
you need to pass the proper parser to :class:`chrono.Date`.

Date parsing is done simply by instantiating a :class:`chrono.Date` object,
passing the date string to be parsed as input. Once instantiated, the
attributes :attr:`chrono.Date.year`, :attr:`chrono.Date.month`, and
:attr:`chrono.Date.day` will contain the respective date parts::

   >>> date = chrono.Date("2009-07-23")
   >>> date.year
   2009
   >>> date.month
   7
   >>> date.day
   23

To retrieve all the attributes at once, use :meth:`chrono.Date.get`::

   >>> date = chrono.Date("2009-07-23")
   >>> date.get()
   (2009, 7, 23)

The default :class:`chrono.parser.CommonParser` parser handles most normal
date formats, such as::

   >>> # ISO dates
   >>> chrono.Date("2009-07-23").get()
   (2009, 7, 23)

   >>> # US dates
   >>> chrono.Date("07/23/2009").get()
   (2009, 7, 23)

   >>> # european dates
   >>> chrono.Date("23.07.2009").get()

   >>> # ISO week dates
   >>> chrono.Date("2009-W32").get()
   (2009, 8, 3)

   >>> # ISO ordinal dates
   >>> chrono.Date("2009-314").get()
   (2009, 11, 10)

   >>> # ISO month dates
   >>> chrono.Date("2009-07").get()
   (2009, 7, 1)

In order to parse all valid date formats for a region, you can pass the
proper parser class to :class:`chrono.Date`::

   >>> # US dates with two-digit year and no separator
   >>> chrono.Date("072309", chrono.parser.USParser).get()
   (2009, 7, 23)

   >>> # slash-separated european dates
   >>> chrono.Date("23/07/2009", chrono.parser.EuroParser).get()
   (2009, 7, 23)

If :class:`chrono.Date` is passed an invalid date it will raise either
:exc:`chrono.error.ParseError` for invalid/unknown format, or a subclass
of :exc:`chrono.error.DateError` (such as :exc:`chrono.error.MonthError`)
if the date was parsed properly but contained an invalid date value::

   >>> date = chrono.Date("xyz")
   chrono.error.ParseError: Invalid ISO date value 'xyz'

   >>> date = chrono.Date("2009-13-27")
   chrono.error.MonthError: Month '13' not in range 1-12

You can also pass a range of non-string inputs to the class, which will
be handled according to the object type::

   >>> # boolean True indicates the current date
   >>> chrono.Date(True).get()
   (2010, 1, 23)

   >>> # integers are interpreted as UNIX timestamps
   >>> chrono.Date(1263745408).get()
   (2010, 1, 17)

   >>> # fetch data from time.struct_time objects
   >>> chrono.Date(time.localtime()).get()
   (2010, 1, 23)

   >>> # fetch data from datetime.date objects
   >>> chrono.Date(datetime.date(2010, 7, 23)).get()
   (2010, 7, 23)

For a complete list of all accepted input types, see the :class:`chrono.Date`
documentation.

To parse date strings without instantiating a :class:`chrono.Date` object, you
can use the parser classes directly::

   >>> # parses all supported ISO date formats
   >>> chrono.parser.ISOParser.parse_date("2009-07-23")
   (2009, 7, 23)

   >>> # only parses week dates
   >>> chrono.parser.ISOParser.week("2009-W32")
   (2009, 8, 3)

   >>> # only parses ordinal dates
   >>> chrono.parser.ISOParser.ordinal("2009-314")
   (2009, 11, 10)

See the :mod:`chrono.parser` documentation for more information on parser
classes.

Calendar info
-------------

python-chrono supports both the ISO and US calendars, which have the
following characteristics:

**ISO Calendar:**

 * Weeks start on Monday
 * The first week of a year is the week which contains the first Thursday

**US Calendar:**

 * Weeks start on Sunday
 * The first week of a year is the week which contains January 1st

By default, the ISO calendar is used. As can be seen above, this only
affects functionality related to week numbers or week days.

:class:`chrono.Date` has a number of methods for retreiving calendar-related
information about about a date, such as::

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

To use the US calendar instead, pass the :class:`chrono.calendar.USCalendar`
class to :class:`chrono.Date`::

   >>> # US week containing date
   >>> chrono.Date("2009-07-23", calendar=chrono.calendar.USCalendar).week()
   (2009, 30)

   >>> US weekday of the date
   >>> chrono.Date("2009-07-23", calendar=chrono.calendar.USCalendar).weekday()
   5

For a full list of calendar-related methods, see the :class:`chrono.Date`
documentation.

If you would like to retreive calendar information without having to
instantiate a :class:`chrono.Date` object, you can use the underlying
calendar class directly::

   >>> chrono.calendar.ISOCalendar.yeardays(2008)
   366

   >>> chrono.calendar.ISOCalendar.ordinal(2009, 7, 23)
   204

   >>> chrono.calendar.ISOCalendar.weekdate(2009, 7, 23)
   (2009, 30, 4)

See the :mod:`chrono.calendar` documentation for more
information.

Arithmetic
----------

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

Formatting
----------

Date formatting is done via the :meth:`chrono.Date.format` method, which
takes a string containing substitution variables of the form ``$name`` or
``${name}``, and replaces them with actual values::

   >>> # full human-readable date
   >>> chrono.Date("2009-07-23").format("$weekdayname $day. $monthname $year")
   'Thursday 23. July 2009'

   >>> # ISO-date, using 0-padded values
   >>> chrono.Date("2009-07-23").format("$0year-$0month-$0day")
   '2009-07-23'

For a full list of substitution variables, see the
:class:`chrono.formatter.Formatter` documentation.

Comparison
----------

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
