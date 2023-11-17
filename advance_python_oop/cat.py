class cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = cat('kred',3)
cat2 = cat('rex',4)
cat3 = cat('kreg',5)

def get_old_cat(*args):
    return max(args)

print(f'The oldesat cat is  {get_old_cat(cat1.age, cat2.age, cat3.age)} years old')