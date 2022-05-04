#!/usr/bin/python3
'''Contains a method that determines if a given data set represents
a valid UTF-8 ecnoding
'''


def validUTF8(data: list) -> bool:
    '''Checks if a given data set is a valid UTF-8
    '''
    for num in data:
        if type(num) == int:
            base = 128
            if num & base:
                return False
            else:
                continue
        else:
            return False
    return True
