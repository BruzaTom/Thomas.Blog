from PIL import Image

path = 'static/images/meandautumn.jpg'
# Open the original image
original_image = Image.open(path)

img_width, img_height = original_image.size
# Define the new size
new_width = img_width / 1.5  # 768 * 1.5 = 1152
new_height = img_height / 1.5  # 768 * 1.5 = 1152

uinput = input('option: ')
if uinput == 'r':
    # Resize the image
    resized_image = original_image.resize((int(new_width), int(new_height)), Image.Resampling.LANCZOS)
    # Save the resized image
    resized_image.save('static/images/meandautumn_rs.jpg')
if uinput == 'f':
    flipped_image = original_image.transpose(Image.FLIP_TOP_BOTTOM)
    # Save or display the flipped image
    flipped_image.save('sprites/space_jet.png')
    flipped_image.show()
if uinput == 's':
    img_width, img_height = original_image.size
    # Define the number of rows and columns
    rows = 9
    cols = 9
    # Calculate the width and height of each tile
    tile_width = img_width // cols
    tile_height = img_height // rows
    # Loop through the image and save each tile
    index = 0
    for row in range(rows):
        for col in range(cols):
            left = col * tile_width
            upper = row * tile_height
            right = (col + 1) * tile_width
            lower = (row + 1) * tile_height
            # Crop the image
            tile = original_image.crop((left, upper, right, lower))
            # Save the tile
            tile.save(f'sprites/explo_frames/{index}.png')
            index += 1