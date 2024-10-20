# Advent Of Code
![img](doc/img.png)

## 1. Backbone

Solutions for each day of a given year are grouped into a main folder *"YYYY"*. Each day solution has its given folder *"day_DD"* that contains : 
- *test.txt* : test input to validate code
- *input.txt* : final input to produce submission
- *instructions.txt* : explanation of the given day problem
- *solution.py* : python script for part 1 of the problem

```python
./2023 
├── day_1 
    ├── test.txt 
    ├── input.txt 
    ├── instructions.txt 
    ├── solution.py 
├── day_2 
...
├── day_25
.get_input.py
```

## 2. Usage

### 2.1. Config file

First, configure a **config.yml** giving values for website url, year, and session token : 

```yaml
url: https://adventofcode.com
year: '2022'
session: <enter session token here>
```

To get you session token, you need to follow these steps :
- go to the website and inspect page (keep it open)
- go to the "network" section in the inspector
- login and click to "login" request in the inspector (left side)
- check for subsection "cookies" in the "network" section in inspector (right side)
- get the "session" value and paste it as session in the "config.yml" file

### 2.2. Collect daily problem

After creation of the **config.yml** file, you can automatically collect the daily problem for a given day by running the following command in you terminal : 

```python
python3 get_input -d DD
```

where DD is the day you want to collect, for the year given in the config.
It will create the directory **YYYY/DD** with the foloowing files:
- ***instructions.txt*** : description of the problem and instructions
- ***input.txt*** : input file to solve the problem
- ***test.txt*** : example input test file to test your solution
- ***solution.py*** : python template file to fill with your solution

## 3. What did I learn in the past ?

### 3.1. Basic tools
- **logical operations** : *all(c for c in conditions)*, *any(c for c in conditions)* to check multiple conditions
- **numpy tools** : *np.flipud*, *np.fliplr* to get vertically/horizontally mirrored array
- **text files** : *.splitlines()*, *.read()*, *.readlines()*
- **list operations** : *map(function,list)* and *list.sort(key=lambda ...)*
- **string sequences** : *.split()*, *.lstrip()*, *.rstrip()*, *.replace()*
- **regular expressions** : find patterns with *re.findall*, *re.search* and *re.match*, *str.__contains__(expr)*
- **set** object : useful to deal with intersections, unions, difference

### 3.2. Packages 
- **[copy](https://docs.python.org/fr/3/library/copy.html)** : module *deepcopy* that allows to make a copy of an element completely detached from the original one (in terms of operations).
- **[heapq](https://docs.python.org/fr/3/library/heapq.html)** : combination of heap data type ("branch type") and deque (queue type operations). *heappop* to get the first element of the queue+ remove it from the queue at the same time. *heappush* to push a new element at the end of the queue. 
- **[collections](https://docs.python.org/fr/3/library/collections.html)** : modules such as *defaultdict* (dictionnary with enforced type), *Counter* (unique occurences,counts) *deque* (queue solving prolems with popleft, )
- **[itertools](https://docs.python.org/fr/3/library/itertools.html)** : *combinations*
- **[simpy](https://simpy.readthedocs.io/en/latest/)** : implement/solve list of equations
- **[networkx](https://networkx.org)** : graph construction, minimal cut problems

### 3.3. Methods
- **[recursion](https://www.programiz.com/python-programming/recursion)** is the process of defining a function in terms of itself. Helpful for branching/path searching problems.
- **[shoelace formula](https://en.wikipedia.org/wiki/Shoelace_formula)** allows to compute the area of a polygon given the list of its edges.
- **[Pick's Theorem](https://en.wikipedia.org/wiki/Pick%27s_theorem)** provides formula for the area of a polygon given the number of interior points and points on its boundary.
- **[Depth First Search](https://en.wikipedia.org/wiki/Depth-first_search)** is an algorithm for traversing or searching tree or graph data structures.
