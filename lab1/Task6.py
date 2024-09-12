def make_pizza(pizza_size, *ingredients):
    output = f"Making a {pizza_size}-inch pizza with the following topping:"
    for topping in ingredients:
        output += f"\n-{topping}"
    return output


output1 = make_pizza(16, "pepperoni")
output2 = make_pizza(12, "mushrooms", "green peppers", "extra cheese")
print(output1)
print(output2)
