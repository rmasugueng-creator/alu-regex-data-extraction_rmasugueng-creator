import re
import json

INPUT_FILE = "input/raw-text.txt"
OUTPUT_FILE = "output/sample-output.json"


def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        text = file.read()

    print(text)


if __name__ == "__main__":
    main()
