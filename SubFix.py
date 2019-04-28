import re
import numpy as np


def timestamp_to_num(ts):
    num_list = []
    ts_list = re.split('[:,]', ts)
    for i in ts_list:
        num_list.append(int(i))
    return np.array(num_list)


def main(filename, delta, output, direction):
    buff = []
    # Read file
    with open(filename, 'r') as f:
        contents = f.readlines()


    # For each line
    for line in contents:
        # Parse line for timestamp
        ts = parse_timestamp(line)
        # If no timestamp, put into buffer as is
        if ts == []:
            buff.append(line)
        # If timestamp exists, make change of delta, put into buffer:
        else:
            new_ts = update_timestamps(ts, delta, direction)
            new_ts_str = timestamp_to_string(new_ts)
            new_line = create_ts_line(new_ts_str)
            buff.append(new_line)

    # Write buffer out
    with open(output, 'w') as file:
        for i in buff:
            file.write(i)


def create_ts_line(ts):
    begin = ts[0]
    end = ts[1]
    string = begin + ' --> ' + end + '\n'
    return string


def timestamp_to_string(ts):
    strings = []
    begin = ts[0]
    end = ts[1]
    strings.append('%02d:%02d:%02d,%03d' % (begin[0], begin[1], begin[2], begin[3]))
    strings.append('%02d:%02d:%02d,%03d' % (end[0], end[1], end[2], end[3]))
    return strings


def update_timestamps(lst, delta, direction):
    # Convert to lists
    begin = timestamp_to_num(lst[0])
    end = timestamp_to_num(lst[1])
    new_delta = timestamp_to_num(delta)

    # Convert to millisecond scalars
    begin_ms = convert_to_ms(begin)
    end_ms = convert_to_ms(end)
    new_delta_ms = convert_to_ms(new_delta)

    # Update timestamps
    if direction == 'B':
        new_begin_ms = begin_ms - new_delta_ms
        new_end_ms = end_ms - new_delta_ms
    else:
        new_begin_ms = begin_ms + new_delta_ms
        new_end_ms = end_ms + new_delta_ms

    # Convert back to list format
    new_begin = convert_to_ts(new_begin_ms)
    new_end = convert_to_ts(new_end_ms)

    return [new_begin, new_end]


def convert_to_ts(millis):
    hours = int(millis // 3.6e6)
    millis %= 3.6e6
    minutes = int(millis // 60000)
    millis %= 60000
    seconds = int(millis // 1000)
    millis = int(millis % 1000)

    return [hours, minutes, seconds, millis]


def convert_to_ms(timestamp):
    ms = timestamp[3]
    secs = timestamp[2] * 1000
    mins = timestamp[1] * 1000 * 60
    hours = timestamp[0] * 1000 * 3600

    time_in_ms = ms + secs + mins + hours
    return time_in_ms


def parse_timestamp(txt):
    pattern = '\d\d:\d\d:\d\d,\d*'
    return re.findall(pattern, txt)


