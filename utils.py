class utils:   
    '''
    Given a number num, returned the number reversed.
    Used algorithm from https://www.programiz.com/python-programming/examples/reverse-a-number
    '''
    def reversed(self, num: int):
        if not type(num) is int:
            try: 
                num = int(num)
            except ValueError:
                raise ValueError("Cannot convert num to int.")
        reversed_num = 0
        while num != 0:
            digit = num % 10
            reversed_num = reversed_num * 10 + digit
            num //= 10
        return reversed_num
    '''
    Given a number num, returned it in binary (base 2) and octal (base 8) format.
    '''
    def formatter(self, num: int):
        if not type(num) is int:
            try: 
                num = int(num)
            except ValueError:
                raise ValueError("Cannot convert num to int.")
        return bin(num), oct(num)

