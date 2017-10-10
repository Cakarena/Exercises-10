##Exercise 1: Revise a previous program (9.3) as follows: Read and parse the "From" lines and pull out the addresses from the line.
## Count the number of messages from each person using a dictionary.
##After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. 
##Then sort the list in reverse order and print out the person who has the most commits.

fname = input("Enter a file name: ")
lines_list = [line.strip("\n") for line in open(fname, 'r')
         if line.startswith("From") and not line.startswith("From:")]

mail_dict = dict()

##The above is the same as 9.3

for line in lines_list:
    mail = line.split()[1]
    mail_dict[mail] = mail_dict.get(mail,0) + 1
    ##WSee notes on this from 9.3

print("1. List of least to most committs:", sorted( [(v,k) for k,v in mail_dict.items()]))
#This is the total list in order of count, email, from least to most.  This is the pretty code Chuck used in 10.2 :) :)

mostmessage = 0
most_person = None
for person in mail_dict:
	if mail_dict[person] > mostmessage:
		mostmessage = mail_dict[person]
		most_person = person
print("Email with the most committs:",mail_dict[most_person],most_person)

