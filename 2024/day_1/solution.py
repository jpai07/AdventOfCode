import argparse

class Solution:
	filename_real_input = 'real_input.txt'
	filename_test_input = 'test_input.txt'
	
	def __init__(self, test=False):
		self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
		self.lines = self.file.splitlines()
		self.group1_ids, self.group2_ids = [], []

	
	def part1(self):
		"""
		Calculates the distance (difference)
		of smallest id pairs and returns the
		summed distance
		
		rtype: int
		"""

		self.populate_group_lists()

		# sort the lists in ascending order -> O(logn)
		self.sort_asc(self.group1_ids, self.group2_ids)

		# track the total distance
		total_dist = 0

		# O(n)
		for i in range(len(self.group1_ids)):
			# find the distance of both groups' smallest 
			dist = abs(self.group1_ids[i] - self.group2_ids[i])
			# update total distance
			total_dist += dist

		return total_dist

	
	def part2(self):
		"""
		Calculates simlarity score between lists
		and returns the total score
		
		rtype: int
		"""

		# k=id, v=id * freq
		uniq_scores_map = {}
		similarity_score = 0

		# ensure lists are empty before populating
		if not self.group1_ids and not self.group2_ids:
			self.populate_group_lists()
		
		for i in range(len(self.group1_ids)):
			# id numbers represent the keys
			k = self.group1_ids[i]

			# check if the id is hashed
			if not k in uniq_scores_map:
				# count the frequency of id in group 2's list
				id_count = self.group2_ids.count(k)
				
				# calculate the score and store it in the map -> k=id, v=score
				score = k * id_count
				uniq_scores_map[k] = score

			# update score
			similarity_score += uniq_scores_map[k]

		return similarity_score
		

	def populate_group_lists(self):
		# O(n)
		for line in self.lines[:]:
			# one row of location IDs, ignore whitespace
			pair = line.split(maxsplit=1)
			self.group1_ids.append(int(pair[0]))
			self.group2_ids.append(int(pair[1]))


	def sort_asc(self, *lists):
		for list in lists:
			list.sort()  
		

if __name__ == '__main__':
	parser = argparse.ArgumentParser('Solution file')
	parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
	parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
	args = parser.parse_args()
	test = True if args.test in ['True','true'] else False
	solution = Solution(test=test)
	result = solution.part1() if args.part == 1 else solution.part2()
	print(f'Result for Part=={args.part} & Test=={test} : {result}')
