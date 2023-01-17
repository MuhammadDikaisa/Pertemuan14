# Mengakses Nilai dalam String
var1 = "Hello word!"
var2 = "Python Programming"
print("var1[0] : ", var1[0]) # Mengambil Karakter Pertama
print("var[1:5] : ", var2[1:5]) # Karakter 2 s/d ke-5

# Mengupdate String
message = "Hello Wordl!"
print("Update String : - ", message[:6] + "Python")

# Latihan
txt = "Hello World"
print(len(txt))
print(txt[10])
print(txt[2:5])
print(txt.replace(" ", ""))
print(txt.upper())
print(txt.lower())
print(txt.replace("H", "J"))

# Latihan 2
umur = 24
txt = "Hello, nama saua Dikaisa, dan umur saya adalah {} tahun"
print(txt.format(umur))