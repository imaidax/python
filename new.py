def main():

    while(True):
        file_name = input('Please enter the file name or type QUIT to exit:\n')
        file_name = file_name.lower() # I added this to simplify the quit string. I originally had many boolean cases ie 'QUIT' or 'QuiT'. 
    #open homework input file
        if(file_name == 'quit'):
            break; 
        else:
            try:
                hw_file = open(file_name, 'r')
                line_count = 0
                total = 0
                #read lines
                
                for line in hw_file:
                    line_count += 1 #needed to count lines for empty file or dividing.
                    total += float(line)
                    
                if(line_count < 1): # checks to see if file is empty. If it is, return message saying it's empty
                    print('File:', file_name, 'is empty.')
                    
                else: #if it's not, print total of integers and the average, using the counter as the dividing value.
                    print('Total:',format(total, '.3f'))
                    hw_file.close()
                    print('Average:',format(total/line_count, '.3f'))
            except:
                print("File:", file_name, "does not exist.")
main()
