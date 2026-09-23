estoque = ["Multímetro", "Protoboard", "Resistor", "Multímetro", "Cabo", "Multímetro", "Protoboard"]

equipamento = input("digite o nome do equipamento: ").strip().title()

if equipamento in estoque:
    print(f"o nome {equipamento} aparece {estoque.count(equipamento)} vezes.")

else:
    print("equipamento não encontrado no estoque!")