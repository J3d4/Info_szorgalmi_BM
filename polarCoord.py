import csvHandler, math
from tqdm import tqdm

# csvHandler
dict = csvHandler.DictReader()
write = csvHandler.Write()
read = csvHandler.Read()
# misc
encoding = 'utf-8'
delimiter = ';'
# inputs
fileIn = 'polarCoord.csv'
input = read.dataFrame(fileIn, encoding, delimiter)
coord = dict.read(input)
# outputs
fileOut = 'polarCoordCalculated.csv'
head = write.header(coord)
# variables
refPoint = "A"
points = ["B","C","D","E","F"]
##############################################################

def calculate(coord):
    for i in tqdm(range(len(coord))):
        for j in range(len(coord)):
            for k in range(len(points)):
                if(refPoint in coord[i].pont and points[k] in coord[j].pont):
                    deltaX = float(coord[i].xCoord) - float(coord[j].xCoord)
                    deltaY = float(coord[i].yCoord) - float(coord[j].yCoord)
                    coord[j].irany = math.degrees(math.atan2(deltaY, deltaX))
                    coord[j].tavolsag = math.sqrt(deltaX**2 + deltaY**2)

    return coord

# run
if __name__ == '__main__':
    print("Calculating ->")
    calculate(coord)
    print("Writing data out ->")
    write.writer(fileOut, head, coord, encoding, delimiter)
    print(" ")