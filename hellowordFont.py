import pygame

def make_font(fonts, size):
    available = pygame.font.get_fonts()
   
    # get_fonts() returns a list of lowercase spaceless font names 
    choices = map(lambda x:x.lower().replace(' ', ''), fonts)
    for choice in choices:
        if choice in available:
            return pygame.font.SysFont(choice, size)
    return pygame.font.Font(None, size)
    
_cached_fonts = {}
def get_font(font_preferences, size):
    global _cached_fonts
    key = str(font_preferences) + '|' + str(size)
    font = _cached_fonts.get(key, None)
    if font == None:
        font = make_font(font_preferences, size)
        _cached_fonts[key] = font
    return font

_cached_text = {}
def create_text(text, fonts, size, color):
    global _cached_text
    key = '|'.join(map(str, (fonts, size, color, text)))
    image = _cached_text.get(key, None)
    if image == None:
        font = get_font(fonts, size)
        get_bold() 
        image = font.render(text, True, color)
        _cached_text[key] = image
    return image

pygame.init()
screen = pygame.display.set_mode((1024, 768))  
clock = pygame.time.Clock()
done = False

font_preferences = [
        "Bizarre-Ass Font Sans Serif",
        "They definitely dont have this installed Gothic",
        "Arial",
        "Comic Sans MS"]

text = create_text("Hola Mundo", font_preferences, 60, (2, 200, 0))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
    
    screen.fill((0, 0, 0))
    screen.blit(text,
        (520 - text.get_width() // 2, 340 - text.get_height() // 2))
    
    pygame.display.flip()
    clock.tick(60)