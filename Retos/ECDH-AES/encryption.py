#################################
#				#
#	ECDH KEY EXCHANGE	#
#				#
#################################
import Crypto
from Crypto import *
from Crypto.Util import *

message = ??????????????????

# Private keys
Alice_priv = Crypto.Util.number.getPrime(16)
Bob_priv = Crypto.Util.number.getPrime(16)

# The curve is y^2 = x^3 + ax + b
a = 1234577
b = 3213242
M = 7654319

P = (5234568, 2287747) # A point in the curve

def add(A,B):
    if A==(0,0): return B
    if B==(0,0): return A
    x1,y1 = A
    x2,y2 = B
    if A!=B:
        p = (y2-y1)*pow(x2-x1,M-2,M)
    else:
        p = (3*x1*x1+a)*pow(2*y1,M-2,M)
    x3 = p*p-x1-x2
    y3 = p*(x1-x3)-y1
    return (x3%M,y3%M)

def mult(m, P):
    added = P
    for i in range(m):
        added = add(added,P)
    return added


# Public: P, a, b, M, Bob_pub, Alice_pub
Bob_pub = mult(Bob_priv,P)
Alice_pub = mult(Alice_priv, P)

# Alice obtains the secret key. Bob can do the same using its private key and Alices public one
shared_secret = mult(Alice_priv, Bob_pub)

key = str(shared_secret[0])

#################################
#				#
#	AES ENCRYPTION		#
#				#
#################################
import AES

aes_engine = AESCipher(key)
cipher = aes_engine.encrypt(message)
print('Encrypted message: ' + str(cipher))

# Encrypted message = J31ueow1irdvyJ+1aGszetQAozbFFfK8q9hmT4ygOvytezpzJWnEE0eDjVAh5Loe

