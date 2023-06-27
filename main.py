import arcade

"""
Polashi Dey
406
Tp 5


Description: Ce code consiste a dessiner un image de la ville lors du coucher de soleil a l'aide de librairie Arcade.
"""

"""
Le code en sous est le code pour le format de l'ecran qui restera toujours la même.
"""

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINDOW_TITTLE = "projet tp 5"

"""
Le fonction draw_background consiste a dessiner le coucher du soleil.
"""


def draw_background():
    arcade.draw_lrtb_rectangle_filled(0, 800, 100, 0, arcade.color.BLACK)
    arcade.draw_lrtb_rectangle_filled(0, 800, 200, 100, arcade.color.BLACK)
    arcade.draw_lrtb_rectangle_filled(0, 800, 300, 200, arcade.color.PERSIMMON)
    arcade.draw_lrtb_rectangle_filled(0, 800, 400, 300, arcade.color.DARK_ORANGE)
    arcade.draw_lrtb_rectangle_filled(0, 800, 500, 400, arcade.color.BARBIE_PINK)


"""
Le fonction draw_batiments consiste a dessiner toutes les batiments de l'image.
"""


def draw_batiments():
    arcade.draw_lrtb_rectangle_filled(100, 150, 350, 200, arcade.color.BLACK)
    arcade.draw_lrtb_rectangle_filled(200, 250, 400, 200, arcade.color.BLACK)
    arcade.draw_lrtb_rectangle_filled(300, 350, 350, 200, arcade.color.BLACK)
    arcade.draw_lrtb_rectangle_filled(400, 500, 300, 200, arcade.color.BLACK)
    arcade.draw_lrtb_rectangle_filled(550, 600, 450, 200, arcade.color.BLACK)
    arcade.draw_lrtb_rectangle_filled(650, 750, 400, 200, arcade.color.BLACK)


"""
Le fonction draw_batiment1 consiste a dessiner les fenetres et le toit de la 1ere batiment du gauche.
"""


def draw_batiment1():
    arcade.draw_lrtb_rectangle_filled(105, 120, 220, 205, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(130, 145, 220, 205, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(105, 120, 245, 230, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(130, 145, 245, 230, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(105, 120, 270, 255, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(130, 145, 270, 255, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(105, 120, 295, 280, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(130, 145, 295, 280, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(105, 120, 320, 305, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(130, 145, 320, 305, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(105, 120, 345, 330, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(130, 145, 345, 330, arcade.color.WHITE)

    """
    Le code pour les fenetres.
    """

    y = SCREEN_HEIGHT / 2 + 50
    arcade.draw_triangle_filled(100, y + 0, 150, y - 0, 125, y + 50, arcade.color.BLACK)


"""
Le code pour le toit
"""


"""
Le fonction draw_batiment2 cosiste a dessiner les fenetres et le toit du 2eme batiment de gauche.
"""


def draw_batiment2():
    arcade.draw_lrtb_rectangle_filled(205, 220, 220, 205, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(230, 245, 220, 205, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(205, 220, 245, 230, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(230, 245, 245, 230, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(205, 220, 270, 255, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(230, 245, 270, 255, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(205, 220, 295, 280, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(230, 245, 295, 280, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(205, 220, 320, 305, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(230, 245, 320, 305, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(205, 220, 345, 330, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(230, 245, 345, 330, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(205, 220, 370, 355, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(230, 245, 370, 355, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(205, 220, 395, 380, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(230, 245, 395, 380, arcade.color.WHITE)

    """ Le code pour les fenetres"""

    y = SCREEN_HEIGHT / 2 + 100
    arcade.draw_triangle_filled(200, y + 0,
                                250, y - 0,
                                225, y + 50,
                                arcade.color.BLACK)
    """ Le code pour le toit"""


"""
Le def draw_batiment3 consiste a dessiner les fenetres et le toit 3eme batiment du gauche.
"""


def draw_batiment3():
    arcade.draw_lrtb_rectangle_filled(305, 320, 220, 205, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(330, 345, 220, 205, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(305, 320, 245, 230, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(330, 345, 245, 230, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(305, 320, 270, 255, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(330, 345, 270, 255, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(305, 320, 295, 280, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(330, 345, 295, 280, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(305, 320, 320, 305, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(330, 345, 320, 305, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(305, 320, 345, 330, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(330, 345, 345, 330, arcade.color.WHITE)

    """ Le code pour les fenetres"""

    y = SCREEN_HEIGHT / 2 + 50
    arcade.draw_triangle_filled(300, y + 0,
                                350, y - 0,
                                325, y + 50,
                                arcade.color.BLACK)
    """ Le code pour le toit"""


"""
Le fonction batiment4 consiste a dessiner le nom,le toit et la porte du 3eme batiment de droite.
"""


def draw_batiment4():
    arcade.draw_arc_filled(450, SCREEN_HEIGHT / 2 + 0, 100, 100, arcade.csscolor.BLACK, 0, 180)
    arcade.draw_text("MARCHÉ", 415, SCREEN_HEIGHT / 2 - 10, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(425, 475, 260, 200, arcade.color.WHITE)
    arcade.draw_line(415, 290, 485, 290, arcade.color.BARBIE_PINK, 1)


"""
Le fontion batiment5 consiste a dessiner les fenetres du 2eme batiment du droite.
"""


def draw_batiment5():
    arcade.draw_lrtb_rectangle_filled(555, 570, 220, 205, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(580, 595, 220, 205, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(555, 570, 245, 230, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(580, 595, 245, 230, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(555, 570, 270, 255, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(580, 595, 270, 255, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(555, 570, 295, 280, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(580, 595, 295, 280, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(555, 570, 320, 305, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(580, 595, 320, 305, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(555, 570, 345, 330, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(580, 595, 345, 330, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(555, 570, 370, 355, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(580, 595, 370, 355, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(555, 570, 395, 380, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(580, 595, 395, 380, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(555, 570, 420, 405, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(580, 595, 420, 405, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(555, 570, 445, 430, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(580, 595, 445, 430, arcade.color.WHITE)


"""
Le fonction draw_batiment6 consiste a dessiner les fenetres du  1ere batiment du droite.
"""


def draw_batiment6():
    arcade.draw_lrtb_rectangle_filled(660, 740, 230, 205, arcade.color.CREAM)
    arcade.draw_lrtb_rectangle_filled(660, 740, 275, 250, arcade.color.CREAM)
    arcade.draw_lrtb_rectangle_filled(660, 740, 320, 295, arcade.color.CREAM)
    arcade.draw_lrtb_rectangle_filled(660, 740, 365, 340, arcade.color.CREAM)


"""
Le fonction draw_arbre consiste a dessiner les arbres.
"""


def draw_arbre():
    arcade.draw_lrtb_rectangle_filled(45, 55, 275, 200, arcade.color.BROWN)
    points = [(35, 275), (65, 275), (85, 300), (50, 350), (15, 300)]
    arcade.draw_polygon_filled(points, arcade.color.BANGLADESH_GREEN)

    arcade.draw_lrtb_rectangle_filled(370, 380, 245, 200, arcade.color.BROWN)
    arcade.draw_ellipse_filled(375, 250, 25, 45, arcade.color.BANGLADESH_GREEN)


"""
Le fonction draw_soleil consiste a dessiner le soleil.
"""


def draw_soleil():
    arcade.draw_circle_filled(700, 500, 70, arcade.color.DARK_ORANGE)


"""
Le fonction main consiste a dessiner toutes les fonctions d'image enfin de commencer et finir le proccesus du dessin 
avec arcade.
"""


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITTLE)
    arcade.set_background_color(arcade.color.DEBIAN_RED)
    arcade.start_render()
    draw_background()
    draw_batiments()
    draw_batiment1()
    draw_batiment2()
    draw_batiment3()
    draw_batiment4()
    draw_batiment5()
    draw_batiment6()
    draw_arbre()
    draw_soleil()

    arcade.finish_render()
    arcade.run()


main()
