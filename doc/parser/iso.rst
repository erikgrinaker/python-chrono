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

=================== =================== ======================= ===============================================
Format              Example             Description             Method
=================== =================== ======================= ===============================================
yyyy-mm-dd hh:mm:ss 2009-12-27 15:27:43 Datetime [#f1]_
yyyy-mm-dd          2009-12-27          Date                    :meth:`chrono.parser.ISOParser.date`
hh:mm:ss            15:27:43            Time [#f1]_             :meth:`chrono.parser.ISOParser.time`
yyyy-ddd            2009-163            Ordinal day             :meth:`chrono.parser.ISOParser.ordinal`
yyyy-Www-d          2009-W36-3          Week and day            :meth:`chrono.parser.ISOParser.weekdate`
yyyy-Www            2009-W36            Week                    :meth:`chrono.parser.ISOParser.week`
yyyy-mm             2009-12             Month                   :meth:`chrono.parser.ISOParser.month`
yyyy                2009                Year                    :meth:`chrono.parser.ISOParser.year`
yyyymmdd hhmmss     20091227 152743     Compact datetime [#f1]_
yyyymmdd            20091227            Compact date            :meth:`chrono.parser.ISOParser.compactdate`
hhmmss              152743              Compact time [#f1]_     :meth:`chrono.parser.ISOParser.compacttime`
yyyyddd             2009163             Compact ordinal day     :meth:`chrono.parser.ISOParser.compactordinal`
yyyyWwwd            2009W363            Compact week and day    :meth:`chrono.parser.ISOParser.compactweekdate`
yyyyWww             2009W36             Compact week            :meth:`chrono.parser.ISOParser.compactweek`
=================== =================== ======================= ===============================================

.. [#f1] Seconds and minutes may be omitted in times

Class reference
---------------

.. autoclass:: chrono.parser.ISOParser
   :members:
   :member-order: groupwise
