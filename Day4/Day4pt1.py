lower_bound = 100000000000000000
upper_bound = 1000000000000000000

def adjacent_criteria(psswd):
    for digit, next_digit in zip(str(psswd), str(psswd)[1::]):
        if int(digit) == int(next_digit):
            return True

    return False

def not_decreasing_criteria(psswd):
    for digit, next_digit in zip(str(psswd), str(psswd)[1::]):
        if int(digit) > int(next_digit):
            return False

    return True

def single_double_digit(psswd):
    for digit in str(psswd):
        if str(psswd).count(digit) == 2:
            return True
    
    return False
            
def compute_password():
    psswd_count = 0
    for psswd in range(lower_bound, upper_bound):
        if adjacent_criteria(psswd) and not_decreasing_criteria(psswd) and single_double_digit(psswd):
            print(psswd)
            psswd_count += 1
    
    return psswd_count

#print(not_decreasing_criteria(266672))
#print(single_double_digit(698788))
print(compute_password())
