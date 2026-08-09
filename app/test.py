# def hello():
#     print("hello hi")

# hello()
# -----------
# ok so conclusion is if i print something then none(without returnnig values) else calling only function without print it wont print none
# def greet(name):
#     print("hello",name)
#     # return 'hello',name
# greet("alice")
# x = greet("alice")
# print(x)



# def test(a=9,b=8):
#     return a*b
# print(test())


# def test(*args, **kwargs):
#     total = sum(args)
#     print("total",total)
#     print("Extra info",kwargs)

# test(0,1,2,4,user = "sai", role = "admin")

# def test(a, b, c):
#     print(a, b, c)

# values = (10, 20, 30)

# test(*values)


def main(api):
    return api
d = main("hi")
print(d)