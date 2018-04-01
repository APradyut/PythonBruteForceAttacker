import itertools
import time
import threading
import bruteForcer

Alphabet = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_.@")
opposite = ("zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA1234567890-_.@")
Found = False
CharLengthTotal = 9
def part4():
    global Found
    start = time.time()
    time.sleep(0.1)
    global CharLengthTotal
    counter = 1
    for CharLength in range(CharLengthTotal,CharLengthTotal+25,2):
        passwords = (itertools.product(opposite, repeat = CharLength))
        lock = threading.Lock()
        lock.acquire()
        print("\n \n")
        print("currently working on passwords with ", CharLength, " chars")
        print("We are currently at ", (counter / (time.time() - start)), "attempts per seconds")
        print("It has been ", time.time() - start, " seconds!")
        print("We have tried ", counter, " possible passwords!")
        lock.release()
        for i in passwords:
            time.sleep(0.5)
            counter += 1
            i = str(i)
            lock.acquire()
            print("Working in part4 with ",i,"\n")
            lock.release()
            i = i.replace("[", "")
            i = i.replace("]", "")
            i = i.replace("'", "")
            i = i.replace(" ", "")
            i = i.replace(",", "")
            i = i.replace("(", "")
            i = i.replace(")", "")
            if Found:
                exit()
            Found = bruteForcer.send(i)
            # if i == Password:
            #     end = time.time()
            #     timetaken = end - start
            #     lock.acquire()
            #     print("Found it in ", timetaken, " seconds and ", counter, "attempts")
            #     Found = True
            #     print("That is ", counter / timetaken, " attempts per second!")
            #     print(i)
            #     input("Press enter when you have finished")
            #     lock.release()
            #     exit()

def part2():
    global Found
    start = time.time()
    time.sleep(0.1)
    global CharLengthTotal
    counter = 1
    for CharLength in range(CharLengthTotal,CharLengthTotal+25,2):
        time.sleep(0.5)
        passwords = (itertools.product(Alphabet, repeat = CharLength))
        lock = threading.Lock()
        lock.acquire()
        print("\n \n")
        print("currently working on passwords with ", CharLength, " chars")
        print("We are currently at ", (counter / (time.time() - start)), "attempts per seconds")
        print("It has been ", time.time() - start, " seconds!")
        print("We have tried ", counter, " possible passwords!")
        lock.release()
        for i in passwords:
            counter += 1
            i = str(i)
            lock.acquire()
            print("Working in part2 with ",i,"\n")
            lock.release()
            i = i.replace("[", "")
            i = i.replace("]", "")
            i = i.replace("'", "")
            i = i.replace(" ", "")
            i = i.replace(",", "")
            i = i.replace("(", "")
            i = i.replace(")", "")
            if Found:
                exit()
            Found = bruteForcer.send(i)
            # if i == Password:
            #     end = time.time()
            #     timetaken = end - start
            #     lock.acquire()
            #     print("Found it in ", timetaken, " seconds and ", counter, "attempts")
            #     Found = True
            #     print("That is ", counter / timetaken, " attempts per second!")
            #     print(i)
            #     input("Press enter when you have finished")
            #     lock.release()
            #     exit()
def part3():
    global Found
    lock = threading.Lock()
    start = time.time()
    time.sleep(0.1)
    global CharLengthTotal
    counter =1
    for CharLength in range(CharLengthTotal,CharLengthTotal+25,2):
        passwords = (itertools.product(opposite, repeat = CharLength))
        lock.acquire()
        print("\n \n")
        print("currently working on passwords with ", CharLength, " chars")
        print("We are currently at ", (counter / (time.time() - start)), "attempts per seconds")
        print("It has been ", time.time() - start, " seconds!")
        print("We have tried ", counter, " possible passwords!")
        lock.release()
        for i in passwords:

            counter += 1
            i = str(i)
            lock.acquire()
            print("Working in part3 with ",i,"\n")
            lock.release()
            i = i.replace("[", "")
            i = i.replace("]", "")
            i = i.replace("'", "")
            i = i.replace(" ", "")
            i = i.replace(",", "")
            i = i.replace("(", "")
            i = i.replace(")", "")
            if Found:
                exit()
            Found = bruteForcer.send(i)
            # if i == Password :
            #     end = time.time()
            #     timetaken = end - start
            #     lock.acquire()
            #     print("Found it in ", timetaken, " seconds and ", counter, "attempts")
            #     Found = True
            #     print("That is ", counter / timetaken, " attempts per second!")
            #     print(i)
            #     input("Press enter when you have finished")
            #     lock.release()
            #     exit()


def part1():
    global Found
    lock = threading.Lock()
    start = time.time()
    time.sleep(0.1)
    global CharLengthTotal
    counter =1
    for CharLength in range(CharLengthTotal,CharLengthTotal+25,2):
        passwords = (itertools.product(Alphabet, repeat = CharLength))
        lock.acquire()
        print("\n \n")
        print("currently working on passwords with ", CharLength, " chars")
        print("We are currently at ", (counter / (time.time() - start)), "attempts per seconds")
        print("It has been ", time.time() - start, " seconds!")
        print("We have tried ", counter, " possible passwords!")
        lock.release()
        for i in passwords:
            counter += 1
            i = str(i)
            lock.acquire()
            print("Working in part1 with ",i,"\n")
            lock.release()
            i = i.replace("[", "")
            i = i.replace("]", "")
            i = i.replace("'", "")
            i = i.replace(" ", "")
            i = i.replace(",", "")
            i = i.replace("(", "")
            i = i.replace(")", "")
            if Found:
                exit()
            Found = bruteForcer.send(i)
            # if i == Password:
            #     end = time.time()
            #     timetaken = end - start
            #     lock.acquire()
            #     print("\n\nFound it in ", timetaken, " seconds and ", counter, "attempts\n\n")
            #     Found = True
            #     print("That is ", counter / timetaken, " attempts per second!")
            #     print(i)
            #     input("Press enter when you have finished")
            #     lock.release()
            #     exit()

threading.Thread(target = part2).start()
#threading.Thread(target = part1).start()       //open for more power
threading.Thread(target = part4).start()
#threading.Thread(target = part3).start()       //open for more power