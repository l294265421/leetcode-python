'''
 An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus
any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned
pixels with the newColor.

At the end, return the modified image.

Example 1:

Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.

Note:
The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
'''
from queue import Queue

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        row_len = len(image)
        column_len = len(image[0])
        flood_filled_position = [[0 for column in row] for row in image]
        origional_color = image[sr][sc]
        helper = Queue()
        helper.put([sr, sc])
        flood_filled_position[sr][sc] = 1
        while not helper.empty():
            current_start = helper.get()
            current_start_row = current_start[0]
            current_start_column = current_start[1]
            image[current_start[0]][current_start[1]] = newColor
            self.one_position(image, row_len, column_len, helper, flood_filled_position, current_start_row - 1, current_start_column, origional_color)
            self.one_position(image, row_len, column_len, helper, flood_filled_position, current_start_row + 1, current_start_column, origional_color)
            self.one_position(image, row_len, column_len, helper, flood_filled_position, current_start_row, current_start_column - 1, origional_color)
            self.one_position(image, row_len, column_len, helper, flood_filled_position, current_start_row, current_start_column + 1, origional_color)
        return image

    def one_position(self, image, row_len, column_len,helper, flood_filled_position, row, column, origional_color):
        if row >= 0 and row < row_len and column >= 0 and column < column_len and flood_filled_position[row][column] == 0 \
                and image[row][column] == origional_color:
            helper.put([row, column])
            flood_filled_position[row][column] = 1

if __name__ == '__main__':
    solution = Solution()
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(solution.floodFill(image, 1, 1, 2))



