password = input("Masukkan password: ")
panjang = len(password)

if panjang < 6:
    print("Password terlalu pendek (minimal 6 karakter)")
elif panjang > 12:
    print("Password terlalu panjang (maksimal 12 karakter)")
else:
    print("Password valid")