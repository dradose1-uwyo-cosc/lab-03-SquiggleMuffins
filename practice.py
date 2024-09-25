names = ["Michael","Cooper","Meghan","Jack","Caleb","Lee","Jackie"]
print(names)

names.remove("Jackie")
print(names)

names.append("Sarah")
print(names)

for name in names:
    print(f"{name} sits at my table.")

names.sort(reverse=True)
print(names)

