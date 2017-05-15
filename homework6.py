Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: C:/Users/Aidax/Desktop/Python/readfilemath.py ===========
>>> main()
1.1
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    main()
  File "C:/Users/Aidax/Desktop/Python/readfilemath.py", line 10, in main
    hw_file.rstrip('\n')
AttributeError: '_io.TextIOWrapper' object has no attribute 'rstrip'
>>> 
=========== RESTART: C:/Users/Aidax/Desktop/Python/readfilemath.py ===========
>>> main()
1.1
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    main()
  File "C:/Users/Aidax/Desktop/Python/readfilemath.py", line 10, in main
    total += int(hw_file.readline())
ValueError: invalid literal for int() with base 10: '2.4\n'
>>> 
=========== RESTART: C:/Users/Aidax/Desktop/Python/readfilemath.py ===========
>>> main()
1.1
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    main()
  File "C:/Users/Aidax/Desktop/Python/readfilemath.py", line 10, in main
    num1 = int(hw_file.readline())
ValueError: invalid literal for int() with base 10: '2.4\n'
>>> 
=========== RESTART: C:/Users/Aidax/Desktop/Python/readfilemath.py ===========
Traceback (most recent call last):
  File "C:/Users/Aidax/Desktop/Python/readfilemath.py", line 12, in <module>
    main()
  File "C:/Users/Aidax/Desktop/Python/readfilemath.py", line 9, in main
    total = int(line)
ValueError: invalid literal for int() with base 10: '1.1\n'
>>> 
=========== RESTART: C:/Users/Aidax/Desktop/Python/readfilemath.py ===========
Traceback (most recent call last):
  File "C:/Users/Aidax/Desktop/Python/readfilemath.py", line 12, in <module>
    main()
  File "C:/Users/Aidax/Desktop/Python/readfilemath.py", line 10, in main
    print(format(line, '.3f'))
ValueError: Unknown format code 'f' for object of type 'str'
>>> 
=========== RESTART: C:/Users/Aidax/Desktop/Python/readfilemath.py ===========
1.1

2.4

3.6

4.7

>>> 
=========== RESTART: C:/Users/Aidax/Desktop/Python/readfilemath.py ===========
1.1
2.4
3.6
4.7
>>> 
=========== RESTART: C:/Users/Aidax/Desktop/Python/readfilemath.py ===========
1.1
3.5
7.1
11.8
>>> 
=========== RESTART: C:/Users/Aidax/Desktop/Python/readfilemath.py ===========
11.8
>>> 
=========== RESTART: C:/Users/Aidax/Desktop/Python/readfilemath.py ===========
11.800
>>> 
=========== RESTART: C:/Users/Aidax/Desktop/Python/readfilemath.py ===========
11.800
2.95
>>> 
=========== RESTART: C:/Users/Aidax/Desktop/Python/readfilemath.py ===========
11.800
2.950
>>> 
=========== RESTART: C:/Users/Aidax/Desktop/Python/readfilemath.py ===========
Please Enter the file name
=========== RESTART: C:/Users/Aidax/Desktop/Python/readfilemath.py ===========
Please Enter the file name: input1.txt
Traceback (most recent call last):
  File "C:/Users/Aidax/Desktop/Python/readfilemath.py", line 16, in <module>
    main()
  File "C:/Users/Aidax/Desktop/Python/readfilemath.py", line 6, in main
    hw_file = open('filename', 'r')
FileNotFoundError: [Errno 2] No such file or directory: 'filename'
>>> 
=========== RESTART: C:/Users/Aidax/Desktop/Python/readfilemath.py ===========
Please Enter the file name: d
Traceback (most recent call last):
  File "C:/Users/Aidax/Desktop/Python/readfilemath.py", line 16, in <module>
    main()
  File "C:/Users/Aidax/Desktop/Python/readfilemath.py", line 6, in main
    hw_file = open(filename, 'r')
NameError: name 'filename' is not defined
>>> 
=========== RESTART: C:/Users/Aidax/Desktop/Python/readfilemath.py ===========
Please Enter the file name: input1.txt
11.800
2.950
>>> 
=========== RESTART: C:/Users/Aidax/Desktop/Python/readfilemath.py ===========
Please Enter the file name: input1.txt
11.800
2.950
Please Enter the file name: f
File:  f  does not exist.
Please Enter the file name: quit
>>> 
=========== RESTART: C:/Users/Aidax/Desktop/Python/readfilemath.py ===========
Please enter the file name or type QUIT to exit: r
File:  r  does not exist.
Please enter the file name or type QUIT to exit: input1.txt
11.800
2.950
Please enter the file name or type QUIT to exit: 
=========== RESTART: C:/Users/Aidax/Desktop/Python/readfilemath.py ===========
Please enter the file name or type QUIT to exit: input1.txt
Total:  11.800
Average:  2.950
Please enter the file name or type QUIT to exit: quit
>>> main()
Please enter the file name or type QUIT to exit: input4.txt
File  input4.txt  is empty.
Please enter the file name or type QUIT to exit: input1.txt
Total:  11.800
Average:  2.950
Please enter the file name or type QUIT to exit: 
=========== RESTART: C:/Users/Aidax/Desktop/Python/readfilemath.py ===========
Please enter the file name or type QUIT to exit: input4.txt
File: input4.txt  is empty.
Please enter the file name or type QUIT to exit: 
=========== RESTART: C:/Users/Aidax/Desktop/Python/readfilemath.py ===========
Please enter the file name or type QUIT to exit: input4.txt
File: input4.txt is empty.
Please enter the file name or type QUIT to exit: input1.txt
Total: 11.800
Average: 2.950
Please enter the file name or type QUIT to exit: input3.txt
Total: 1.124
Average: 1.124
Please enter the file name or type QUIT to exit: input5.txt
File: input5.txt does not exist.
Please enter the file name or type QUIT to exit: input4.txt
File: input4.txt is empty.
Please enter the file name or type QUIT to exit: input5.txt
File: input5.txt does not exist.
Please enter the file name or type QUIT to exit: input1.txt
Total: 11.800
Average: 2.950
Please enter the file name or type QUIT to exit: 
=========== RESTART: C:/Users/Aidax/Desktop/Python/readfilemath.py ===========
Please enter the file name or type QUIT to exit: QUIT
File: QUIT does not exist.
Please enter the file name or type QUIT to exit: quit
>>> 
=========== RESTART: C:/Users/Aidax/Desktop/Python/readfilemath.py ===========
Please enter the file name or type QUIT to exit: QUIT
>>> main
<function main at 0x02BC2228>
>>> main()
Please enter the file name or type QUIT to exit: traceback
File: traceback does not exist.
Please enter the file name or type QUIT to exit: 
