# Author: SCT (ADMG) 10/12/21

inital = int(input("Input a investment amount.\n"))

rate = float(input("Input the annual intrest rate (%).\n"))

time = int(input("Input the time the investment will be compounded.\n"))

value = inital * (1 + rate / 12) ** (12 * time)

value = str(value)

time = str(time)

print("Your inital investment value after " + time + " " + "years is " + value)
