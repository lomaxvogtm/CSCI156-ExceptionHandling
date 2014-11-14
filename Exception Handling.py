__author__ = 'Madeleine'


inputstring = "Please enter your social security number in the form AAA-GG-SSSS: "

def SS(social):
    try:
        area, group, serial = social.split("-")
        t = area, group, serial
        if len(t) == 3:
            if "666" in area:
                print("Please retype your number correctly.")
                return None
            elif "00" in area:
                print("Please retype your number correctly.")
                return None
            elif "000" in group:
                print("Please retype your number correctly.")
                return None
            elif "0000" in serial:
                print("Please retype your number correctly.")
                return None
            elif len(area) != 3:
               print("Please retype your number correctly.")
               return None
            elif len(group) != 2:
                print("Please retype your number correctly.")
                return None
            elif len(serial) != 4:
                print("Please retype your number correctly.")
                return None
            elif "078" in area + "05" in group + "1120" in serial:
                print("Please retype your number correctly.")
                return None
        else:
            print("Please retype your number correctly.")
        area = int(area)
        group = int(group)
        serial = int(serial)
        if 900<= area <= 999:
            print("Please retype your number correctly.")
            return None
    except ValueError:
        print("Please enter a valid social security number.")
        return None
    exit()


def truth(s):
    social = input(s)
    ss = SS(social)
    while ss is None:
        social = input(s)
        ss = SS(social)
    return ss


truth(inputstring)