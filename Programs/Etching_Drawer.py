import shutil, sys

UP_DOWN_CHAR         = chr(9474)
LEFT_RIGHT_CHAR      = chr(9472)
DOWN_RIGHT_CHAR      = chr(9484)
DOWN_LEFT_CHAR       = chr(9488)
UP_RIGHT_CHAR        = chr(9492)
UP_LEFT_CHAR         = chr(9496)
UP_DOWN_RIGHT_CHAR   = chr(9500)
UP_DOWN_LEFT_CHAR    = chr(9508)
DOWN_LEFT_RIGHT_CHAR = chr(9516)
UP_LEFT_RIGHT_CHAR   = chr(9524)
CROSS_CHAR           = chr(9532)

CANVAS_WIDTH, CANVAS_HEIGHT = shutil.get_terminal_size()
CANVAS_WIDTH -= 1
CANVAS_HEIGHT -= 5

canvas = {}
cursorX = 0
cursorY = 0

def getCanvasString(canvasData, cx, cy):
    canvasStr = ''
    for rowNum in range(CANVAS_HEIGHT):
        for columnNum in range(CANVAS_WIDTH):
            if columnNum == cx and rowNum == cy:
                canvasStr += '#'
                continue
            cell = canvasData.get((columnNum, rowNum))
            if cell in (set(['W', 'S']), set(['W']), set(['S'])):
                canvasStr += UP_DOWN_CHAR
            # Add more conditions for other characters...
            elif cell == None:
                canvasStr += ' '
        canvasStr += '\n'
    return canvasStr

moves = []
while True:
    print(getCanvasString(canvas, cursorX, cursorY))
    print('WASD keys to move, H for help, C to clear, F to save, or QUIT.')
    response = input('> ').upper()

    if response == 'QUIT':
        print('Thanks for playing!')
        sys.exit()
    # Add more conditions and actions based on user input...

