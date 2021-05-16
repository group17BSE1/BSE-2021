str = 'X-DSPAM-Confidence:0.8475'
colon = str.find(':')
extract = str[colon + 1:]
print(extract)
converted = float(extract)
print('the float value =', converted)
