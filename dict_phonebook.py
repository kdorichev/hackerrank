""" 
The first line contains an integer, N, denoting the number of entries in the phone book. 
Each of the N subsequent lines describes an entry in the form of two space-separated values on a single line. 
The first value is a friend's name, and the second value is an 8-digit phone number.

After the  lines of phone book entries, there are an unknown number of lines of queries. 
Each line (query) contains a name to look up, and you must continue reading lines until there is no more input.
"""
n = int(input())

book = dict()    

for i in range(n):
    line = input()
    name, phone = line.split()
    book[name] = phone

while True: 
    line = input()
    phone = book.get(line,"0")
    if phone == "0":
        print("Not found")
    else:
        print("{}={}".format(line,book[line]))
