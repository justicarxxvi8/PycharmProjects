def incorrectPasscodeAttempts(passcode, attempts):
    tries = 0
    while tries < 9:
        for x in attempts:
            if x != passcode:
                tries += 1
                if tries == 9:
                    return False
            elif len(attempts) == 0:
                return False
            elif x == passcode:
                return True
    return False


password = "1234"
password_input = ["9999",
 "9999",
 "9999",
 "9999",
 "9999",
 "9999",
 "9999",
 "9999",
 "9999",
 "1234",
 "9999",
 "9999"]

incorrectPasscodeAttempts(password,password_input)