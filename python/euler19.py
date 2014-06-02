def is_leap(year):
    """ Returns True if the year is leap
    The year is leap if is divisible by four and not a century year
    or if it is a century year divisible by 400
    Parameters
    ----------
        year: int
    Returns
    -------
        True if year is a leap year and False if it is not a leap year
    """
    if year%4==0 and ( year%100!=0 or year%400==0):
        return True
    else:
        return False

if __name__ == '__main__':
    #Mon:  Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec,Jan
    dpm = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dd = 1      # 1 Jan 1900 is Monday
    cnt = 0     # therefore initial count is 0
    year = 1900
    while year <= 2000:
        for month in range(12):
            dd += dpm[month]

            if month==1 and is_leap(year):
                dd += 1
            if ( dd%7==0                            # Is Sunday
                 and (year > 1900 or month==11)     # After 1/Jan/1901
                 and (year < 2000 or month<11) ):   # on or Before 1/Dec/2000
                   cnt += 1
        year += 1
    print(cnt)
