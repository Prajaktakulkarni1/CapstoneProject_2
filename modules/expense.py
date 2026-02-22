import re
from datetime import datetime

class Expense:
    def __init__(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date

    @staticmethod
    def validate_amount(amount):
        try:
            amount = float(amount)
            if amount <= 0:
                return None
            return amount
        except ValueError:
            return None

    @staticmethod
    def validate_date(date):
        pattern = r"^\d{4}-\d{2}-\d{2}$"
        if re.match(pattern, date):
            try:
                datetime.strptime(date, "%Y-%m-%d")
                return True
            except ValueError:
                return False
        return False

    def to_file_string(self):
        return f"{self.amount},{self.category},{self.date}"

    @staticmethod
    def from_file_string(line):
        parts = line.strip().split(",")
        if len(parts) != 3:
            return None
        return Expense(float(parts[0]), parts[1], parts[2])
