"""
Something is wrong with global snow production, and you've been selected to take
a look. The Elves have even given you a map; on it, they've used stars to mark
the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you
need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day
in the Advent calendar; the second puzzle is unlocked when you complete the
first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough")
and where they're even sending you ("the sky") and why your map looks mostly
blank ("you sure ask a lot of questions") and hang on did you just say the sky
("of course, where do you think snow comes from") when you realize that the
Elves are already loading you into a trebuchet ("please hold still, we need to
strap you in").

As they're making the final adjustments, they discover that their calibration
document (your puzzle input) has been amended by a very young Elf who was
apparently just excited to show off her art skills. Consequently, the Elves are
having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line
originally contained a specific calibration value that the Elves now need to
recover. On each line, the calibration value can be found by combining the first
digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and
77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the
calibration values?
"""
import os
import sys

def load_file_as_list(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

def account_for_overlap(input_string):
    # run some string transformations that fix cases like "twone"

    text = input_string

    overlap_to_fixed = {
    "ron": "roon",
    "nei": "neei",
    "won": 'woon',
    "eei": 'eeei',
    "vei": 'veei',
    "eni": 'enni',
    "hth": "htth",
    "htw": "httw"
    }

    for short_combo, long_combo in overlap_to_fixed.items():
        text = text.replace(short_combo, long_combo)

    return text

def text_to_number(input_string):
    # convert spelled-out numbers to numerical characters. eg "three" --> 3

    text = input_string

    words_to_digits = {
    "zero":'0',
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
    }

    for word, digit in words_to_digits.items():
        text = text.replace(word, digit)
    return text

    return text

def compute_line_value(input_string):
    first_digit = None
    last_digit = None

    reverse_string = input_string[::-1]

    # get the first number
    for char in input_string:
        if char.isdigit():
            if first_digit is None:
                first_digit = char
                break

    # get the last number
    for char in reverse_string:
        if char.isdigit():
            if last_digit is None:
                last_digit = char
                break

    return first_digit + last_digit

def main():
    all_lines = load_file_as_list('day1input.txt')
    print(all_lines[:30])
    print("/n")

    all_lines_fixed = [account_for_overlap(line) for line in all_lines]
    print(all_lines_fixed[:30])
    print("/n")

    all_lines_with_digits = [text_to_number(line) for line in all_lines_fixed]
    print(all_lines_with_digits[:30])
    print("/n")

    totals = [int(compute_line_value(lines)) for lines in all_lines_with_digits]
    print(totals[:30])

    print(sum(totals))

    # print(sum(totals))

if __name__ == '__main__':
    main()
