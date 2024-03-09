import time
a = 100
def cuntdown(t):
    while t:
        mins, secs = divmod(t, 60)
        print_time = '{:02d}:{:02d}'.format(mins, secs)
        print(print_time)
        time.sleep(1)
        t -= 1
       # a -= 1

        print('End !!! a=', a)


t = int(input('Enter the time in seconds: '))
cuntdown(t)