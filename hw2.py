import time

def num_paths(m, n):
    # TODO: Task 1 of the assignment

def num_paths_memo(m, n):
    # TODO: Task 2 of the assignment

#driver code - you do not need to make any changes after this line.
#However, submit a screenshot of the output to report the execution time/elapsed time.
start_time = time.time()
print(num_paths(15,14))
end_time = time.time()

start_time_memo = time.time()
print(num_paths_memo(15,14))
end_time_memo = time.time()

print(f"Elapsed time (no memoization): {end_time - start_time} seconds")
print(f"Elapsed time (memoization): {end_time_memo - start_time_memo} seconds")
