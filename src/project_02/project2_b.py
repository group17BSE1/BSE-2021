"""The program in “project2_b.py” will display one summary report to the user according to the
year and income level entered"""


def open_file():
    while True:
        file_name = input("Enter input file name: ")
        try:
            fhand = open(file_name, "r")  # Opens the file in read mode and stores it the variable measles
            break
        except:  # When the user enters a wrong year, he is re-prompted until a valid file name is entered
            print("Couldn't open file. Invalid name or file doesn't exist!")
            continue  # re-prompts for an existing or valid file name.
    return fhand


def process_file(fhand):
    while True:
        year = input("Enter year: ")
        if len(year) == 4:  # The year has four characters else an error message pops up.
            break
        else:  # When the user enters a wrong year, he is re-prompted until a valid year is entered
            print("Year must be four digits,please enter a valid year!!")
            continue
    while True:  # Prompt the user for income level
        print("Income levels;\n Input 1 for WB_LI\n Input 2 for WB_LMI\n Input 3 for WB_UMI\n Input 4 for WB_HI")
        income = input("Enter income level>> ")
        if income == "1":
            income = "WB_LI"
            break
        elif income == "2":
            income = "WB_LMI"
            break
        elif income == "3":
            income = "WB_UMI"
            break
        elif income == "4":
            income = "WB_HI"
            break
        else:
            print("Invalid income level!!")  # if an income level other than (1,2,3,4) is input
            continue

    count = 0
    percentages = []
    countries = []
    for line in fhand:
        if (line[88:92] == year) and (line[51:56] == income or line[51:57] == income):
            count += 1
            percentages.append(int(line[59:61]))  # For each line met,add percentages to the percentages list.
            country = ((str(line[0:51])).strip())
            countries.append(country)  # adds percentages to the list of countries
            continue
    """Create a dictionary with country as the key and percentages as  the value."""
    country_percentage = dict(zip(countries, percentages))
    """The count of records in the input file which match the user’s criteria
The average percentage for those records (displayed with one fractional digit)
The country with the lowest percentage for those records
The country with the highest percentage for those records"""

    if count > 0:
        percent_sum = sum(percentages)
        average = percent_sum / count
        maximum = max(percentages)
        minimum = min(percentages)

        # this gets countries for maximum percentages to this list
        country_maxm = [country for country, percentage in country_percentage.items() if percentage == maximum]
        # this gets countries for minimum percentages to this list
        country_minm = [country for country, percentage in country_percentage.items() if percentage == minimum]

        print(f"Number of countries in the record: {count}")
        print(f"Average percentage for {year} with {income} is {average:.1f}%")

        print(f"The following countries have the maximum percentage in {year} with {income} of {maximum}%")
        for i in country_maxm:
            print("   -", i)  # This prints the countries with maximum percentage.
        print(f"The following countries have the minimum percentage in {year} with {income} of {minimum}%")
        for i in country_minm:
            print(" -", i)  # This prints the countries with minimum percentage.

    else:  # if there is no item in the list, it prints this
        print(f"There are no records for the year {year} in the file")


def main():  # invoke the open_file and process_file functions and then close them.
    fhand = open_file()
    process_file(fhand)
    fhand.close()


main()
