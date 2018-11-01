x = 8
y = 0
a = "Hello!"
b = ""

print("first bullet:")
# Check if x and b are both true. If they are, print "Both of these are true.
if x and a:
    print("both of these are true.")

print("second bullet:")
# Check if y or a is false. If one is, print "One of these is false."
if (y== False) or (a == False):
    print("(at least) one of these is false")

print("third bullet:")
# Check if either x or y is false. If one is, print out "One is false."
if (x==False) or (y == False):
    print("one of these is false.")

#the back slash eliminates the code error indicating the extra line
#indent here is optional

print("fourth bullet:")
if x or y :
    if (x == False) or ( y == False):
        if x > y:
            print("x is greater than y.")
