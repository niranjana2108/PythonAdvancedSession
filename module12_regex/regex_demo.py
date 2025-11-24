import re

# ----------------------------------------
# Example 1: Finding all numbers
# ----------------------------------------
def find_numbers():
    text = "I have 2 apples and 5 bananas."
    result = re.findall(r"\d+", text)
    print("Numbers found:", result)


# ----------------------------------------
# Example 2: Email validation
# ----------------------------------------
def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$" #r means raw string
    if re.match(pattern, email):
        print(f"{email} is Valid")
    else:
        print(f"{email} is Invalid")


# ----------------------------------------
# Example 3: Extract dates
# ----------------------------------------
def extract_dates():
    text = "Today's date is 09-11-2025. Tomorrow is 20-11-2025."
    dates = re.findall(r"\d{2}-\d{2}-\d{4}", text)
    print("Dates found:", dates)


# ----------------------------------------
# Example 4: Replace multiple spaces
# ----------------------------------------
def clean_spaces():
    text = "Python    is    awesome"
    print("Cleaned Text:", text)
    clean = re.sub(r"\s+", " ", text)
    print("Cleaned Text:", clean)


# MAIN
if __name__ == "__main__":
    find_numbers()
    validate_email("test@example.com")
    validate_email("invalid-email")
    extract_dates()
    clean_spaces()
