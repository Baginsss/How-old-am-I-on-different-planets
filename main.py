print("How old am I on different planets?")
print("----------------------------------")
print("How old are you?")
age = input("Age:")

age = float(age)

orb_merkury = 0.2408
orb_wenus = 0.6152
orb_mars = 1.8808
orb_jowisz = 11.8637
orb_saturn = 29.4484
orb_uran = 84.0711
orb_neptun = 164.8799

age_merkury = age / orb_merkury
age_wenus = age / orb_wenus
age_mars = age / orb_mars
age_jowisz = age / orb_jowisz
age_saturn = age / orb_saturn
age_uran = age / orb_uran
age_neptun = age / orb_neptun

print("----------------------------------")
print("Merkury: ", age_merkury)
print("Wenus: ", age_wenus)
print("Mars: ", age_mars)
print("Jowisz: ", age_jowisz)
print("Saturn: ", age_saturn)
print("Uran: ", age_uran)
print("Neptun: ", age_neptun)
print("----------------------------------")

pause = input("")