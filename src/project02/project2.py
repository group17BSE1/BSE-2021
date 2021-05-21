file_input = open('measles.txt', 'r')
year= input('enter the year')
file_out = input('enter output file:')
output_file = open('file_out', 'w')
for line in file_input:
    if year==line[88:88+len(year)]:
        output_file.write(line)
    elif year==("","all","ALL"):
        output_file.write(line)


output_file.close()
file_input.close()
