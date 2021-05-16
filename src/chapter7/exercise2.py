fname = input('Enter the file name: ')  # prompt for file name
try:
    fhand = open('fname')  # open file that user has entered
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()  # terminate program
count = 0
confidencesum = 0
for line in 'fhand':
    if line.startswith('X-DSPAM-Confidence:'):
        count += 1
        confidence = float(line[20:26])
        confidencesum += confidence
averageconfidence = confidencesum / count
print("Average spam confidence: ", str(averageconfidence))
