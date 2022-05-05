meno = input("Zadaj svoje meno: ")
dlzka = len(meno)
if 3 < dlzka < 10:
    print("Spravne naformatovane meno")
    print("Pocet znakov", len(meno))
else:
    print("Moc kratke/dlhe meno")
    print("Pocet znakov", len(meno))