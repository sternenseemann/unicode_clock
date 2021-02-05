# unicode 🕐

This package includes:

* `unicode-clock`: script displaying the closest available unicode clock symbol to the current time
* `unicode_clock`: python library offering the same symbol approximation for arbitrary times

## usage

In the base mode `unicode-clock` will display the current system time as a unicode symbol:

```
13:37 $ unicode-clock
🕜
```

You can also give a specific time, by giving an hour and optionally a minute to use
(if the minute is omitted, `unicode-clock` will use 0).

```
13:38 $ unicode-clock 13 12
🕐
```

If you add `-n` to any invocation, `unicode-clock` won't print a trailing newline:

```
$ unicode-clock -n 23; echo " <- Clock"
🕚 <- Clock
```

## library example

```
from unicode_clock import unicode_clock

clock = unicode_clock(13, 37)
```

## installation

`unicode-clock` only depends on Python 3 and installs as you'd expect using `setuptools`.

## license
![](http://www.gnu.org/graphics/gplv3-127x51.png)
