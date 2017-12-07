import sys

digit_string = sys.argv[1]
#digit_string='2234'
sdigit=0
for digit in digit_string:
  sdigit+=int(digit)
print(sdigit)
