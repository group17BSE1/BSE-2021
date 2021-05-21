"""fname = input('enter file name')
fh = open('fname')
s = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
        pos = line.find('0')
        s = sum + float(line[pos:pos+6])
        count = count + 1
print('Average spam confidence', sum / count)"""


def main():
    while True:
        try:
            input_file = open('measles.txt')
            break
        except:
            print('cant open file', input_file)
    while True:
        f2 = input('what is the name of the output file>>')
        try:
            output_file = open(f2, 'w')
            break
        except:
            print('error opening file', output_file)
            break
    year = str(input('input the year>>'))
    line = input_file.readline().strip()
    while line != "":
        for line in input_file:
            if year == line[88:88 + len(year)]:
                output_file.write(line)
            elif year in ("", "all", "ALL") or line.split()[-1].startswith(year):
                output_file.write(line)

        output_file.close()
        input_file.close()


main()
