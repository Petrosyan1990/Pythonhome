# x = int(input("Enter your age-"))
# if x >= 20:
#     print("you can enter")
# elif x >= 18:
#     print("you can enter with mom")
# else:
#     print("it is not for you")


# def hello():
#     print("jfblsrnfnarjjf;anm;nv;jn;hgsngnzvz")

# hello()


# x = int(input("mutqagreq arajin tivy-"))
# y = int(input("mutqagreq erkrorq tivy-"))

# def sum(a,b):
#     return(a + b)
# z = sum(x,y)
# print(z)


# i = 1
# while i <= 10:
#     print(i)
#     i += 1


x = "a,2,b,5,c,6,e,11,a,67,c,8"
listOfX = x.split(",")
dict1 = {}
for i in range(0, len(listOfX), 2):
    key = listOfX[i]
    value = int(listOfX[i + 1])
    if key in dict1:
        dict1[key] += value
    else:
        dict1[key] = value


print(dict1)



