with open('engine/src/algorithms/catalog.toml', 'r', encoding='utf-8') as f:
    text = f.read()

for block in text.split('[[algorithm]]'):
    if 'status = "approved"' in block:
        name_line = [l for l in block.splitlines() if 'name =' in l]
        if name_line:
            print(name_line[0].strip())
