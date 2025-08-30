c_to_f = lambda c: (c * 9/5) + 32
for c in [0, 10, 20, 30]:
    print(f"{c}°C -> {c_to_f(c)}°F")