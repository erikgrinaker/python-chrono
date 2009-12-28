:class:`chrono.parser.ISOParser` - ISO 8601 parser
==================================================

ISO 8601 is a variant of the Gregorian calendar which is widely used internationally,
in particular in western Europe. The ISO calendar has the following characteristics:

* Weeks start on Monday
* Weekdays are specified in the range 1 (Monday) to 7 (Sunday)
* The first week of a year is the week containing the first Thursday
* Hours are in the range 0 (midnight) to 23, as opposed to the 12-hour times used in the U.S. etc

Valid formats
-------------

The most commonly used ISO formats are *yyyy-mm-dd* and *yyyy-mm-dd hh:mm:ss*,
although the standard specifies a range of formats:

=================== =================== =======================
Format              Example             Description
=================== =================== =======================
yyyy-mm-dd          2009-12-27          Regular date
hh:mm:ss            15:27:43            Regular time [#f1]_
yyyy-mm-dd hh:mm:ss 2009-12-27 15:27:43 Regular datetime [#f1]_
yyyymmdd            20091227            Compact date
hhmmss              152743              Compact time [#f1]_
yyyymmdd hhmmss     20091227 152743     Compact datetime [#f1]_
yyyy                2009                Year
yyyy-mm             2009-12             Month
yyyy-Www            2009-W36            Week
yyyy-Www-d          2009-W36-3          Week and day
yyyyWww             2009W36             Compact week
yyyyWwwd            2009W363            Compact week and day
yyyy-ddd            2009-163            Ordinal day
=================== =================== =======================

.. [#f1] Seconds and minutes may be omitted in times

Class reference
---------------

.. autoclass:: chrono.parser.ISOParser
   :members:
   :member-order: groupwise
