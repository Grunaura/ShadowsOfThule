def text_to_image(
    text: str,
    font_filepath: str,
    font_size: int,
    color: Tuple[int, int, int, int],
) -> ImageType:
    font = ImageFont.truetype(font_filepath, size=font_size)

    img = Image.new("RGBA", font.getmask(text).size)

    draw = ImageDraw.Draw(img)
    draw_point = (0, 0)

    draw.multiline_text(draw_point, text, font=font, fill=color)
    font = ImageFont.truetype(font_filepath, size=font_size)

    text_window = img.getbbox()
    img = img.crop(text_window)


    return img