


class BuildingBlueprint():
    pass


b1=BuildingBlueprint()
b2=BuildingBlueprint()

print(f"Building 1 object : {b1}")
print(f"Building 2 object : {b2}")

# addresss 

print(f"buildig 1 address {id(b1)}")
print(f"building 2 address {id(b2)}")

print(b1 is b2)