def print_star(n):
    print("*"*n)


print(print_star)

print(id(print_star))

c=print_star
c(5)

print(id(c))
print(type(c))