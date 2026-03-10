"""
Ogechukwu Okereke
CSMC 111
Spring 2026
week5 assignment4
"""
import re
def extract_phone_numbers(text):
    pattern = r"\d{3}-\d{3}-\d{4}"
    return re.findall(pattern, text)
sample_text = "Call me at 123-456-7890 or 987-654-3210. Office: 555-111-2222. Invalid: 1234567890."
print("Phone numbers found:", extract_phone_numbers(sample_text))
email_input = input("Enter an email address: ")
def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.match(pattern, email):
        return "Valid email address."
    else:
        return "Invalid email address."
print(validate_email(email_input))

