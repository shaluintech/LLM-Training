def bmi(weight_kg, height_m):
    value = weight_kg / (height_m ** 2)
    return round(value, 1)
if __name__ == "__main__":
    print(bmi(72,1.75))
    print(bmi(50,1.60))
