"""
Ogechukwu Okereke
CSMC 111
Spring 2026
week5 assignment2
"""
password = input("Enter a password: ")
if len(password) >= 8:
    print("Password accepted. It meets the minimum length requirement.")
else:
    print("Password too short. It must be at least 8 characters long.")