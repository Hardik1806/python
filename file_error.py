with open("abc.txt","w")as f: #creating a txt file
    f.write("important notice")# writing some info in it

reader=open("abc.txt","r")#again opening adn reading it 
writer=open("abc.txt","w") #again opening it knowing that reader hasn't cloased 
writer.write("new stuff") #writing info in it
print(reader.read()) #again reading it  getting the nothing as output because of data corruption
