# examples of nested function
def outer_function(t: str):
    text: str = t

    def inner_function():
        print(text)

    inner_function()

outer_function('Hello!') # read parent's parameter 'text'

# using operator
def outer_function(a):
    b: List[int] = a
    print(id(b), b)

    def inner_function1():
        b.append(4) # event
        print(id(b), b)

    def inner_function2():
        print(id(b), b) # applied to parents function

    inner_function1()
    inner_function2() # no id change

outer_function([1, 2, 3])

# re-allocate
def outer_function(t: str):
    text: str = t
    print(id(text), text)

    def inner_function1():
        text = 'World' # constant object (string) re-allocating
        print(id(text), text) # changed id

    def inner_function2():
        print(id(text), text)

    inner_function1()
    inner_function2()

outer_function('Hello!')
