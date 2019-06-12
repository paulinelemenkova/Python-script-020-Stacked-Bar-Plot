# 0. Polina's_EXAMPLE: automatic numbering for profiles 1 to 25.
mylength = range(1,26)
for i in range(len(mylength)):
    print("Profile {}".format(i + 1, mylength[i]))

////////////////////////////////////////////////////////////////

# 1. Python For Loop for Numbers.
# Don’t forget to specify the colon [:] at the end of for loop line. This is part of the syntax.
# For every for loop iteration, each value is picked-up from the list and stored in the variable given in the for loop. In this example, the variable is “x”.
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step
for x in my_range(1, 5, 1):
    print (x)

# 2. Python For Loop for Strings. Here we are looping through the three names and printing them out one by one. “names” – This is the variable which has a list that in-turn contains three string items.
names = ["john", "raj", "lisa"]
for i in names:
    print(i)

# 3. Python For Loop Using Default Range Function. if you specify range(x), make sure you pay attention to the fact that range function by default will always start with number 0, and then generate “x” number of numbers.
for i in range(5):
    print(i)

# 4. Python For Loop With Custom Start and End Numbers. this will start with number “1”. But, the value the above will print will be only 5 (and not 6). For a sequence of 1 .. n, then your range should be: range(1,n+1). So, in this example, we wanted sequence from 1 .. 5 and we gave range as range(1,6). i.e the end value is n+1.
for i in range(1,6):
    print(i)

# 5. Python For Loop With Incremental Numbers. In the following example, we are generating numbers from 1 through 6 with a increment of 2.
for i in range(1,6,2):
    print(i)

# 6. Python For Loop Range with Negative Values
for i in range(4,-5,-2):
    print(i)

# 7. Continue Statement Inside Python For Loop. When a for loop encounters “continue”, it will not execute the rest of the statements in that particular for-loop-block, instead it will start the for-loop again for the next element in the list.
# Т.е. если элемент не равен Лизе - бросаем его и проходим дальше искать Лизу.
# если элемент равен Лизе - выводим его.
# continue подходит для "отыскать всех 'n'"
names = ["john", "lisa", "james", "lisa"]
for i in names:
    if i != "lisa": continue
    print(i)
# Out / получится 2 Лизы:
#lisa
#lisa

# 8. Break Statement Inside Python For Loop
# выскочить из цикла принудительно
# здесь: как только доходим до "james" - выскакиваем.
names = ["john", "lisa", "james", "lisa"]
for i in names:
    if i == "james": break
    print(i)
# Output:
#john
#lisa

# 9. Can a For Loop itself have an Else without If? This is a unique feature to Python.
names = ["john", "raj", "lisa"]
for i in names:
    print(i)
else: print("for loop condition failed!")

#10. Else and Break Combination Behavior Inside Python For. One important thing to understand is that when you have a “break” statement inside your for-loop-block, then the “else” part will not be executed.
names = ["john", "lisa", "raj", "lisa"]
for i in names:
    if i == "raj": break # доходим до 'raj', цикл прекращен.
    print(i)
else:
    print("for loop condition failed!")
    print("--end--")
# Out:
#john
#lisa
# the print command inside the “else” did not get executed this time, because the for loop encounterd a “break” and came-out of the loop in-between.

# 11. Nested For Loops in Python
distros = ["centos", "redhat", "ubuntu"]
arch = ["32-bit", "64-bit"]
for i in distros:
    for j in arch:
        print(i + " " + j)
        print("-----------")

# 12. 12. Handling List-of-Lists in Python For Loop
# list of lists inside for loop.
multiple_state_lists = [ ["CA","NV","UT"], ["NJ","NY","DE"]]
for state_list in multiple_state_lists:
    for state in state_list:
        print (state)

# 13. Loop using enumerate()
my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list):
    print(idx, val)

# 14.
elements = (['foo', 'bar', 'baz'])
for elem in elements:
    print (elem)
#
for item in enumerate(["a", "b", "c"]):
    print (item)

# 15.
letters = ['a']
for i in range(len((1,26))):
    letter = letters[i]
    print (i, letter)

# 16. Enumerate a Tuple
t = ('apples', 'bananas', 'oranges')
for idx, val in enumerate(t):
# print("index is %d and value is %s" % (idx, val))
    print("%d %s" % (idx, val))
    print((idx, val))

# 17. while loop
colors = ["red", "green", "blue", "purple"]
i = 0
while i < len(colors):
    print(colors[i])
    i += 1

# 18. range of length
presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]
for i in range(len(presidents)):
    print("President {}: {}".format(i + 1, presidents[i]))
