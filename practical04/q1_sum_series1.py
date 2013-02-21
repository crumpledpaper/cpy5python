

def sum_series1(i):
    if i==1:
        return 1
    else:
        return 1/i+sum_series1(i-1)
