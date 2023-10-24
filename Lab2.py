def display_main_menu():
    print("1. average temp")
    print("2. min/max temp")
    print("3. sorted temp")
    print("4. median temp")


def get_user_input():
    user_in = input()
    user_in = user_in.split(",")
    result = []
    for u in user_in:
        result.append(float(u))
    return result


def calc_average(x):
    result = 0
    for i in x:
        result += i
    result /= len(x)
    return result


def find_min_max(x):
    min = x[0]
    max = x[0]
    for i in x:
        if i < min: min = i
        if i > max: max = i
    result = [min, max]
    return result


def sort_temperature(x):
    return sorted(x)


from statistics import median


def calc_median_temperature(x):
    return median(x)


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    print("Please enter some temperature values")
    print(">> ", end="")
    num_list = get_user_input()
    display_main_menu()
    print(">> ", end="")
    choice = int(input())
    if choice <= 0 and choice > 4:
        print("Invalid choice!")
        return
    funcs = [calc_average, find_min_max, sort_temperature, calc_median_temperature]
    result = funcs[choice-1](num_list)
    print("Result:" + str(result))

if __name__ == "__main__":
    main()
