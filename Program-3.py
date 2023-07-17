def generate_series(a):
    series = []
    i = 1
    while i <= a:
        if i % 2 == 1:
            series.append(i)
        i += 1
    return series
