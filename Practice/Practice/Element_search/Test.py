def find(my_list,new_element):
    for element in my_list:
        if element == new_element:
            return True
        return False


    if __name__ == "__main__":
        l = [2, 4, 6, 8, 10]
        print(find(l, 5))  # prints False
        print(find(l, 10))  # prints True
        print(find(l, -1))  # prints False
        print(find(l, 2))  # prints True