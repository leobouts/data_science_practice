import sys
import random

sampling_number = int(sys.argv[1])
reservoir_array = [''] * sampling_number
iteration = 0

#using the standard input

for next_item in sys.stdin:

   	#fill the reservoir array with k first items

	if iteration < sampling_number:
   		reservoir_array[iteration] = next_item
   
	#k+1 iteration to n
	else:
		position_to_be_replaced = random.randint(0, iteration)
		if position_to_be_replaced < sampling_number:
			reservoir_array[position_to_be_replaced] = next_item

	iteration+=1

#using the standard output

sys.stdout.write(''.join(map(str, reservoir_array)) + '\n')


