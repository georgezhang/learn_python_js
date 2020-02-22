def time_machine(year):
    if year < 2000:
        return
    print("I am in year %d. %s" % (year, "Back to future"))
    time_machine(year - 1)
    print("I came back from %d!!!" % year)

time_machine(2020)