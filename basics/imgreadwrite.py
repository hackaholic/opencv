import cv2
import sys
import os

filename = sys.argv[1]

img = cv2.imread(filename, -1)
cv2.imshow("image", img)
key = cv2.waitKey(0)
print("Key pressed -> " + chr(key))
if key == 113:
    cv2.destroyAllWindows()
elif key == 115:
    basename =  os.path.basename(filename).split(".")
    cv2.imwrite("{}_copy.{}".format(basename[0], basename[1]), img)
    cv2.destroyAllWindows()
