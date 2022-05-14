from PIL import Image, ImageFilter, ImageDraw, ImageFont, ImageColor, ImageEnhance

import os

os.chdir("your_path/and your_folder")

for file in os.scandir('.'): 
   if (file.path.endswith(".jpeg") or file.path.endswith(".jpg")) or file.path.endswith("png") and file.is_file():

      img = Image.open(file.path)
      fn, flext = os.path.splitext(file)
      b_w = img.convert("L")
      detail = b_w.filter(ImageFilter.DETAIL)
      resize = detail.resize((1080, 1080))
      width, height = resize.size
      draw = ImageDraw.Draw(resize)
      watermark  = "Simple_watermark"
      color = "WHITE"
      font = ImageFont.truetype("/Bullpen3D.ttf", 60)
      textwidth, textheight = draw.textsize(watermark, font)
      edge = 10 
      p_x = width - textwidth - edge
      p_y = height - textheight - edge 

      draw.text((p_x, p_y), watermark, color, font=font) 
      resize.save('{0}{1}'.format(fn, flext))