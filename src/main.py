import re
import json

INPUT_FILE = "input/raw-text.txt"
OUTPUT_FILE = "output/sample-output.json"

EMAIL_PATTERN = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

PHONE_PATTERN = r"(?:\+250[\s-]?\d{3}[\s-]?\d{3}[\s-]?\d{3}|0\d{9})"

URL_PATTERN = r"https?://(?:www\.)?[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?:/[^\s]*)?"

CREDIT_CARD_PATTERN = r"\b(?:\d{4}[- ]?){3}\d{4}\b"

def classify_alu_email(email):
    domain = email.rsplit("@", 1)[1].lower()

    if domain == "alueducation.com":
        return "ALU official"

    elif domain == "alumni.alueducation.com":
        return "ALU alumni"

    elif domain == "si.alueducation.com":
        return "ALU SI"

    else:
        return "Other"

def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        text = file.read()

    emails = re.findall(EMAIL_PATTERN, text)
    phones = re.findall(PHONE_PATTERN, text)
    urls = re.findall(URL_PATTERN, text)
    credit_cards = re.findall(CREDIT_CARD_PATTERN, text)

    print("Emails:", emails)
    print("Phones:", phones)
    print("URLs:", urls)
    print("Credit cards:", credit_cards)


if __name__ == "__main__":
    main()
