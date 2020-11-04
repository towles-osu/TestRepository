#stew
#example of issues of assignment and mutability

#example 1
def example_1_immutable():
    example_immutable = [(1,1),(2,2),(3,3),(4,4)]
    copy_example_list = example_immutable
    copy_example_element = example_immutable[0]
    example_immutable[0] = (5,1)
    print(copy_example_list)
    print(copy_example_element)

def example_1_mutable_binding():
    example_mutable = [[1,1],[2,2],[3,3],[4,4]]
    copy_example_list = example_mutable
    copy_example_element = example_mutable[0]
    example_mutable[0] = [5,1]
    print(copy_example_list)
    print(copy_example_element)

def example_1_mutable_mutating():
    example_mutable = [[1,1],[2,2],[3,3],[4,4]]
    copy_example_list = example_mutable
    copy_example_element = example_mutable[0]
    example_mutable[0][0] = 5
    print(copy_example_list)
    print(copy_example_element)


example_1_immutable()
example_1_mutable_binding()
example_1_mutable_mutating()

#example 2
ingredients = [('salt',2),('flour',8),('water',8)]
salt = ingredients[0]
salt = ('salt',1)
print(ingredients)

#example 3
salt = ingredients[0]
ingredients[0] = ('salt', 1)
print(salt)
print(ingredients)

#example 4
def test_saltiness(list_ingr):
    """tests if recipe is too salty, changes saltiness to be at most 1/5 as much salt as flour"""
    #this will get stuck in an infinite loop and does not work
    salt = list_ingr[0]
    if list_ingr[1][1] // salt[1] < 5:
        #list_ingr[0] = (salt[0],salt[1] - 1)
        salt = (salt[0],salt[1] - 1)
        test_saltiness(list_ingr)
    #returns a value for printing test cases purposes
    return salt #list_ingr[0]

ingredients_2 = [('salt',2), ('flour', 8), ('water', 8)]
print("original ingredients are:", ingredients_2)
print("new saltiness is:", test_saltiness(ingredients_2))
#even if our method had not crashed because of infinite recursion, the following print would show that the ingredients
# in the list have not been changed. If our function had instead of creating a variable pointing to
# an object simply reassigned the value at the index then it would have worked
print("new ingredient list is:", ingredients_2)
