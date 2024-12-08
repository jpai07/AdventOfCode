import argparse

class Solution:
	filename_real_input = 'real_input.txt'
	filename_test_input = 'test_input.txt'
  
	def __init__(self, test=False):
		self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
		self.lines = self.file.splitlines()
	
	def part1(self):
		# report -> one row of data
		# level -> one number in one report's list; one report contains multiple levels
		# reports can be safe/unsafe; track and return the number of safe reports
		# safe: levels in one report are all unique and increasing or decreasing 

		# Class attributes
		# print(self.file)
		# print(self.lines) # List 
		# print(self.lines[0]) # String

		safe_reports = 0

		for report in self.lines:
			report = list(map(int, report.split())) # List
			report_zipped_list = list(zip(report, report[1:])) # Iterator to List

			print("Tuple Pairs")
			print(report_zipped_list)
			print()
			

			lvls_inc = self.pair_strictly_increasing(report_zipped_list)
			lvls_dec = self.pair_strictly_decreasing(report_zipped_list)
			# lvls_eq = self.pair_is_equal(report_zipped_list)
			x = self.all_equal(lvls_inc) and self.all_equal(lvls_dec)
			lvls_monotonic = [a or b and x for a, b in zip(lvls_inc, lvls_dec)]

			# lvls_monotonic = [l and self.all_equal(lvls_inc) and self.all_equal(lvls_dec) for l in lvls_monotonic]

			print(lvls_inc)
			print(lvls_dec)
			# print(lvls_eq)
			print("ORIG: ", [a or b for a, b in zip(lvls_inc, lvls_dec)])
			print("      ", lvls_monotonic) # use this version
			# print()

			# abs(a - b) for a, b in report_zipped_list
			# list(i > 0 and i < 4 for i in res2)
			lvls_dist = self.calculate_pair_distance(report_zipped_list)
			lvls_safe_dist = self.pair_safe_distance(lvls_dist)

			# print(lvls_dist)
			# print(lvls_safe_dist)
			# print()

			print("Bitch you better!")
			# if its all inc or all dec, then or with the one that is true, otherwise don't or
			if lvls_inc[0] == True:
				# strictly inc -> linear
				lvls_monotonic = [a or b for a, b in zip(lvls_monotonic, lvls_inc)]
			elif lvls_dec[0] == True:
				# strictly dec -> linear
				lvls_monotonic = [a or b for a, b in zip(lvls_monotonic, lvls_dec)]
			else:
				# non-linear
				lvls_monotonic = [a or b or c for a, b, c in zip(lvls_monotonic, lvls_inc, lvls_dec)]

			print("      ", lvls_monotonic)
			print()

			res = self.all_equal([a and b for a, b in zip(lvls_monotonic, lvls_safe_dist)])
			print(f"Safe report = {res}")
			print()

			
			# each element is a tuple, where the first element is a bool returned 
			# by a < b and the second element is the absolute value of a - b			
			ab_res = [] 

			for pair in report_zipped_list:
				# access first and second elements in tuple pair
				a, b = pair
				ab_res.append((a < b, abs(a - b))) # return here
			
			# res1 -> tuple of all bools returned by a < b
			# res2 -> tuple of all returned by abs(a - b)
			res1, res2 = list(zip(*ab_res))

			monotonic = self.all_equal(res1)
			# check if adjacent elements in list differ by at least 1 and at most 3
			safe_difference = self.all_equal(list(i > 0 and i < 4 for i in res2)) # make this into a list of bools

			# decrease the safe reports count if either of these conditions are false
			if not monotonic or not safe_difference:
				safe_reports -= 1
			
			# assume reports are safe unless detected unsafe otherwise
			safe_reports += 1
		
		print(f"Safe reports {safe_reports}")
		return safe_reports
	
  
	def part2(self):
		safe_reports = 0

		report_num = 1
		for report in self.lines:
			print("Report #" + str(report_num))

			report = list(map(int, report.split())) # List
			report_zipped_list = list(zip(report, report[1:])) # Iterator to List

			print(report)
			print()
			# print("Tuple Pairs")
			# print(report_zipped_list)
			# print()
			
			# each element is a tuple, where the first element is a bool returned 
			# by a < b and the second element is the absolute value of a - b			
			ab_res = [] 

			for pair in report_zipped_list:
				# access first and second elements in tuple pair
				a, b = pair
				ab_res.append((a < b, abs(a - b)))
			
			# res1 -> tuple of all bools returned by a < b
			# res2 -> tuple of all returned by abs(a - b)
			res1, res2 = list(zip(*ab_res))

			# print("a < b")
			# print(list(res1))
			# print()

			# print("abs(a - b)")
			# print(list(res2))
			# print()

			monotonic = self.all_equal(res1)
			# if booleans are all False or all True, convert booleans to all True
			if monotonic: 
				# print("res1 all same")
				res1 = [True for bool in res1]

			# print("a < b")
			# print(res1)
			# print()

			# convert to list of bools, applying the condition if adjacent 
			# elements in list differ by at least 1 and at most 3
			res2 = list(i > 0 and i < 4 for i in res2[:]) 

			# print("abs(a - b) T/F")
			# print(res2)
			# print()

			##############################
			# res1 & res 2 -> List[bool] #
			##############################

			print("res1:", res1)
			print("res2:", res2)
			print()


			print("Anded")
			print([a and b for a, b in zip(res1, res2)])
			print()

			# print("all_equal(res1 or res2) SAFE")
			if self.all_equal([a and b for a, b in zip(res1, res2)]): # and
				print("SAFE")
			else:
				print("UNSAFE")
			print()

			if self.all_equal([a and b for a, b in zip(res1, res2)]):
				safe_reports += 1

			# decrease the safe reports count if either of these conditions are false
			# if not monotonic or not safe_difference:
				# safe_reports -= 1
			
			# assume reports are safe unless detected unsafe otherwise
			# safe_reports += 1
			
			report_num += 1
			print("------------------------------------")
			print()
		
		print(f"Safe reports {safe_reports}")
		return safe_reports


	def all_equal(self, items):
		"Returns True if all elements in the list are the same"
		return all(item == items[0] for item in items)
	
	
	def pair_strictly_increasing(self, levels):
		return [a < b for a, b in levels]
	

	def pair_strictly_decreasing(self, levels):
		return [a > b for a, b in levels]
	
	
	def pair_is_equal(self, levels):
		return [a == b for a, b in levels]


	def calculate_pair_distance(self, levels):
		return [abs(a - b) for a, b in levels]


	def pair_safe_distance(self, dist):
		return list(i > 0 and i < 4 for i in dist)


	
	# def set_all_True(self, bools):
	# 	for i in range(len(bools)):
	# 		bools[i] = True
  
if __name__ == '__main__':
	parser = argparse.ArgumentParser('Solution file')
	parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
	parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
	args = parser.parse_args()
	test = True if args.test in ['True','true'] else False
	solution = Solution(test=test)
	result = solution.part1() if args.part == 1 else solution.part2()
	# print(f'Result for Part=={args.part} & Test=={test} : {result}')
