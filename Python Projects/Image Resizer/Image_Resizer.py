import cv2

# Configurable Parameters:
source = "Challenger.jpg"
destination = "ModifiedImage.jpeg"
scale_percent = 50

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
#cv2.imshow("title",src)

# Percentage by which the Image is Resized:

# Calculate the 50 Percent of Original Dimensions

new_width = int(src.shape[1] * scale_percent/100)
new_height = int(src.shape[0] * scale_percent/100)

# Resize Image:
output = cv2.resize(src,(new_width, new_height))

cv2.imwrite(destination,output)
# cv2.waitkey(0)
