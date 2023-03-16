#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        message = None
        try:
            result.append(my_list_1[i]/my_list_2[i])
        except TypeError:
            message = "wrong type"
            result.append(0)
        except ZeroDivisionError:
            message = "division by 0"
            result.append(0)
        except IndexError:
            message = "out of range"
            result.append(0)
        finally:
            if message:
                print(message)
    return result
