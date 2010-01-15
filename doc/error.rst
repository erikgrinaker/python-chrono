:mod:`chrono.error` - Exceptions
================================

The :class:`chrono.error` module contains various custom exceptions that
are used by python-chrono.

.. note::

   These exceptions are imported into the main :mod:`chrono` module,
   and can therefore be referenced both via (for example)
   :class:`chrono.error.YearError` and :class:`chrono.YearError`.

Exception inheritance is structured as follows:

* :class:`ValueError`

  * :class:`chrono.error.DateTimeError`

    * :class:`chrono.error.DateError`

      * :class:`chrono.error.DayError`
      * :class:`chrono.error.MonthError`
      * :class:`chrono.error.YearError`

    * :class:`chrono.error.TimeError`

      * :class:`chrono.error.HourError`
      * :class:`chrono.error.MinuteError`
      * :class:`chrono.error.SecondError`

  * :class:`chrono.error.ParseError`

Exception reference
-------------------

.. automodule:: chrono.error
   :members:
