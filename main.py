import json
import math
import sys
import os.path

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

def read_json(string):
    data = json.loads(string)
    if "ALL" in data and "network_bytes_received" in data and "network_bytes_sent" in data:
        return str(data['ALL']['accepted_clients']) + "," + str(convert_size(int(data['network_bytes_received']) + int(data['network_bytes_sent']))) + "," + str(data['timestamp'])

def export_csv(file_path):
    count = 0
    output_line = ""
    with open(file_path, 'r') as file:
        for line in file:
            if (str(read_json(line.strip())) != "None"):
                output_line += str(read_json(line.strip())) + "\n"
                count = count + 1
    
    f = open("output.csv", "w")
    f.write(output_line)
    f.close()

    return count

def show_error(error):
    print("Error : " + error)

logs_path = input("➜ Enter Psiphon logs file path : ")

if(os.path.isfile(logs_path) == False):
    show_error("file not exist")
    exit()

print()
print(" -----------------------------------------------------------------")
print(" e:   Export csv file with (date-time, connected user, data usage)")
print(" s:   Show transformed data (Not completed)")
print(" c:   Show number of all connections that made (Not completed)")
print(" -----------------------------------------------------------------")
print()

action = input("➜ What do you want to do? (e/s/c) : ")
if (action=="e"):
    print("Exporting csv file...")
    print("CSV file successfully genarated in output.csv with " + str(export_csv(logs_path)) + " lines")
elif (action=="s"):
    print("All transformed data : ...")
elif (action=="c"):
    print("Number of all connections : ...")
else:
    show_error("undefined input")