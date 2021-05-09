with open('file', 'r') as file:
    data = file.read()
data1 = data[::-1]
output1 = data1[data1.find(".")+1:data1.find("/")]
output2 = data[data.find(",")+1:data.find("\n")]

if output1[::-1]==output2:
    print("1") 
else:
    print("0")