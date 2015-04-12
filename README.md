# python-chrono

python-chrono is a Python module for simple and convenient date/time handling,
including parsing, arithmetic, comparison, formatting, and calendar
functionality. It supports both the ISO and US calendars, and dates/times in
ISO, US, and European formats.

This software is licensed under the terms of the GNU General Public License
version 3, the full text is available in the file LICENSE.

## News

### python-chrono 0.3.0 released (2010-03-08)

This release adds support for date differences (intervals), julian day numbers,
and constants for setting the default calendar and parser. It also fixes some
errors in the documentation code examples.

### python-chrono 0.2.0 released (2010-02-06)

This release adds support for US and european date formats, as well as the US
calendar and 12-hour clocks. It also fixes formatting of 12-hour times.

## Installation

The easiest way to install python-chrono is via PIP:

```
$ pip install python-chrono
```

Releases are also available for download on the [release
page](https://github.com/erikgrinaker/python-chrono/releases), or you can clone
the repo using Git for the latest code. Install with:

```
$ ./setup.py install
```

## Usage

Below are some simple examples of python-chrono usage. To load chrono, run:

```python
>>> import chrono
```

### Parse a date from an ISO-formatted string

```python
>>> date = chrono.Date("2010-07-23")
>>> date.get()
(2010, 7, 23)
>>> date.year
2010
>>> date.month
7
>>> date.day
23
```

### Simple date arithmetic

```python
>>> date = chrono.Date("2010-07-23")
>>> date.month += 6
>>> date.day += 14
>>> date.get()
(2011, 2, 6)
```

### Easy-to-understand formatting

```python
>>> chrono.Date("2010-07-23").format("$weekdayname $day. $monthname $year")
'Sunday 6. February 2011'
```

### Calendar information

```python
>>> date = chrono.Date("2010-07-23")
>>> date.week()
(2011, 5)
>>> date.leapyear()
False
>>> date.monthdays()
28
```

### Date comparisons using various data types

```python
>>> date = chrono.Date("2010-07-23")
>>> date > chrono.Date("2011-01-01")
True
>>> date <= "2011-07-01"
True
>>> date == time.localtime()
False
```
