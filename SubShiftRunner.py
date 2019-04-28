import argparse
import SubShift

parser = argparse.ArgumentParser(
    description='Utility for quickly fixing time offsets in subtitles')

parser.add_argument('-f', '--file', type=str,
                    help='Input file', required=True)
parser.add_argument('-t', '--time', type=str,
                    help='Time offset. Format is hh:mm:ss,lll' +
                    'Example: to move 4.5 seconds back, input is ' +
                    '00:00:04,500', required=True)

parser.add_argument('-o', '--output', type=str,
                    help='Output file. Should have the same name as movie ' +
                    'file, but ending in .srt', required=True)

parser.add_argument('-d', '--direction', type=str,
                    help='Direction in which to shift subtitles. F/B for ' +
                    'Forward/Backward respectively')

args = parser.parse_args()

input_file = args.file
delta = args.time
output_file = args.output
direction = args.direction

SubShift.main(input_file, delta, output_file, direction)
