import datetime
import datetime

def date_difference_generator():
    while True:
        jalali_date_str = yield
        jalali_date = datetime.datetime.strptime(jalali_date_str, "%Y-%m-%d").togregorian()
        current_date = datetime.datetime.now()
        difference = (current_date - jalali_date).days
        yield jalali_date.strftime("%Y-%m-%d"), difference

date_diff_gen = date_difference_generator()
next(date_diff_gen)  


user_input = "1399-06-20"
converted_date, days_difference = date_diff_gen.send(user_input)

print(f"Gregorian Date: {converted_date}, Days Difference: {days_difference}")

