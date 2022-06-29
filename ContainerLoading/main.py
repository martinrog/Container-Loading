# https://github.com/martinrog/Container-Loading.git

from BinPacker.Packer import Packer
from BinPacker.Container import Container
from BinPacker.Box import Box

packer = Packer()

#We only make use of this kind container, you can change the size if you want or just add another bin.
packer.add_bin(Container('Standard 40’ HC Container', 2.33, 2.69, 12.01, 26780))

def addToContainer(name, width, height, dept, weight, quantity):
    """This function can add one or more boxes to the container"""
    for item in range(quantity):
        packer.add_item(Box(name, width, height, dept, weight))
    return width, height, dept, quantity

if __name__ == '__main__':

    #Test case: Box is .01 meters longer than the container. TEST BOX Bigger should not fit, the smaller box should
    # addToContainer('TEST BOX Bigger', 2.33, 2.69, 12.02, 50, 1)
    # addToContainer('TEST BOX Smaller', 2.33, 2.69, 12, 50, 2)

    # #Test case: The box is slightly heavier than the container. TEST BOX Heavier should fail, the lighter box should work
    # addToContainer('TEST BOX Heavier', 1, 1, 1, 27000, 1)
    # addToContainer('TEST BOX Lighter', 1, 1, 1, 26000, 1)

    # Last container shipment from the product owner, was a container full with threadmills, 150 pcs
    # addToContainer('TREADMILL BLACK', 0.74, 0.48, 1.7, 50 ,106)

    # Regular test case: Large heterogeneous set of boxes
    addToContainer('Commercial FID Bench', 0.51, 0.34, 1.4, 45, 100)
    addToContainer('Hexagon rubber coated dumbbell 5KG', 0.25, 0.19, 0.3, 20.5, 100)
    addToContainer('Hexagon rubber coated dumbbell 10KG', 0.3, 0.12, 0.35, 20.5, 100)
    addToContainer('Hexagon rubber coated dumbbell 15KG', 0.18, 0.14, 0.37, 15.5, 100)
    addToContainer('Hexagon rubber coated dumbbell 20KG', 0.21, 0.15, 0.39, 20.5, 100)
    addToContainer('TREADMILL BLACK', 0.74, 0.48, 1.7, 50 ,50)


def getVolumeBoxes(self):
    """This function return the volume of all the boxes combined"""
    total = 0
    for box in self.items:
        total += box.get_volume()
    return total

packedBoxesVolume = getVolumeBoxes(packer)


#pack the boxes
packer.pack()

#print the output
for b in packer.bins:
    print(b.string(),"\n")

    print("FITTED ITEMS:")
    for item in b.items:
        print("=> ", item.string())
    print(f"Total packed volume: {packedBoxesVolume}")

    getVolumeBoxes(packer)

    print("\nUNFITTED ITEMS:")
    for item in b.unfitted_items:
        print("=> ", item.string())

# packer.add_item(Box('Voetbaldoos', 0.4, 0.43, 0.64, 5))
# packer.add_item(Box('Yoga mat', 0.2, 0.2, 0.63, 3))
# packer.add_item(Box('Commercial FID Bench', 0.51, 0.34, 1.4, 45))
# packer.add_item(Box('TREADMILL BLACK', 0.74, 0.48, 1.7, 50))
# packer.add_item(Box('Hexagon rubber coated dumbbell 5KG', 0.25, 0.19, 0.3, 20.5))
# packer.add_item(Box('Hexagon rubber coated dumbbell 10KG', 0.3, 0.12, 0.35, 20.5))
# packer.add_item(Box('Hexagon rubber coated dumbbell 15KG', 0.18, 0.14, 0.37, 15.5))
# packer.add_item(Box('Hexagon rubber coated dumbbell 20KG', 0.21, 0.15, 0.39, 20.5))
# packer.add_item(Box('Neoprene Coated dumbbell 1KG', 0.19, 0.24, 0.31, 20.5))
# packer.add_item(Box('Neoprene Coated dumbbell 2KG', 0.23, 0.16, 0.32, 16.5))
# packer.add_item(Box('Neoprene Coated dumbbell 5KG', 0.24, 0.1, 0.26, 10.5))