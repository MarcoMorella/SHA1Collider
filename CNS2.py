import hashlib
import random
import string
import time
start_time = time.time()

N = 8 #String Length
M = 12 #Number of hexdigest's digit to check
s = string.ascii_letters+string.digits #All possibile string characters
Tries = 0 #Tries done before finishing
dict = {}

def get_random():
    return ''.join(random.sample(s,N))

while True :
    Tries = Tries+1
    TryString = get_random()
    Hashed = hashlib.sha1(TryString.encode("ascii")).hexdigest()

    if Hashed[-M:] not in dict.keys() :
        try: #Let's expect a MemoryError if we search a too big collision
            dict[Hashed[-M:]] = TryString
        except MemoryError:
            print("LOG: MemoryError")
            dict = {}
    else:
        if dict[Hashed[-M:]] == TryString :
            print("Found an already used string!")
            print("Number of tries made so far" ,Tries)
        else :
            break


print("--- %s seconds ---" % (time.time() - start_time))
print("Number of tries made" ,Tries)

colliding = dict[Hashed[-M:]]
collHash = hashlib.sha1(colliding.encode("ascii")).hexdigest()
print (colliding+'\n'+collHash+'\n'+TryString+'\n'+Hashed)
