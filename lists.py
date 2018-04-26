# Joyce Wu
# Softdev pd 7
# K15 -- Do you even list?
# 2018-04-25

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
num = '0123456789'
non_alph_chars = '.?!&#,;:-_*'

#determines whether password reaches a certain threshold
def threshold(pw):
    upper_chars = [x for x in pw if x in upper]
    lower_chars = [x for x in pw if x in lower]
    num_chars = [x for x in pw if x in num]
    return len(upper_chars) > 0 and len(lower_chars) > 0 and len(num_chars) > 0

#rates password strength
def pw_strength(pw):
    rating = 0
    rating += .5 * len([x for x in pw if x in upper])
    rating += .5 * len([x for x in pw if x in lower])
    rating += .5 * len([x for x in pw if x in num])
    rating += len([x for x in pw if x in non_alph_chars])
    if rating > 10:
        rating = 10
    return int(rating)

#####TESTING##############
# print(threshold('aSFewfwef123')) #true
# print(threshold('aEW12VFDsc0')) #true
# print(threshold('!!!!!!')) #false
# print(threshold('23442!242')) #false
# print(threshold('alfdjfkl')) #false
print(pw_strength('hEll0!!')) #6
print(pw_strength('yuuuuuuuuuuu')) #6
print(pw_strength('h!!!!;yUp0123')) #9
print(pw_strength('naHHur!23')) #5
