class Date:

    # 构造函数
    def __init__(self, year, month, date):
        self.year = year
        self.month = month
        self.date = date

    def tomorrow(self):
        self.date += 1

    @staticmethod
    def date_parse_from_string(date_str):
        year, month, date = tuple(date_str.split('-'))
        return Date(int(year), int(month), int(date))

    @staticmethod
    def is_valid_str(date_str):
        year, month, date = tuple(date_str.split('-'))
        if int(year) > 0 and int(month) < 12 and int(date) < 31:
            return True
        else:
            return False

    @classmethod
    def from_string(cls, date_str):
        year, month, date = tuple(date_str.split('-'))
        return cls(int(year), int(month), int(date))

    def __str__(self):
        return "{year}/{month}/{date}".format(year=self.year, month=self.month, date=self.date)


if __name__ == "__main__":
    new_day = Date(2018, 6, 28)
    new_day.tomorrow()
    print(new_day)

    date_str = '2018-6-18'
    year, month, date = tuple(date_str.split('-'))
    new_day1 = Date(int(year), int(month), int(date))
    print(new_day1)

    new_day2 = Date.date_parse_from_string(date_str)
    print(new_day2)

    new_day3 = Date.from_string(date_str)
    print(new_day3)

    new_day4 = Date.is_valid_str('2018-6-32')
    print(new_day4)
