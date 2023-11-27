import re

def extract_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(pattern, text)
    return emails

def validate_email(email):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(pattern, email)

# Example text containing email addresses
sample_text = """
This is a sample text with emails such as test.email@example.com,
another.email@example.co.uk, and one_more@email.com.
However, not.everything.is.an.email and @invalid.com is not valid either.
"""

# Extracting and printing email addresses from the sample text
extracted_emails = extract_emails(sample_text)
print("Extracted emails:")
for email in extracted_emails:
    print(email)

# Validating email addresses
print("\nValidating emails:")
emails_to_validate = ["test.email@example.com", "invalid@email", "another.email@example.co.uk"]
for email in emails_to_validate:
    if validate_email(email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is NOT a valid email address.")
