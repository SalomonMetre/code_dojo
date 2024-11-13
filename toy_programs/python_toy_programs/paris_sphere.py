import math

import cairo

WIDTH, HEIGHT = 600, 600
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)


def draw_sphere(context, center_x, center_y, radius):
    context.arc(center_x, center_y, radius, 0, 2 * math.pi)
    gradient = cairo.RadialGradient(center_x - radius * 0.5, center_y - radius * 0.5, radius * 0.2,
                                    center_x, center_y, radius)
    gradient.add_color_stop_rgb(0, 1, 1, 1)
    gradient.add_color_stop_rgb(0.7, 0.5, 0.5, 0.5)
    gradient.add_color_stop_rgb(1, 0.1, 0.1, 0.1)
    context.set_source(gradient)
    context.fill()


context.set_source_rgb(0.2, 0.2, 0.2)
context.paint()
draw_sphere(context, WIDTH // 2, HEIGHT // 2, 200)
surface.write_to_png("3d_sphere.png")

print("3D sphere image created!")