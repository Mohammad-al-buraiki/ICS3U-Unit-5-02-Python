# !/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on January 2021
# This program is a tringle area program

def calculate_tringle_area(high, base):
    # this function is calculation the tringle area

    # process

    area = 1/2*(high*base)

    # output
    print("the area of tringle is {0} cm².".format(area))


def main():
    # input
    high_from_user = int(input("Enter the high of the tringle: "))
    base_from_user = int(input("Enter the base of the tringle: "))

    # calling functions
    calculate_tringle_area(high_from_user, base_from_user)


if __name__ == "__main__":
    main()
