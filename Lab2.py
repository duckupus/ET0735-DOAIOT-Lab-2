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
    print("sort_temperature")
    return

def calc_median_temperature():
    print("calc_median_temperature")
    return

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()

if __name__ == "__main__":
    main()
