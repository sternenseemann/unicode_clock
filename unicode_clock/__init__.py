#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
#  This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from datetime import datetime

FULLHOURS = "_🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚🕛"
HALFHOURS = "_🕜🕝🕞🕟🕠🕡🕢🕣🕤🕥🕦🕧"


class RangeError(Exception):
    pass


def round_time(hour, minute):
    if not (hour in range(24) and minute in range(60)):
        raise RangeError()
    if minute < 15:
        return hour, 0
    elif minute >= 45:
        return hour + 1, 0
    else:
        return hour, 30


def twentyfour2twelve(hour):
    if hour == 0 or hour == 24 or hour == 12:
        return 12
    else:
        return hour % 12


def unicode_clock(hour, minute):
    rh, rm = round_time(hour, minute)
    rh = twentyfour2twelve(rh)
    if rm == 0:
        return FULLHOURS[rh]
    elif rm == 30:
        return HALFHOURS[rh]

if __name__ == "__main__":
    import sys
    endline = "\n"
    numbers = []
    for arg in sys.argv[1:]:
        if arg == "-h" or arg == "--help" or arg == "--usage":
            print("""Usage:
  {} [-n] [HOUR [MINUTE]]

Arguments:
  -h      Display this message
  -n      Don't print newline after the clock symbol
  HOUR    Set hour to use; if not given, use system clock
  MINUTE  Set minute to use; if not given, use 0,
          if HOUR is given, otherwise system clock""".format(sys.argv[0]))
            sys.exit()
        elif arg == "-n":
            endline = ""
        else:
            try:
                numbers.append(int(arg))
            except ValueError:
                sys.exit("{}: Unexpected command line parameter \"{}\", use {} -h for help".format(sys.argv[0], arg, sys.argv[0]))

    if len(numbers) == 0:
        now = datetime.now()
        numbers = [ now.hour, now.minute ]
    elif len(numbers) == 1:
        numbers.append(0)

    try:
        print(unicode_clock(numbers[0], numbers[1]),end=endline)
    except RangeError:
        sys.exit("{}: Malformed time: {}:{}".format(sys.argv[0], numbers[0], numbers[1]))
