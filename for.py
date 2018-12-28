fruitslist = ['apple','orange','banana']
fruitstuple = ('apple','orange','banana')
fruitsset = {'apple','orange','banana'}
print(len(fruitslist))
fruitslist.append('grapes')
# fruitstuple.append('guava')
fruitsset.add('orange')
for f in fruitslist:
    print(f)
    if f == "apple":
        continue
print (fruitslist)
print (fruitstuple)
print (fruitsset)