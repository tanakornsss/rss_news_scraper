# Sanitize text
# Convert all text to lowercase
# Remove all character that is not related
# Ex. ( ) , / : ...

import re


def sanitize_text(text: str) -> str:
    # Split the end part out
    text = text.split(" - ")[0]

    # Lowercase
    text = text.lower()

    # Replace '’ with blank
    text = re.sub(r"(?<=[a-z])['’](?=[a-z])", "", text)

    # Replace special characters with space
    text = re.sub(r"[^a-z0-9ก-๙ ]", " ", text)

    # Replace multiple spaces with single space if found
    text = re.sub(r"\s+", " ", text).strip()
    return text
