#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    try:
        new_list.append(my_list1 / my_list2)
    except ZeroDivisionError:
        new_list.append(0)
        print('division by zero')
        continue
    except TypeError:
        new_list.append(0)
        print('wrong type')
        continue
    except IndexError:
        new_list.append(0)
        print('out of range')
        continue
    finally:
        pass
return new_list
