def count_sundays(year):
  """Counts the number of Sundays in a given year.

  Args:
    year: The year to count the Sundays in.

  Returns:
    The number of Sundays in the given year.
  """
  days_in_year = 365
  if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    days_in_year += 1
  number_of_sundays = days_in_year // 7
  return number_of_sundays
number_of_sundays = count_sundays(2023)
print(number_of_sundays)