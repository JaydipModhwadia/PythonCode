def hello_three_times (a):
    print("")
    return "Hello", a + "\n" + "Hello",  a + "\n" + "Hello", a + "\n"
x=input("Enter Your Name\n")
x=str(x)
print(hello_three_times(x))
