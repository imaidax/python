def main():

    while(True):
        file_name = input('Please enter the file name or type QUIT to exit:\n')
        file_name = file_name.lower() # I added this to simplify the quit string. I originally had many boolean cases ie 'QUIT' or 'QuiT'.
    #open homework input file
        if(file_name == 'quit'):
            break;
        else:
            try:
                readmath(file_name)
            except:
                print("File:", file_name, "does not exist.")
main()

def readmath(file):
    hw_file = open(file, 'r')
    line_count = 0
    total = 0
    #read lines
    for line in hw_file:
        line_count += 1 #needed to count lines for empty file or dividing.
        total += float(line)
        if(line_count < 1):
            print('File:', file, 'is empty.')
    else:
            print('Total:',format(total, '.3f'))
            hw_file.close()
            print('Average:',format(total/line_count, '.3f'))
