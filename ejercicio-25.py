def cuenta_atras(num):
    num -= 1
    if num > 0:
        print(num)
        cuenta_atras(num)
    else:
        print("BOOOOM!!!")
    print(f"Fin la funcoin{num}")

print(cuenta_atras(5))