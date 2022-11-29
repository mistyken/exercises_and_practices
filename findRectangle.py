"""
Imagine we have an image. We'll represent this image as a simple 2D array where every pixel is a 1 or a 0.

The image you get is known to have potentially many distinct rectangles of 0s on a background of 1's. Write a function that takes in the image and returns the coordinates of all the 0 rectangles -- top-left and bottom-right; or top-left, width and height.

image1 = [
   0  1  2  3  4  5  6
  [0, 1, 1, 1, 1, 1, 1], 0
  [1, 1, 1, 1, 1, 1, 1], 1
  [0, 1, 1, 0, 0, 0, 1], 2
  [1, 0, 1, 0, 0, 0, 1], 3
  [1, 0, 1, 1, 1, 1, 1], 4
  [1, 0, 1, 0, 0, 1, 1], 5
  [1, 1, 1, 0, 0, 1, 1], 6
  [1, 1, 1, 1, 1, 1, 0], 7
]

Sample output variations (only one is necessary):

findRectangles(image1) =>
  // (using top-left-row-column and bottom-right):
  [
    [[0,0],[0,0]],
    [[2,0],[2,0]],
    [[2,3],[3,5]],
    [[3,1],[5,1]],
    [[5,3],[6,4]],
    [[7,6],[7,6]],
  ]
  // (using top-left-row-column and width/height):
  [
    [[0,0],[1,1]],
    [[2,0],[1,1]],
    [[2,3],[3,2]],
    [[3,1],[1,3]],
    [[5,3],[2,2]],
    [[7,6],[1,1]],
  ]

Other test cases:

image2 = [
  [0],
]

findRectangles(image2) =>
  // (using top-left-row-column and bottom-right):
  [
    [[0,0],[0,0]],
  ]

  // (using top-left-row-column and width/height):
  [
    [[0,0],[1,1]],
  ]

image3 = [
  [1],
]

findRectangles(image3) => []

image4 = [
  [1, 1, 1, 1, 1],
  [1, 0, 0, 0, 1],
  [1, 0, 0, 0, 1],
  [1, 0, 0, 0, 1],
  [1, 1, 1, 1, 1],
]

findRectangles(image4) =>
  // (using top-left-row-column, and bottom-right or width/height):
  [
    [[1,1],[3,3]],
  ]

n: number of rows in the input image
m: number of columns in the input image
"""



image2 = [
  [0],
]

image3 = [
  [1],
]

image4 = [
  [1, 1, 1, 1, 1],
  [1, 0, 0, 0, 1],
  [1, 0, 0, 0, 1],
  [1, 0, 0, 0, 1],
  [1, 1, 1, 1, 1],
]

image1 = [
  #0  1  2  3  4  5  6
  [0, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [0, 1, 1, 0, 0, 0, 1],
  [1, 0, 1, 0, 0, 0, 1],
  [1, 0, 1, 1, 1, 1, 1],
  [1, 0, 1, 0, 0, 1, 1],
  [1, 1, 1, 0, 0, 1, 1],
  [1, 1, 1, 1, 1, 1, 0],
]

def findRectangles(image):
    starts = []
    dimensions = []
    for y in range(len(image)):
        for x in range(len(image[y])):
            for point, dimension in zip(starts, dimensions):
                if y <= point[0] + dimension[0] and x <= point[1] + dimension[1]:
                    break
                else:
                    result = findRectangle(image[y: len(image)][x: len(image[y])])

def findRectangle(image):
    start = []
    width = 0
    # O(W)
    for y in range(len(image)):
        for x in range(len(image[y])):
            if image[y][x] == 0:
                if not start:
                    start.append((y, x))
                else:
                    width += 1
            if start and image[y][x] == 1:
                break
        if start:
            break
    
    column = 0
    #O(Height)
    for x in range(start[0][1], len(image[0])):
        for y in range(start[0][0], len(image)):
            print("num {} coord {} count {}".format(image[y][x], (y, x), column))
            if image[y][x] == 0:
                column += 1
            else:
                break
        break
        
    #O(H + W)
    #O(1)
    
    return start[0][0], start[0][1], width + 1, column

print(findRectangle(image1))
print(findRectangle(image2))
print(findRectangle(image3))
print(findRectangle(image4))



