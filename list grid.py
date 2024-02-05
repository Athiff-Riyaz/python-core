number=3
things=["string",0,[1,2,number],4.56]
print(things[1])
print(things[2])
print(things[2][2])

nums=[7,7,7,7,7]
nums[2]=5
print(nums)

no=[1,2,3]
print(no+[4,5,6])
print(no*3)

words=["spam","eggs","sausage","bread"]
print("spam" in words)
print("eggs" in words)
print("tomato" in words)

some=[1,2,3]
print(not 4 in some)
print(4 not in some)
print(not 3 in some)
print(3 not in some)

numbers=[1,2,3]
numbers.append(4)
print(numbers)
print(len(numbers))
wordz=["python","fun"]
index=1
wordz.insert(index, "is")
print(wordz)

letters=['p','q','r','s','t','u']
print(letters.index('r'))
print(letters.index('p'))