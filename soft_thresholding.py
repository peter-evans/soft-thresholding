import numpy as np
import numpy.random as npr

# The maximum number of candidates to select
max_candidates = 3
# The sorted list
sorted_list = sorted(npr.random_integers(1, 100, size=25))
print "Sorted list of candidates:", sorted_list

while (len(sorted_list) > 1):
    # Output remaining candidates
    print "Remaining candidates:", len(sorted_list)

    # Calculate the mean, median and standard deviation of the list
    mean = np.mean(sorted_list)
    median = np.median(sorted_list)
    std = np.std(sorted_list)

    # If the standard deviation is zero the list values are identical
    if (std == 0):
        sorted_list = sorted_list[:max_candidates]
        break

    if (abs(mean - median) < 0.1 * max(mean, median)) & (std < 0.5 * mean):
        if len(sorted_list) <= max_candidates:
            break

    # Remove any values less or equal to the minimum of the mean and median
    sorted_list = [_ for _ in sorted_list if _ <= min(mean, median)]


# Results after soft threshold iterations
print "=" * 24
print "Selected candidates:", sorted_list
