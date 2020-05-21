import string
import math

number = "0123456789"
letters = string.ascii_letters + number
letter_count = 0
space_count = 0
s = ".!?"
sent_count = 0

with open("input.txt", "r") as file:
    data = file.readlines()


for i in data:
    space_count += i.count(" ")
    for p in letters:
        letter_count += i.count(p)

for i in data:
    for p in s:
        sent_count += i.count(p)

ari = 4.71 * (letter_count / space_count) + 0.5 * (space_count / sent_count) - 21.43

ari = math.ceil(ari)


def age(ari):
    if ari == 1:
        return print("age: 5-6 , kindergarten")
    if ari == 2:
        return print("age:6-7,  First/Second Grade")
    if ari == 3:
        return print("age:7-9, Third Grade")
    if ari == 4:
        return print("age:9-10, Fourth Grade")
    if ari == 5:
        return print("age:10-11, Fifth Grade")
    if ari == 6:
        return print("age:11-12, Sixth Grade")
    if ari == 7:
        return print("age:12-13, Seventh Grade")
    if ari == 8:
        return print("age:13-14, Eighth Grade")
    if ari == 9:
        return print("age:14-15, Ninth Grade")
    if ari == 10:
        return print("age:15-16, Tenth Grade")
    if ari == 11:
        return print("age:16-17, Eleventh Grade")
    if ari == 12:
        return print("age:17-18, Twelfth Grade")
    if ari == 13:
        return print("age:18-24, College student")
    if ari == 14:
        return print("age:24+, Professor")


age(ari)
