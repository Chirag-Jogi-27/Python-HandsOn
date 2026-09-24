## file handling 



# file = open("notes.txt", "r" , encoding="utf-8")

# reading all line at one time only

# all_text = file.read()
# print(all_text)


# readig line by line

# line1= file.readline()

# line2=file.readline()

# line3=file.readline()

# print(repr(line1))
# print(repr(line2))

# print(repr(line3))


# while True:
#     line = file.readline()
#     if not line:
#         break
#     print(line.strip())

# file.close()


## write method 

# lines = [
#     "Line 1: Server started\n",
#     "Line 2: Database connected\n",
#     "Line 3: API running\n"
# ]

# file = open("notes.txt" , mode = "w" , encoding="utf-8")

# file.writelines(lines)
# file.close()



# new_file = open("notes.txt", "r", encoding="utf-8")

# for line in new_file:
#     print(line.strip())

# new_file.close()



with open("notes.txt","r", encoding="utf-8") as file:
    for line in file:
        print(line)

