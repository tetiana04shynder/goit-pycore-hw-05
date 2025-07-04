def get_cats_info(path):
    cats = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue 
                parts = line.split(',')
                if len(parts) != 3:
                    continue 
                cat_id, name, age = parts
                cat = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }
                cats.append(cat)
        return cats
    except FileNotFoundError:
        print(f"'{path}'")
        return []
    except Exception as e:
        print(f"{e}")
        return []
cats_info = get_cats_info("/Users/taniashynder/Desktop/cats_file.txt")
print(cats_info)
