def main():
	# write your code here
	time = int(input("Enter the time: "))
	
	items=input("enter name of items: ")
	
	name= input("Enter a name: ")
	scream = input("Enter the scream: ")
	action = input ("What action!: ")

	print ("It was %d o'clock when I heard a knock at the door.\nI opened the door and there was a box full of %s with a note saying \" From Mr. %s.\"\nJust as I closed the door I heard a scream\"%s.\"\nI froze in place and all I could do was %s"%(time, items, name.title(), scream.upper(), action))



if __name__ == '__main__':
	main()
