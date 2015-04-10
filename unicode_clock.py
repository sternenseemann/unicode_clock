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

if __name__ == '__main__':
    now = datetime.now()
    print(unicode_clock(now.hour, now.minute))
