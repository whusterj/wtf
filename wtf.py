#!/usr/bin/env python

"""
wtf.py
Just write a timestamp to a text file, so later we can calculate the
number of 'WTFs' per minute.

Inspired by: http://www.osnews.com/story/19266/WTFs_m

Use it like this:

    ./wtf.py
"""

import argparse
from datetime import datetime

parser = argparse.ArgumentParser(description="Easily record WTF moments.")
parser.add_argument(
    '-m', '--message',
    type=str,
    help='Record the thing that made you go WTF'
)
parser.add_argument(
    '-o', '--outfile',
    help='Specify a filename for your WTF log.'
)
parser.add_argument(
    '-r', '--read',
    help='Read a WTF log file. Outputs WTFs per minute.'
)


def _parse_timestamp(timestamp):
    """Get timezone-naive datetime object

    Args:
        timestamp (str): Timezone-naive ISO-formatted datetime string.
    """
    ISO_FMT = '%Y-%m-%dT%H:%M:%S.%f'
    return datetime.strptime(timestamp, ISO_FMT)


def get_stats(filename):
    """Read a WTFs log file and compute statistics, including:

     - Total WTFs
     - Total Duration
     - WTFs/minute

    Args:
        filename (str): Path to the WTFs log file.
    """
    with open(filename, 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    timestamps = [line.split(' ')[0] for line in content]

    start = _parse_timestamp(min(*timestamps))
    end = _parse_timestamp(max(*timestamps))

    time_diff = end - start
    total_minutes = time_diff.seconds / 60

    return {
        'total': len(timestamps),
        'duration': total_minutes,
        'wtfs_per_min': len(timestamps) / total_minutes,
    }


if __name__ == "__main__":
    args = parser.parse_args()
    message = args.message
    outfile = args.outfile
    readfile = args.read

    if readfile:
        if (message or outfile):
            raise ValueError(
                'The --read option cannot be used with '
                'the --message or --outfile options'
            )
        stats = get_stats(readfile)
        print('Total WTFs:', stats['total'])
        print('Duration (minutes):', stats['duration'])
        print('WTFs/min:', str(round(stats['wtfs_per_min'], 3)))
    else:
        if outfile is None:
            outfile = 'wtfs.txt'
        with open(outfile, 'a+') as f:
            now = datetime.now()
            f.write(now.isoformat())
            if message:
                f.write(' ' + message)
            f.write('\r\n')
