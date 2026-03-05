import itertools 

print("make a password with 10 letters/digits")
passwd = input("password: ")

nums = ['0','1','2','3','4','5','6','7','8','9',
        'a','b','c','d','e','f','g','h','i','j',
        'k','l','m','n','o','p','q','r','s','t',
        'u','v','w','x','y','z']
for p in itertools.product(nums, repeat=9):
    number = (''.join(map(str, p)))
    print(number)

    if number == passwd:
	    print("password found:", passwd)
	    break
