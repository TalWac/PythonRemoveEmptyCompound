

# https://stackoverflow.com/questions/14849293/python-find-index-position-in-list-based-of-partial-string
# https://stackoverflow.com/questions/2400840/python-finding-differences-between-elements-of-a-list


#  option 1 from
# https://stackoverflow.com/questions/66088913/how-to-conditionally-remove-sequence-of-rows-from-txt-file-using-python/66089688?noredirect=1#comment116873503_66089688
# Open / read tmp file created with the text you supplied
filedat = open('D:\CD_Production\Libraries\MS-DIAL\MSMS-Public-Pos-VS15.msp','r')
filelines = filedat.readlines()

# Open output file object
file_out = open('D:\CD_Production\Libraries\MS-DIAL\z.msp','w')

line_count = 0

# Iterate through all file lines
for line in filelines:
    # If line is beginning of section
    # reset tmp variables
    if line != "\n" and line.split()[0] == "NAME:":
        tmp_lines = []
        flag = 'n'

    tmp_lines.append(line)
    line_count += 1

    # If line is the end of a section and peaks > 0
    # write to file
    if (line == "\n" or line_count == len(filelines)) and flag == 'y':
        #tmp_lines.append("\n")
        for tmp_line in tmp_lines:
            file_out.write(tmp_line)

    # If peaks > 0 set flag to "y"
    if line != "\n" and line.split()[0] == "Num":
            if int(line.split()[2]) != 0:
                flag = "y"

file_out.close()


#  option 2
# with open('D:\CD_Production\Libraries\MS-DIAL\MSMS-Public-Pos-VS15_Partially_Clean.msp') as f:
count_name=0
with open('D:\CD_Production\Libraries\MS-DIAL\MSMS-Public-Pos-VS15_1.msp', 'w') as output1,\
        open('D:\CD_Production\Libraries\MS-DIAL\MSMS-Public-Pos-VS15_2.msp', 'w') as output2,\
        open('D:\CD_Production\Libraries\MS-DIAL\MSMS-Public-Pos-VS15_3.msp', 'w') as output3,\
        open('D:\CD_Production\Libraries\MS-DIAL\MSMS-Public-Pos-VS15.msp') as f:
    line_cache = []
    for line in f:
        if line.startswith('NAME:'):
            count_name+=1
            if line_cache:
                if count_name<=100000:
                    print(*line_cache, sep='', file=output1)
                    # print(*line_cache, sep='')
                    line_cache = []
                elif count_name<=200000:
                    print(*line_cache, sep='', file=output2)
                    # print(*line_cache, sep='')
                    line_cache = []
                elif count_name<=300000:
                    print(*line_cache, sep='', file=output3)
                    # print(*line_cache, sep='')
                    line_cache = []
        elif line.startswith('Num Peaks:'):
            num_peaks = int(line.partition(': ')[2])
            if num_peaks == 0:
                line_cache = []
                continue

        if line.strip():        # filter empty lines
            line_cache.append(line)

    if line_cache:    # don't forget the last record
        if count_name <= 100000:
            print(*line_cache, sep='', file=output1)
            # print(*line_cache, sep='', end='')
        elif count_name <= 200000:
            print(*line_cache, sep='', file=output2)
            # print(*line_cache, sep='')
            line_cache = []
        elif count_name <= 300000:
            print(*line_cache, sep='', file=output3)





#  https://stackoverflow.com/questions/18970761/read-text-file-into-a-list-of-dictionaries-in-python




# https://stackoverflow.com/questions/30677334/how-to-save-a-dictionary-to-a-file-with-key-values-one-per-line

