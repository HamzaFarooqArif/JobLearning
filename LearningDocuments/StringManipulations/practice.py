print("MULTIPLY")
message2a = 'hello ' * 3
message2b = 'world'
print(message2a + message2b)

print("")
print("Find")
message5 = "hello world"
message5a = message5.find("worl")
print(message5a)
message6 = "Hello World"
message6b = message6.find("squirrel")
print(message6b)

print("")
print("LowerCase")
message7 = "HELLO WORLD"
message7a = message7.lower()
print(message7a)

print("")
print("UpperCase")
message7 = "hello world"
message7a = message7.upper()
print(message7a)

print("")
print("Replace")
message8 = "HELLO WORLD"
message8a = message8.replace("L", "pizza")
print(message8a)

print("")
print("Slice")
message9 = "Hello World"
message9a = message9[1:8]
message9b = message9[1:]
message9c = message9[:1]
print(message9a)
print(message9b)
print(message9c)

print("")
print("EscapeSequences")
print('The program printed \"hello world\"')
print('hello\thello\thello\nworld')