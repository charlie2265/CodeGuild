def minimun(nums):
    run_min = float('inf')
    for num in nums:
        if num < run_min:
            run_min = num
    return run_min
    
