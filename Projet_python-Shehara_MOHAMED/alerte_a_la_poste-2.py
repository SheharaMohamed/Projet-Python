from datetime import datetime       #import date time object to manipulate with date time data

#Read the input file 
file_input = open('inputs\\connexion.log.txt','r')
suspects = []

#Read the file line by line
lines_input = file_input.readlines()
for line in lines_input:

    utilisateur = line.split(";")

    #Create date time object with last item in the list in format (dd/mm/yy HH:MM)
    datetime_obj = datetime.strptime(utilisateur[2][:-1],"%d/%m/%y %H:%M")

    #Take hour and minute
    heure = datetime_obj.hour
    minutes = datetime_obj.minute

    #Condition to time period (before 8h00 and after 19h00)
    if (heure>=19 or heure<8) and minutes!=0:
        suspect = utilisateur[1]+" - "+utilisateur[0]
        if suspect not in suspects:
            suspects.append(suspect) 

#Output (print) the suspects list
for i in suspects:
    print(i)

#Close file
file_input .close()