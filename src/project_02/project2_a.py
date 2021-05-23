"""The program in “project2_a.py” will copy selected lines from “measles.txt” into a
file selected by the user"""
try:
    file = open('measles.txt', 'r')  # open measles.txt in a reading mode.
    # prompt for the year of reference and output file where to save the text.
    yr_prompt = input('Enter year of reference>>')
    file_out = input('Enter file to save data to>>')
    if '.txt' in file_out:  # if file has the extension skip the else clause and execute the other code lines
        pass
    else:
        print('Error,output file should have [.txt] extension,re-run!!')  # output file should have an extension
        exit()
    file_saved = open(file_out, 'w')
    for line in file:
        if (yr_prompt == " ") or (yr_prompt.lower() == "all"):
            file_saved.write(line)  # This is to add data to the new file created.
        elif line[88:].startswith(yr_prompt):  # year field begins at index 88 and beyond.
            file_saved.write(line)  # This is to add data to the new file created.
    file_saved.close
    file.close
except FileExistsError:
    print("Couldn't open file")
