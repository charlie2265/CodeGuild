
# Charlie Lab18 peaks_and_valleys
# loops work through list

def peaks(data):
    #returns list of indices of peaks in data
    peaks = []
    for i in range(1, len(data)-1):
        left = data[i-1]
        mid = data[i]
        right = data[i+1]
        if mid > left and mid > right:
            peaks.append(i)
    return peaks
    

def valleys(data):
    #returns list of indices of peaks in data
    valleys = []
    for i in range(1, len(data)-1):
        left = data[i-1]
        mid = data[i]
        right = data[i+1]
        if mid < left and mid < right:
            valleys.append(i)
    return valleys
    

def peaks_and_valleys(data):
    peaks_and_valleys = []
    
    #returns indices of peaks and valleys sorted
    # peaks_and_valleys.append(peaks(data))
    # peaks_and_valleys.append(valleys(data))
    # peaks_and_valleys.sort
    p = peaks(data)
    v = valleys(data)
    peaks_and_valleys = p + v
    return sorted(peaks_and_valleys)


data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
print(peaks(data))
print(valleys(data))
print(peaks_and_valleys(data))
