#helpful shared functions

#return if string can be converted to int
def is_number(n):
    try:
        int(n)
        return True
    except:
        return False

#converts string num to appropriate int
def to_int(num):
    if num:
        return int(num)
    else:
        return 1
