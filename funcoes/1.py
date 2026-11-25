def celsius_para_fahrenheit(celsius):
    f = celsius * 1.8 + 32
    return f"{celsius}° celsius são: {f:.2f}° fahrenheit."

def fahrenheit_para_celsius(fahrenheit):
    c = ( fahrenheit - 32) / 1.8
    return f"{fahrenheit}° fahrenheit são: {c:.2f}° celsius."

c = celsius_para_fahrenheit(829)
f = fahrenheit_para_celsius(525)

print(c)
print(f)