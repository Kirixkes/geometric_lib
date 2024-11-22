import circle
import square

figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
	assert fig in figs
	assert func in funcs

	if not (fig == "circle" or fig == "square"):
		print("Wrong shape type")
		return -1

	if not (func == "area" or func == "perimeter"):
		print("Wrong function name")
		return -1

	if not isinstance(*size, (int, float)):
		print("Wrong size type")
		return -1

	result = eval(f'{fig}.{func}(*{size})')
	return (f'{func} of {fig} is {result}')

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	print(calc(fig, func, size))



