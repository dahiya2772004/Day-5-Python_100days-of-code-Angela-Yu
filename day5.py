import random
lower="abcdefghijklmnopqrstwxyz"
upper="ABCDEFGHIJKLMNOPQRSTWXYZ"
numbers="0123456789"
symbols="@#%^&*+="
length=8
all=lower+upper+numbers+symbols
password=''.join(random.sample(all,length))

printable="the password generated"+" "+" "+ "is" + "   "+""+ (password)+ "\n"
print(printable)
