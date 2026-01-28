art = [12, [23, 'string', 0, [12, 'new']], [], 3j]

print(art[1][3])

s = [1, 2, 3, 4, 5]
names= ['Alex', 'John', 'Fred', 'Samantha', 'Gennady']
# for i in range(len(s)):
#     print(names[i], "'s Id is: ", s[i])
    
f = s + names
print(f)
x = names.count('Fred')
print(x)

z = {}
z['fall'] = 3
z['fall']+=2
z[10]= 'string'
z['inner_list'] = [1, 3, 'test', {'new':1000}]
z['inner_dict'] = {'asd':123}
# z['test_key
print(list(z.keys()))