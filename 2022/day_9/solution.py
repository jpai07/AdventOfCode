import argparse

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  def __init__(self, test=False):
    self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
    self.lines = self.file.splitlines()
    self.visited = set()
    self.visited.add((0,0))
    self.head_coords = (0,0)
    self.tail_coords = (0,0)
    self.directions_deltas = {'L':(0,-1),'R':(0,1),'U':(-1,0),'D':(1,0)}
    
    for line in self.lines:
      direction, steps = line.split(' ')
      steps = int(steps)
      for _ in range(steps):
        last_head_position = self.head_coords
        self.head_coords = tuple(map(lambda c1,c2: c1+c2, self.head_coords, self.directions_deltas[direction]))
        print(self.head_coords)
        print(self.tail_coords)
        print('')
        if abs(self.head_coords[0]-self.tail_coords[0])>=2 or abs(self.head_coords[1]-self.tail_coords[1]) >=2:
          self.tail_coords = last_head_position
          self.visited.add(self.tail_coords)

    print(self.visited)
    
  def display(self):
    xs = [c[0] for c in list(self.visited)]
    ys = [c[1] for c in list(self.visited)]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    for x in range(min_x, max_x+1):
      line = ''
      for y in range(min_y, max_y+1):
        if (x,y) in self.visited:
          line += '#'
          continue
        line += '.'
      print(line)
      print('\n')
        
  def part1(self):
    self.display()
    return len(self.visited)
  
  def part2(self):
    pass
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
