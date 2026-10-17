import statistics

def main():

    data= [2,3,4,5,6]

    mean_val=statistics.mean(data)
    mode_val=statistics.mode(data)
    median_val=statistics.median(data)

    variance_val=statistics.pvariance(data)

    print(mean_val)
    print(mode_val)
    print(median_val)
    print(variance_val)

main()
