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
    while True:
        high_from_user_str = input("Enter the high of the tringle cm : ")
        base_from_user_str = input("Enter the base of the tringle cm : ")

        try:
            high_from_user = int(high_from_user_str)
            base_from_user = int(base_from_user_str)

            # calling functions
            calculate_tringle_area(high_from_user, base_from_user)
            break
        except:
            print("Something wrong")
            print("Please re-enter the values.")


if __name__ == "__main__":
    main()
