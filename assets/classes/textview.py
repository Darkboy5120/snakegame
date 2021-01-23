import pygame

class Textview:
    def __init__(self, x, y, spacing, text, style):
        self.x = x
        self.y = y
        self.width = None
        self.height = None
        self.paddingX = spacing["paddingX"]
        self.paddingY = spacing["paddingY"]
        self.text = text
        self.textSize = style["textSize"]
        self.font = pygame.font.Font(None, self.textSize)
        self.defaultTextColor = style["defaultTextColor"]
        self.hoverTextColor = style["hoverTextColor"]
        self.clickTextColor = style["clickTextColor"]
        self.defaultBdColor = style["defaultBdColor"]
        self.hoverBdColor = style["hoverBdColor"]
        self.clickBdColor = style["clickBdColor"]
        self.currentBdColor = self.defaultBdColor
        self.currentTextColor = self.defaultTextColor
        self.fontRender = None
        self.fontRenderRect = None
        self.shadowColor = style["shadowColor"]
        self.shadowRect = None
        self.rect = None
        self.buildRect()
        
    def setText(self, text):
        self.text = text
        self.buildRect()
    def buildRect(self):
        self.fontRender = self.font.render(self.text, True, self.currentTextColor)
        if (len(self.currentTextColor)==4): self.fontRender.set_alpha(self.currentTextColor[3])
        self.fontRenderRect = self.fontRender.get_rect()
        self.width = self.fontRenderRect.width + (self.paddingX * 2)
        self.height = self.fontRenderRect.height + (self.paddingY * 2)
        self.rect = pygame.rect.Rect(self.x, self.y, self.width, self.height)
        self.fontRenderRect.x = self.x + self.paddingX
        self.fontRenderRect.y = self.y + self.paddingY
        self.shadowRect = pygame.rect.Rect(self.x, self.y, self.width+2, self.height+4)
    def getRect(self):
        return self.rect
    def draw(self, surface):
        shadow = pygame.Surface(self.shadowRect.size, pygame.SRCALPHA)
        shadow.fill(self.shadowColor)
        surface.blit(shadow, self.shadowRect)

        body = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        body.fill(self.currentBdColor)
        surface.blit(body, self.rect)
        
        surface.blit(self.fontRender, self.fontRenderRect)
    def hover(self):
        self.currentBdColor = self.hoverBdColor
        self.currentTextColor = self.hoverTextColor
        self.buildRect()
    def click(self):
        self.currentBdColor = self.clickBdColor
        self.currentTextColor = self.clickTextColor
        self.buildRect()
    def default(self):
        self.currentBdColor = self.defaultBdColor
        self.currentTextColor = self.defaultTextColor
        self.buildRect()
