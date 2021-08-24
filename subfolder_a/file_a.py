import json

with open('subfolder_a/data.json', 'r') as f:
    data = json.load(f)

value_a = data.get("a")

if __name__ == "__main__":
    print("value a is :", value_a)
