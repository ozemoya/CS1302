from datetime import datetime

class Date:
    # Constructor
    def __init__(self, m, d, y):
        self.month = m
        self.day = d
        self.year = y

    def leap_year(self):
        return (self.year % 4 == 0) and (self.year % 100 != 0 or self.year % 400 == 0)

    @classmethod
    def today(cls):
        today = datetime.today()
        return cls(today.month, today.day, today.year)

    def day_of_weekS(self):
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        return days[self.day_of_weekN()]

    def day_of_weekN(self):
        Y = self.year - (14 - self.month) // 12
        x = Y + Y // 4 - Y // 100 + Y // 400
        M = self.month + 12 * ((14 - self.month) // 12) - 2
        D = (self.day + x + (31 * M) // 12) % 7
        return D

    def tomorrow(self):
        days_in_month = [31, 29 if self.leap_year() else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        new_day = self.day + 1
        new_month = self.month
        new_year = self.year

        if new_day > days_in_month[self.month - 1]:
            new_day = 1
            new_month += 1
            if new_month > 12:
                new_month = 1
                new_year += 1

        return Date(new_month, new_day, new_year)

    def add(self, ndays):
        result_date = self
        for _ in range(ndays):
            result_date = result_date.tomorrow()
        return result_date

    def after(self, d):
        return (self.year, self.month, self.day) > (d.year, d.month, d.day)

    def equals(self, d):
        return (self.year, self.month, self.day) == (d.year, d.month, d.day)

    def before(self, d):
        return (self.year, self.month, self.day) < (d.year, d.month, d.day)


    def days_between(self, d):
        # Check if the end date is the current date (for living individuals)
        if d.equals(Date.today()):
            # Apply the specific counting rule for living individuals
            day_count = abs(self.to_days() - d.to_days())
            # Adjust the count by subtracting 1
            return day_count - 1
        else:
            # For deceased individuals, use the existing calculation
            day_count = abs(self.to_days() - d.to_days())
            return day_count


    pass
    def to_days(self):
        # Convert a date to the number of days since a fixed date (e.g., 01/01/0000)
        m = (self.month + 9) % 12
        y = self.year - m // 10
        return 365*y + y//4 - y//100 + y//400 + (m*306 + 5)//10 + (self.day - 1)
    def __str__(self):
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        return f"{self.day} {months[self.month-1]}, {self.year}"


