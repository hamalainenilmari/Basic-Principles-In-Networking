# 1. Pick two random prime number p & q
# 2. Get n = p * q
# 3. Get m = (p-1)*(q-1)
# 4. 
import rsa

def generate(num):
    (publickey, privatekey) = rsa.newkeys(num)
    return (publickey, privatekey)


def encrypt(original):
    print(f'get original: {original}')
    numbers = [ord(char) for char in original]
    print(numbers)
    encryptNumbers=[]
    
    for num in numbers:
        encryptNumbers.append(pow(num, e) % n)
    print(encryptNumbers)
    encryptChars = [chr(num) for num in encryptNumbers]
    print(encryptChars)
    return encryptChars
        

def decrypt(encrypt):
    encryptNumbers = [ord(char) for char in encrypt]
    decryptNumbers=[]
    for num in encryptNumbers:
        decryptNumbers.append(pow(num, d) % n)
    print(decryptNumbers)
    decryptChars = [chr(num) for num in decryptNumbers]
    print (decryptChars)
    


def subString(msg):
    array = []
    i = 0
    start = 0
    while (i < len(msg)):
        #print(msg[i])
        if (msg[i] == ' '):
            print(f"I found a space at {i}")
            print(msg[start: i])
            array.append(msg[start: i])
            start = i + 1
        i += 1
    print(array)
    


def main():
    # print('-------')
    # secret = encrypt("Hello World")
    # print('-------')
    # decrypt(secret)
    (publickey, privatekey) = generate(1024)
    print(publickey)
    
    subString("hello you happy no")

if __name__ == "__main__":
    main()


