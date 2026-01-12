tinggi_daun = 9
tinggi_batang = 3

for k in range(tinggi_daun):
    spasi = " " * (tinggi_daun -k)
    daun = "*" * (2 * k + 1)
    print(spasi + daun)

for l in range(tinggi_batang):
    spasi = " " * (tinggi_daun -1)
    batang = "|" *2
    print(spasi + batang)