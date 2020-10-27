#Stew
#Activity for class
def cumsum(numbers):
    for i in range(len(numbers)):
        if i == 0:
            continue
        numbers[i] = numbers[i] + numbers[i-1]
    return numbers


# def cum_sum(numbers):
#     new = numbers
#     if len(numbers) > 0:
#         new = numbers[:-1]
#         new[len(new)] = cum_sum(new)[-1] + numbers[-1]
#     return new

print(cumsum([1,2,3,4,5]))

#but how to do it with a comprehension