'''
How many cores does the machine have?
'''
# import os
# import multiprocessing

# def get_cpu_cores():
#     if os.name == 'posix': # Linux / MAC
#         return os.sysconf('SC_NPROCESSORS_ONLN')
#     elif os.name == 'nt': # Stupid Windows
#         return os.cpu_count()
#     else:
#         return None

# if __name__ == "__main__":
#     cores = get_cpu_cores()
#     if cores != None:
#         print(f"Number of CPU cores: {cores}")
#     else:
#         print("Unable to determine the number of CPU cores.")

'''
How fast can the machine find prime numbers from 3 to n using a single core?
'''
# import math
# import time
# def getPrimeNumbersUpTo(number):
#     array = []
#     for i in range(3,number):
#         flag = True
#         for j in range(3,math.ceil(i/2)+1):
#             if i % j == 0:
#                 flag = False
#                 break
#         if flag:
#             array.append(i)
#     return array

# if __name__ == "__main__":
#     start_time = time.time()
#     print(getPrimeNumbersUpTo(80000))
#     end_time = time.time()
#     elapsed_time = end_time - start_time
#     print(f"Elapsed Time: {elapsed_time} seconds")

'''
How fast can the machine find prime numbers from 3 to n using all cores?
'''
# import time
# import math
# import threading
# def is_prime(num):
#     for j in range(2, math.ceil(num/2) + 1):
#         if num % j == 0:
#             return False
#     return True

# def get_prime_numbers(start, end, result_list):
#     for i in range(start, end):
#         if is_prime(i):
#             result_list.append(i)

# def get_prime_using_all_cores(number, num_threads=4):
#     array = []
#     threads = []

#     # Split the range into chunks for each thread
#     chunk_size = (number - 3) // num_threads
#     start = 3

#     for _ in range(num_threads):
#         end = start + chunk_size
#         thread = threading.Thread(target=get_prime_numbers, args=(start, end, array))
#         thread.start()
#         threads.append(thread)
#         start = end

#     # Wait for all threads to finish
#     for thread in threads:
#         thread.join()

#     return array

# if __name__ == "__main__":
#     start_time = time.time()
#     result = get_prime_using_all_cores(80000)
#     end_time = time.time()
#     elapsed_time = end_time - start_time

#     print(result)
#     print(f"Elapsed Time: {elapsed_time} seconds")