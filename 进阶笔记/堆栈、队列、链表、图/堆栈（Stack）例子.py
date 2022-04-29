def balanced(expression):
    # your code goes here
    list = []
    # print(expression)

    for i in expression:
        if i == "(":
            list.insert(0, i)

        if i == ")":
            if list==[]:
                return False
            else:
                list.pop(0)

    if len(list) == 0:
        return True
    else:
        return False

print(balanced(input()))