# Loops in Python

## For Loops in Python

### Loop through a collection

```
for name in ['Christopher', 'Susan']:
    print(name)
```

### Looping a number of times

```
for index in range(0, 2):
    print(index)
```

## While Loop

### Looping with a condition

```
names = ["Christopher", "Susan"]
index = 0
while index < len(names):
    print(names[index])
    # Change the condition!
    index = index + 1
```

NOTE: It is ideal to use a for loop when iterating over strings.

A while loop is ideally used in situations where something will change automatically.