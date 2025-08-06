def leap_year(year):
    leap = False
    if year%4==0 and year%100!=0 or year%400==0:
        leap = True
        return leap
print(leap_year(2004))