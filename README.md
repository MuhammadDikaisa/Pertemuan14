# Nama : Muhammad Dikaisa ibnu amin
# NIM : 312210289
# Kelas : TI.22.A.3

*<h3>Mengakses Nilai dalam String*

Input : 

```python
var1 = "Hello word!"
var2 = "Python Programming"
print("var1[0] : ", var1[0]) # Mengambil Karakter Pertama
print("var[1:5] : ", var2[1:5]) # Karakter 2 s/d ke-5
```

Output : 

akan mengeluarkan karakter pertama dari variabel 1 yaitu "H"
dan di variable kedua akan mengeluarkan karakter 1 s/d 5

```python
var1[0] :  H
var[1:5] :  ytho
```

*<h3>Mengupdate String*
Input : 

```python
message = "Hello Wordl!"
print("Update String : - ", message[:6] + "Python")
```

Output : 

Output akan mengambil karakter 1 s/d 6 dan ditambahkan dengan "Python"

```python
Update String : -  Hello Python
```

# Latihan

Input :

```python
txt = "Hello World"                 
print(len(txt))                   # Len untuk menghitung jumlah karakter yang ada di dalam sebuah variable
print(txt[10])                    # Akan mengeluarkan karakter ke 10
print(txt[2:5])                   # Akan mengeluarkan karakter 2 s/d 5
print(txt.replace(" ", ""))       # Mengganti karakter white space menjadi tanpa white space
print(txt.upper())                # Membuat semua karakter menjadi huruf kapital
print(txt.lower())                # Membuat semua karakter menjadi huruf kecil
print(txt.replace("H", "J"))      # Mengubah huruf, dari huruf "H" menjadi huruf "J"
```

Output : 

```python
11
d
llo
HelloWorld
HELLO WORLD
hello world
Jello World
```

# Latihan 2
Input :
Tambahkan kekurangan dengan tanda "{}"
```python
umur = 24
txt = "Hello, nama saya Dikaisa, dan umur saya adalah {} tahun"
print(txt.format(umur))
```

Output : 

```python
Hello, nama saya Dikaisa, dan umur saya adalah 24 tahun
```
