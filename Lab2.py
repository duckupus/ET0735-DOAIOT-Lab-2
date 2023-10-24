def display_main_menu():
    print("Enter numbers seperated by commas. (e.g. 3, 45, 67")

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

def calc_median_temperature(x):
    x = sort_temperature(x)
    length = len(x)
    index = (length - 1) // 2
    result = 0
    if (length % 2) == 0:
        result = (x[length] + x[length + 1])/2.0
    else:
        result = x[length]
    return result

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()

if __name__ == "__main__":
    main()
