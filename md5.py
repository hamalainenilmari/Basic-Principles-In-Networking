import math

# functions
def F(x, y, z): return (x & y) | (~x & z)
def G(x, y, z): return (x & z) | (y & ~z)
def H(x, y, z): return x ^ y ^ z
def I(x, y, z): return y ^ (x | ~z)

def left_rotate(x, amount):
    return ((x << amount) | (x >> (32 - amount))) & 0xFFFFFFFF

# constants
K = [math.floor(2**32 * abs(math.sin(i + 1))) for i in range(64)]
s = [
    7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
    5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
    4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
    6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21
]

def md5(message):
    # initial hash  values
    a0 = 0x67452301
    b0 = 0xefcdab89
    c0 = 0x98badcfe
    d0 = 0x10325476

    # pre-processing: adding padding to the input message
    paddedMessage = message.encode('utf-8') + b'\x80'
    while (len(paddedMessage) * 8) % 512 != 448:
        paddedMessage += b'\x00'
    paddedMessage += (len(message) * 8).to_bytes(8, "little")

    # main processing in 512-bit chunks
    chunks = [paddedMessage[i:i+64] for i in range(0, len(paddedMessage), 64)]
    for chunk in chunks:
        M = [int.from_bytes(chunk[i:i+4], byteorder='little') for i in range(0, 64, 4)]
        A, B, C, D = a0, b0, c0, d0

        for i in range(64):
            if 0 <= i <= 15:
                f = F(B, C, D)
                g = i
            elif 16 <= i <= 31:
                f = G(B, C, D)
                g = (5 * i + 1) % 16
            elif 32 <= i <= 47:
                f = H(B, C, D)
                g = (3 * i + 5) % 16
            elif 48 <= i <= 63:
                f = I(B, C, D)
                g = (7 * i) % 16

            temp = D
            D = C
            C = B
            B = B + left_rotate(A + f + K[i] + M[g], s[i])
            A = temp
        
        a0 = (a0 + A) & 0xFFFFFFFF
        b0 = (b0 + B) & 0xFFFFFFFF
        c0 = (c0 + C) & 0xFFFFFFFF
        d0 = (d0 + D) & 0xFFFFFFFF

    digest = a0.to_bytes(4, 'little') + b0.to_bytes(4, 'little') + \
         c0.to_bytes(4, 'little') + d0.to_bytes(4, 'little')
    return digest.hex()
    

def main():
    message = input("Enter the message to hash: ")
    hashedMessage = md5(message)
    print(f"Hash value: {hashedMessage}")

if __name__ == "__main__":
    main()