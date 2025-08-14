# zadania domowe z 04notebook

#Ćwiczenie 1
#Dane wejściowe: str1 = "Datatypes"
#Oczekiwany Wynik: aty

str1 = "Datatypes"
str1_len = len(str1)
print(str1_len)

str2 = str1[3:-3]
print(str2)

#Ćwiczenie nr 2
# Dane wyjściowe: 2 cigi
# s1 = "FullStack"
# s2 = "Python"
#Oczekiwany wynik: 
# FullPythonStack

s1 = "FullStack"
s2 = "Python"

s3 = len(s1)
print(s3)
print(s1[0:4] + s2 + s1[4:] )


#Ćwiczenie nr 3
# Dane wejściowe: 2 ciągi
# s1 = "America"
# s2 = "Japan"
# Oczekiwany wynik
# AJrpan

s1 = "America"
s2 = "Japan"


result = s1[0] + s2[0] + s1[len(s1)//2] + s2[len(s2)//2] + s1[-1] + s2[-1]
print(result)

result2 = s1[0] + s2[0] + s1[3] + s2[2] + s1[-1] + s2[-1]
print(result2)

# Ćwiczenie nr 4
# Dane wejściowe: 
# str1 = "Python"
# Oczekwiany wynik:
# nohtyP

str1 = "Python"
str_reversed = str1[::-1]

print(str_reversed)