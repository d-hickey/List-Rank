List Rank
==============

I wanted to rank a list I had and the first two results on Google didn't help so I made this.

### To run:
Have python installed and run the file listcompare.py


### To use:
Enter a file path for a text file containing the list of items, with each item on its own line.
No empty lines please because I didn't set the script up to deal with those.
A sample input "fruit.txt" is available.
HOT TIP: put your text file in the directory you are running the script from so you don't have to enter full file path.

You will be given a choice between two items on the list, enter the number associated with the item you rank higher.
This process will continue until the script has a unique rank for every item in the list.

### Algorithm:
I didn't put too much thought into the algorithm so there's almost certainly a better way to do this.
Every item is put into a Dictionary as keys, all with the same initial value: the amount of items in the list.
When an item wins a comparision it's value is lowered by one, advancing it in rank.
For each rank every item with that value will be compared until there's only one with that value.
The program then moves onto the next rank.

To avoid users having to answer the same question multiple times, a History of comparisons is stored in the format Winner&Loser
If the program is due to compare two items that are already in the History it will take the result from the History instead of querying the user.

When the rank level is advanced the program expands the History by assuming that if an item has beat a second item, it would also beat all of the items the second item has beat.
e.g. Winner1&Loser1 Winner2&Loser2 -> if Loser1 is equal to Winner2 then a new entry is made: Winner1&Loser2
I'm not sure this is an entirely fair assumption to make, but it can significantly reduce the amount of queries the user has to answer.

### Improvements/To-Do:
Delete empty lines
Randomise Dict so choice order isn't always the same
Output to file
Make GUI