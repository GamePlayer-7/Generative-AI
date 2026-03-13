try:
    file=open('example.txt','r')
    content=file.read()
    print(content)

except FileNotFoundError:
    print("The file does not exists.")