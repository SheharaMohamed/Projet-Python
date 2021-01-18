#Open warning input file
file_warning = open('inputs\\warning.txt','r')

#Ceate a list to take the suspects
suspects_ip = []

#Read lines and take the suspects in to the list suspects_ip
lines_warning = file_warning.readlines()
for line in lines_warning:
    suspects_ip.append(line[:-1])

#Close suspect input file
file_warning .close()

#Open and read the users file line by line
file_input = open('inputs\\connexion.log.txt','r')
lines_input = file_input.readlines()

#Open a writable file 
file_output = open('outputs\\suspects.txt','w')

#Creating a list to save output
list_output = []

for ip in suspects_ip:

    for line in lines_input:
        #Split the line to take details
        user = line.split(";")

        #IP matching
        if user[0]==ip:

            list_output.append(user[1])
            
#Remove duplicates in list_output
set_output = set(list_output)

for i in set_output:
    file_output.write(i+";"+str(list_output.count(i))+"\n")

#Close files
file_input.close()
file_output.close()
            