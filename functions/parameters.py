#parameters
def say_hello(name,emoji):
    print(f'hello {name}{emoji}')

#positional arguments
say_hello('kennedy', '😊')
say_hello('junior','😊')
say_hello('june','😊')

#keyword arguments
say_hello(emoji = '😊',name = 'bibi')