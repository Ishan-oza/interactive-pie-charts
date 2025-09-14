import matplotlib.pyplot as plt


def greeter() :
	print("              *-Hey There!-*\n*-So Today You Decided To Plot Pie Chart Haa-*\n")
	
	
def pie_p() :
	
	val_i = int(input("\nEnter the number of inputs for Labels: "))
	val_1 = [] 
	for i in range(val_i):
		a = input(f"label {i}: ")
		val_1.append(a)
		
	print("\n")
	val_2 = [] 
	for j in range(val_i):
		b = float(input(f"value {j}: "))
		val_2.append(b)
	
	explode = [0] * val_i  # no explode
	exp = input("\nDo You Want To Use Explode Effect (y/n): ")
	if exp == "y" :
		explode = []
		print("(b/w 0 and 1)")
		for k in range(val_i):
			c = float(input(f"Explode value {k} : "))
			explode.append(c)
		#plt.pie(val_2, labels=val_1, shadow=True, explode=explode)
	elif exp == "n" :
		print("Got That Bro...")
	else :
		print("Are You Mad Trying something Weird?")
	
	title_g = input("\nEnter graph's title: ")
	
	plt.title(title_g)
	plt.style.use("ggplot")
	
	res = input("\nDo You Want To Plot Percentage (y/n): ")
	if res == "y" :
		plt.pie(val_2, labels=val_1, shadow=True, autopct='%1.1f%%', explode=explode)
	elif res == "n" :
		plt.pie(val_2, labels=val_1, explode=explode, shadow=True)
	else :
		print("Are You Mad Tring something Weird?")
		return
	plt.show()



def select_plot():
	ans = input("Want To Plot ? (y/n): ")
	if ans == "y" :
		pie_p()
	elif ans == "n" :
		print("You Useless...")
	else :
		print("Are You Mad Tring something Weird?")
		return
greeter()
select_plot()

