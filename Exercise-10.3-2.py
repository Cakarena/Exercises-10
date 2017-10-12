##Exercise 2: This program counts the distribution of the hour of the day for each of the messages. 
##You can pull the hour from the "From" line by finding the time string 
## and then splitting that string into parts using the colon character. 
## Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.
# hh = hour histogram

fname = input("Enter a file name: ")
line_list = [line.strip("\n") for line in open(fname, 'r')
             if line.startswith("From ") and not line.startswith("From:")]
hh = {}
#hour histogram
tuple_list = []

for line in line_list:
    time = line.split()[5]
    hour = time.split(":")[0]
    hh[hour] = hh.get(hour, 0) + 1

##print(hh)
for key in hh:
    tuple_list.append((key, hh[key]))

sort_tuple_list = sorted(tuple_list)

for item in sort_tuple_list:
    print(item[0], item[1])
## note reasoning for each line

