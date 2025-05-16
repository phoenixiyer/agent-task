import re
from typing import List, Tuple

def validate_csv(file_path: str) -> List[Tuple[int, str]]:
    """
    Validate a CSV file against the requirements.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        List[Tuple[int, str]]: List of errors, where each error is a tuple of the row number and the error message.
    """
    errors = []

    with open(file_path, 'r') as file:
        rows = file.readlines()

    # Check header
    headers = rows[0].strip().split(',')
    if headers != ['id', 'name', 'email', 'age', 'subscription_status']:
        errors.append((1, 'Invalid headers'))

    # Validate rows
    for row_num, row in enumerate(rows[1:], start=2):
        values = row.strip().split(',')
        if len(values) != 5:
            errors.append((row_num, 'Invalid number of columns'))
            continue

        # Validate id
        try:
            id_value = int(values[0])
            if id_value <= 0:
                errors.append((row_num, 'id must be a positive integer'))
        except ValueError:
            errors.append((row_num, 'id must be an integer'))

        # Validate name
        name_value = values[1]
        if not name_value or len(name_value) > 100:
            errors.append((row_num, 'name must be a non-empty string with max 100 characters'))

        # Validate email
        email_value = values[2]
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email_value):
            errors.append((row_num, 'email must be a valid email address'))

        # Validate age
        try:
            age_value = int(values[3])
            if age_value < 13 or age_value > 120:
                errors.append((row_num, 'age must be an integer between 13 and 120'))
        except ValueError:
            errors.append((row_num, 'age must be an integer'))

        # Validate subscription_status
        subscription_status = values[4]
        if subscription_status not in ['active', 'expired', 'trial', 'canceled']:
            errors.append((row_num, 'subscription_status must be one of: active, expired, trial, canceled'))

    return errors