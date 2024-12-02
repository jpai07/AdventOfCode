# --- Day 2: Red-Nosed Reports ---

Fortunately, the first location The Historians want to search isn't a long walk from the Chief Historian's office.

While theRed-Nosed Reindeer nuclear fusion/fission plantappears to contain no sign of the Chief Historian, the engineers there run up to you as soon as they see you. Apparently, theystilltalk about the time Rudolph was saved through molecular synthesis from a single electron.

They're quick to add that - since you're already here - they'd really appreciate your help analyzing some unusual data from the Red-Nosed reactor. You turn to check if The Historians are waiting for you, but they seem to have already divided into groups that are currently searching every corner of the facility. You offer to help with the unusual data.

The unusual data (your puzzle input) consists of manyreports, one report per line. Each report is a list of numbers calledlevelsthat are separated by spaces. For example:

```shell
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
```
This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports aresafe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

In the example above, the reports can be found safe or unsafe by checking those rules:

So, in this example,2reports aresafe.

Analyze the unusual data from the engineers.How many reports are safe?

