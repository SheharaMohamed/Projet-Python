#Open connexion.log
file_input = open("inputs\\connexion.log.txt",'r')

#Opening the writing file, the user file in file named "utilisateurs.txt"
file_output = open('outputs\\utilisateurs.txt','w')

#Read the file line by line
lines_input = file_input.readlines()

#Save the users in a list
list_output = []
for line in lines_input:
    #Seperate the details in a line
    list_output.append(line.split(";")[1])

#Remove duplicates in output_list
set_output = set(list_output)

#Write file
for i in set_output:
    file_output.write(i+"\n")

#Close files
file_input .close()
file_output.close()
