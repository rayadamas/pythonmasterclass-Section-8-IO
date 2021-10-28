import shelve

fruit = shelve.open('ShelfTest')
fruit['orange'] = "a sweet, orange, citrus fruit"
fruit['apple'] = "good for making cider"
fruit['lemon'] = "a sour, yellow citrus fruit"
fruit['grape'] = "a small, sweet fruit growing in bunches"
fruit['lime'] = "a sour, green citrus fruit"

print(fruit)


while True:
    shelve_key = input("Please enter a fruit: ")
    if shelve_key == "quit":
        break

    description = fruit.get(shelve_key, "We don't have a " + shelve_key)
    print(description)

fruit.close()

