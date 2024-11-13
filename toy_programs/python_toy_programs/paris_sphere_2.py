import math
import cairo

# Set up image dimensions and surface
WIDTH, HEIGHT = 600, 800
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)

# Define colors for the trophy
gold_very_bright = (1, 0.95, 0.4)  # Very bright gold color
gold_bright = (1, 0.84, 0)         # Bright gold color
gold_dark = (0.85, 0.65, 0.1)      # Dark gold color
gold_deep = (0.6, 0.4, 0)          # Deep gold color

def draw_trophy_body(context, center_x, center_y, radius):
    # Draw the main body (a sphere) with a multi-stop gradient
    context.arc(center_x, center_y, radius, 0, 2 * math.pi)
    gradient = cairo.RadialGradient(center_x - radius * 0.4, center_y - radius * 0.4, radius * 0.2,
                                    center_x, center_y, radius)
    gradient.add_color_stop_rgb(0, *gold_very_bright)
    gradient.add_color_stop_rgb(0.4, *gold_bright)
    gradient.add_color_stop_rgb(0.7, *gold_dark)
    gradient.add_color_stop_rgb(1, *gold_deep)
    context.set_source(gradient)
    context.fill()

def draw_central_handle(context, center_x, center_y, handle_width, handle_height):
    # Draw a shorter central handle from base to main body, stopping just before the base
    context.rectangle(center_x - handle_width / 2, center_y, handle_width, handle_height)
    gradient = cairo.LinearGradient(center_x - handle_width / 2, center_y, center_x + handle_width / 2, center_y + handle_height)
    gradient.add_color_stop_rgb(0, *gold_deep)
    gradient.add_color_stop_rgb(0.5, *gold_dark)
    gradient.add_color_stop_rgb(1, *gold_bright)
    context.set_source(gradient)
    context.fill()

def draw_stand_and_base(context, center_x, center_y, width, height):
    # Draw the stand under the main body with a gradient
    context.rectangle(center_x - width / 4, center_y, width / 2, height / 2)
    gradient = cairo.LinearGradient(center_x - width / 4, center_y, center_x + width / 4, center_y + height / 2)
    gradient.add_color_stop_rgb(0, *gold_bright)
    gradient.add_color_stop_rgb(1, *gold_dark)
    context.set_source(gradient)
    context.fill()

    # Draw the base
    context.rectangle(center_x - width / 2, center_y + height / 2, width, height)
    gradient = cairo.LinearGradient(center_x - width / 2, center_y + height / 2, center_x + width / 2, center_y + height)
    gradient.add_color_stop_rgb(0, *gold_dark)
    gradient.add_color_stop_rgb(1, *gold_deep)
    context.set_source(gradient)
    context.fill()

def draw_shadow(context, center_x, center_y, radius, shadow_offset, blur_radius):
    # Draw a shadow ellipse under the trophy
    context.save()
    context.translate(center_x + shadow_offset, center_y + shadow_offset)
    context.scale(1, 0.2)
    context.arc(0, radius * 8, radius, 0, 2 * math.pi)
    shadow_gradient = cairo.RadialGradient(0, radius * 8, blur_radius, 0, radius * 8, radius * 1.5)
    shadow_gradient.add_color_stop_rgba(0, 0, 0, 0, 0.3)
    shadow_gradient.add_color_stop_rgba(1, 0, 0, 0, 0)
    context.set_source(shadow_gradient)
    context.fill()
    context.restore()

# Set background color
context.set_source_rgb(0.1, 0.1, 0.1)
context.paint()

# Draw the shadow first to layer it correctly
center_x, center_y = WIDTH // 2, HEIGHT // 2 - 100
draw_shadow(context, center_x, center_y, 150, shadow_offset=10, blur_radius=50)

# Draw the trophy components
handle_height = 200  # Shorter length of the central handle to avoid going beyond the base
handle_width = 20    # Width of the central handle
draw_central_handle(context, center_x, center_y + 150, handle_width, handle_height)
draw_trophy_body(context, center_x, center_y, 150)
draw_stand_and_base(context, center_x, HEIGHT // 2 + 150, 200, 80)

# Save the result
surface.write_to_png("trophy_with_shortened_handle_and_shadow.png")
print("Trophy with a shorter central handle, varied gradient, and shadow effect created!")
