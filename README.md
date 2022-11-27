# Requirements

Python 3.7


# Usage
If you use:
```
python3 main.py -r 200
```
the following answer will be displayed:
```
CC
```

and if you try arabic param
```
python3 main.py -a 200
```
then
```
Not implemented yet
```

# Notes
To reverse the list
```
l = l[::-1]
```
(main.py l21)

We use a while loop because we don't know how many times.
```
    while nb != 0:
```
(logic.py l25)


The iterator is incremented only if the current number cannot be reused.
```
if not(nb >= l[i].get_arabic()):
        if i < len(l)-1:
            i += 1
```
(logic.py l33)


Constants are used to facilitate the use

Using an object can be interesting because there are several ways to write big Roman Numbers; This is also a limit to this script..
Also we can imagine a method to display with a specific formatting.
