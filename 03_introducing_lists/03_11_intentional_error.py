# Avoiding index errors.

guest_list = ['Kenny', 'Carter', 'Preston']
print(guest_list[3])

'''
Traceback (most recent call last):
  File "c:\Users\mmale\OneDrive\Desktop\CSC_141\03_introducing_lists\03_11_intentional_error.py", line 4, in <module>
    print(guest_list[3])
          ~~~~~~~~~~^^^
IndexError: list index out of range
''' 
# Lists start at 0 so there is no element for Python to print for 3.