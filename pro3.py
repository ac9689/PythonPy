#check befor appending
file = open('/home/ashwani/Desktop/wwe.txt', 'r')
obj=file.read()
print(obj)
# Check if "busitantsinc" is not in the file content
# Append "Busitantsinc" to the file if not present
if "busitantsinc" not in obj:
    file= open('/home/ashwani/Desktop/wwe.txt', 'a')
    a = file.write("john\n")
    print(a)
    