def checkPalindrome(inputString):
    reversed_string = inputString[::-1]
    
    if reversed_string == inputString:
        return True
    elif reversed_string != inputString:

        return False

checkPalindrome("Fad")
