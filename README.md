# ALU Regex Data Extraction

## Description
This project extracts and validates structured information
from untrusted raw text using Python regular expressions.

## Data types
The program extracts:
- Email addresses
- Phone numbers
- URLs
- Credit card numbers

## Project structure

...

## Requirements
Python 3.x

## How to run
python src/main.py

## Security considerations

The input is treated as untrusted.
Credit card numbers are validated using the Luhn algorithm
and are masked before being written to the output.
Malformed emails, URLs, phone numbers and card numbers
are rejected.

The program does not execute extracted content.

## Edge cases

The input contains:
- Different spacing formats
- Different phone number formats
- Invalid email addresses
- Invalid credit card numbers
- URLs with paths and query parameters
- Injection-like text
