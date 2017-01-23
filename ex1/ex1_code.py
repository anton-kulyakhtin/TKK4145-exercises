# python code
from threading import Thread

def increase_i(total_steps):
	global i
	for k in range(total_steps):
		i=i+1

def decrease_i(total_steps):
	global i
	for k in range(total_steps):
		i=i-1

#def main():
total_steps=1000000
i=0
Thread_incr = Thread(target = increase_i, args = (total_steps,))
Thread_incr.start()

Thread_decr = Thread(target = decrease_i, args = (total_steps,))
Thread_decr.start()

    
Thread_incr.join()
Thread_decr.join()
print(i)


#main()