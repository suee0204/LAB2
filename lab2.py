def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67,32)")
    return

def get_user_input():
    theinput = str(input())
    thelist = theinput.split(",")
    thelist = [float(num.strip()) for num in thelist]
    return thelist

display_main_menu()
thelist = get_user_input()
print(thelist)

def calc_average_temperature(thelist):
    average = sum(thelist) / len(thelist)
    print(average)
    return

def find_min_max(thelist):
    maxlist = max(thelist)
    minlist = min(thelist)
    maxminlist = list[minlist, maxlist]
    print(maxminlist)
    return

def sort_list(thelist):
    sortedlist = sorted(thelist)
    print(sortedlist)
    return sortedlist

def median_list(thelist):
    import statistics
    medianlist = statistics.median(thelist)
    print(medianlist)
    return
calc_average_temperature(thelist)
find_min_max(thelist)
sortedlist = sort_list(thelist)
median_list(sortedlist)