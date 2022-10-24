from PIL import Image, ImageDraw, ImageFont
from flask import url_for

def write_on_img(message):
  #img = Image.open("{{ url_for('static', filename='2.jpg') }}")
  img = Image.open("static/2.jpg")
  font = ImageFont.truetype('static/莫大毛筆-Regular.ttf', 90)
  #font = ImageFont.load_default()
  imgDraw = ImageDraw.Draw(img)

  textWidth, textHeight = imgDraw.textsize(message, font=font)
  xText = 530
  yText = 370

  imgDraw.multiline_text((xText, yText), message, font=font, fill=(50, 50, 50), spacing=35)
  return img